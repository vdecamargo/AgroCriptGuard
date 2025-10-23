"""
Módulo de autenticação e gerenciamento de senha mestra.
Implementa hash seguro com Argon2 e derivação de chave criptográfica.
"""

import json
import secrets
import base64
from argon2 import PasswordHasher
from argon2.low_level import hash_secret_raw, Type
from pathlib import Path
from typing import Optional, Tuple

from config import AUTH_FILE, ARGON2_TIME_COST, ARGON2_MEMORY_COST, \
    ARGON2_PARALLELISM, ARGON2_HASH_LEN, ARGON2_SALT_LEN


class AuthManager:
    """Gerencia autenticação e derivação de chaves."""
    
    def __init__(self):
        self.ph = PasswordHasher(
            time_cost=ARGON2_TIME_COST,
            memory_cost=ARGON2_MEMORY_COST,
            parallelism=ARGON2_PARALLELISM,
            hash_len=ARGON2_HASH_LEN,
            salt_len=ARGON2_SALT_LEN
        )
    
    def user_exists(self) -> bool:
        """Verifica se já existe usuário cadastrado."""
        return AUTH_FILE.exists()
    
    def create_user(self, password: str) -> bool:
        """
        Cria novo usuário com senha mestra.
        
        Args:
            password: Senha em texto plano
            
        Returns:
            True se criado com sucesso, False caso contrário
        """
        try:
            if self.user_exists():
                return False
            
            # Gera salt aleatório
            salt = secrets.token_bytes(ARGON2_SALT_LEN)
            
            # Gera hash da senha para armazenamento
            password_hash = self.ph.hash(password)
            
            # Salva hash e salt em base64
            auth_data = {
                "password_hash": password_hash,
                "salt": base64.b64encode(salt).decode('utf-8')
            }
            
            with open(AUTH_FILE, 'w') as f:
                json.dump(auth_data, f, indent=2)
            
            return True
            
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            return False
    
    def verify_password(self, password: str) -> bool:
        """
        Verifica se a senha fornecida está correta.
        
        Args:
            password: Senha em texto plano
            
        Returns:
            True se senha correta, False caso contrário
        """
        try:
            if not self.user_exists():
                return False
            
            with open(AUTH_FILE, 'r') as f:
                auth_data = json.load(f)
            
            password_hash = auth_data.get("password_hash")
            
            # Verifica o hash
            self.ph.verify(password_hash, password)
            
            # Verifica se precisa rehash (parâmetros mudaram)
            if self.ph.check_needs_rehash(password_hash):
                # Atualiza o hash com novos parâmetros
                auth_data["password_hash"] = self.ph.hash(password)
                with open(AUTH_FILE, 'w') as f:
                    json.dump(auth_data, f, indent=2)
            
            return True
            
        except Exception as e:
            print(f"Erro na verificação: {e}")
            return False
    
    def derive_key(self, password: str) -> Optional[bytes]:
        """
        Deriva chave criptográfica a partir da senha usando Argon2 como KDF.
        
        Args:
            password: Senha em texto plano
            
        Returns:
            Chave de 32 bytes ou None se falhar
        """
        try:
            if not self.user_exists():
                return None
            
            with open(AUTH_FILE, 'r') as f:
                auth_data = json.load(f)
            
            # Recupera salt armazenado
            salt = base64.b64decode(auth_data["salt"])
            
            # Deriva chave usando Argon2id (recomendado para KDF)
            key = hash_secret_raw(
                secret=password.encode('utf-8'),
                salt=salt,
                time_cost=ARGON2_TIME_COST,
                memory_cost=ARGON2_MEMORY_COST,
                parallelism=ARGON2_PARALLELISM,
                hash_len=ARGON2_HASH_LEN,
                type=Type.ID  # Argon2id é o mais seguro
            )
            
            return key
            
        except Exception as e:
            print(f"Erro na derivação de chave: {e}")
            return None
