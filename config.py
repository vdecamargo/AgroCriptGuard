"""
Configurações globais do AgroCryptGuard.
Define constantes para caminhos de arquivos e parâmetros de segurança.
"""

import os
from pathlib import Path

# Diretórios
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Arquivos
AUTH_FILE = BASE_DIR / "auth.json"
ENCRYPTED_DATA_FILE = DATA_DIR / "dados_agricolas.enc"

# Parâmetros Argon2 (ajuste conforme necessário)
ARGON2_TIME_COST = 2          # Número de iterações
ARGON2_MEMORY_COST = 65536    # Memória em KB (64 MB)
ARGON2_PARALLELISM = 2        # Threads paralelas
ARGON2_HASH_LEN = 32          # Tamanho da chave derivada (256 bits)
ARGON2_SALT_LEN = 16          # Tamanho do salt (128 bits)

# Parâmetros AES-GCM
AES_KEY_SIZE = 32             # 256 bits
NONCE_SIZE = 12               # 96 bits (recomendado para AES-GCM)

# Categorias de dados agrícolas
DATA_CATEGORIES = [
    "Custos",
    "Produção",
    "Insumos",
    "Colheita",
    "Clima",
    "Finanças"
]
