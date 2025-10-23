"""
Funções auxiliares diversas.
"""

from datetime import datetime
from typing import Dict, Any


def format_currency(value: float) -> str:
    """Formata valor como moeda brasileira."""
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def format_date_display(date_str: str) -> str:
    """Formata data para exibição."""
    try:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        return date_obj.strftime("%d/%m/%Y")
    except:
        return date_str


def get_current_date() -> str:
    """Retorna data atual no formato DD/MM/YYYY."""
    return datetime.now().strftime("%d/%m/%Y")


def sanitize_record(record: Dict[str, Any]) -> Dict[str, Any]:
    """Remove espaços em branco desnecessários dos campos."""
    sanitized = {}
    for key, value in record.items():
        if isinstance(value, str):
            sanitized[key] = value.strip()
        else:
            sanitized[key] = value
    return sanitized
