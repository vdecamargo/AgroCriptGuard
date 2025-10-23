"""
Módulo de criptografia usando AES-GCM.
Implementa funções de encrypt/decrypt com autenticação.
"""

import secrets
import base64
from typing import Optional, Dict
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag

from config import NONCE_SIZE


class CryptoManager:
    """Gerencia operações de criptografia AES-GCM."""
    
    def __init__(self, key: bytes):
        """
        Inicializa o gerenciador com uma chave.
        
        Args:
            key: Chave de 32 bytes (256 bits)
        """
        if len(key) != 32:
            raise ValueError("Chave deve ter 32 bytes (256 bits)")
        
        self.aesgcm = AESGCM(key)
    
    def encrypt(self, plaintext: str) -> Optional[Dict[str, str]]:
        """
        Criptografa texto usando AES-GCM.
        
        Args:
            plaintext: Texto em formato string
            
        Returns:
            Dicionário com nonce, ciphertext e tag em base64
        """
        try:
            # Gera nonce aleatório (NUNCA REUTILIZAR com a mesma chave)
            nonce = secrets.token_bytes(NONCE_SIZE)
            
            # Converte texto para bytes
            data = plaintext.encode('utf-8')
            
            # Criptografa (retorna ciphertext + tag concatenados)
            ciphertext_with_tag = self.aesgcm.encrypt(nonce, data, None)
            
            # Separa ciphertext e tag (tag são os últimos 16 bytes)
            ciphertext = ciphertext_with_tag[:-16]
            tag = ciphertext_with_tag[-16:]
            
            # Retorna tudo em base64
            return {
                "nonce": base64.b64encode(nonce).decode('utf-8'),
                "ciphertext": base64.b64encode(ciphertext).decode('utf-8'),
                "tag": base64.b64encode(tag).decode('utf-8')
            }
            
        except Exception as e:
            print(f"Erro na criptografia: {e}")
            return None
    
    def decrypt(self, encrypted_data: Dict[str, str]) -> Optional[str]:
        """
        Descriptografa dados criptografados com AES-GCM.
        
        Args:
            encrypted_data: Dicionário com nonce, ciphertext e tag
            
        Returns:
            Texto descriptografado ou None se falhar
        """
        try:
            # Decodifica de base64
            nonce = base64.b64decode(encrypted_data["nonce"])
            ciphertext = base64.b64decode(encrypted_data["ciphertext"])
            tag = base64.b64decode(encrypted_data["tag"])
            
            # Reconstrói dados para decrypt (ciphertext + tag)
            ciphertext_with_tag = ciphertext + tag
            
            # Descriptografa e verifica autenticidade
            plaintext_bytes = self.aesgcm.decrypt(nonce, ciphertext_with_tag, None)
            
            return plaintext_bytes.decode('utf-8')
            
        except InvalidTag:
            print("Erro: Tag de autenticação inválida (dados corrompidos ou chave errada)")
            return None
        except Exception as e:
            print(f"Erro na descriptografia: {e}")
            return None
