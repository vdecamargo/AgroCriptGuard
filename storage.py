"""
Módulo de armazenamento criptografado.
Gerencia persistência de dados agrícolas em arquivos JSON criptografados.
"""

import json
from typing import Optional, List, Dict, Any
from pathlib import Path

from crypto import CryptoManager
from config import ENCRYPTED_DATA_FILE


class StorageManager:
    """Gerencia armazenamento criptografado de dados."""
    
    def init(self, crypto_manager: CryptoManager):
        """
        Inicializa o gerenciador de armazenamento.
        
        Args:
            crypto_manager: Instância do CryptoManager
        """
        self.crypto = crypto_manager
    
    def save_data(self, data: List[Dict[str, Any]]) -> bool:
        """
        Salva dados criptografados em arquivo.
        
        Args:
            data: Lista de registros agrícolas
            
        Returns:
            True se salvou com sucesso, False caso contrário
        """
        try:
            # Converte dados para JSON
            json_data = json.dumps(data, ensure_ascii=False, indent=2)
            
            # Criptografa
            encrypted = self.crypto.encrypt(json_data)
            
            if encrypted is None:
                return False
            
            # Salva arquivo criptografado
            with open(ENCRYPTED_DATA_FILE, 'w') as f:
                json.dump(encrypted, f, indent=2)
            
            return True
            
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")
            return False
    
    def load_data(self) -> Optional[List[Dict[str, Any]]]:
        """
        Carrega e descriptografa dados do arquivo.
        
        Returns:
            Lista de registros ou lista vazia se arquivo não existir,
            None se houver erro na descriptografia
        """
        try:
            # Se arquivo não existe, retorna lista vazia
            if not ENCRYPTED_DATA_FILE.exists():
                return []
            
            # Carrega dados criptografados
            with open(ENCRYPTED_DATA_FILE, 'r') as f:
                encrypted_data = json.load(f)
            
            # Descriptografa
            decrypted_json = self.crypto.decrypt(encrypted_data)
            
            if decrypted_json is None:
                return None
            
            # Converte de JSON para Python
            data = json.loads(decrypted_json)
            
            return data
            
        except json.JSONDecodeError:
            print("Erro: Arquivo de dados corrompido")
            return None
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return None
    
    def add_record(self, record: Dict[str, Any]) -> bool:
        """Adiciona novo registro aos dados."""
        data = self.load_data()
        if data is None:
            return False
        
        data.append(record)
        return self.save_data(data)
    
    def update_record(self, index: int, record: Dict[str, Any]) -> bool:
        """Atualiza registro existente."""
        data = self.load_data()
        if data is None or index < 0 or index >= len(data):
            return False
        
        data[index] = record
        return self.save_data(data)
    
    def delete_record(self, index: int) -> bool:
        """Remove registro pelo índice."""
        data = self.load_data()
        if data is None or index < 0 or index >= len(data):
            return False
        
        data.pop(index)
        return self.save_data(data)