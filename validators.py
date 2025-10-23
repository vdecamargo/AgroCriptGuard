"""
Módulo de validação de dados agrícolas.
Implementa regras de validação para garantir integridade dos dados.
"""

from datetime import datetime
from typing import Dict, Any, Optional


class ValidationError(Exception):
    """Exceção para erros de validação."""
    pass


class DataValidator:
    """Valida dados de entrada agrícolas."""
    
    @staticmethod
    def validate_not_empty(value: str, field_name: str) -> None:
        """
        Valida que campo não está vazio.
        
        Raises:
            ValidationError: Se campo estiver vazio
        """
        if not value or value.strip() == "":
            raise ValidationError(f"Campo '{field_name}' não pode estar vazio")
    
    @staticmethod
    def validate_positive_number(value: float, field_name: str) -> None:
        """
        Valida que número é positivo.
        
        Raises:
            ValidationError: Se número for negativo
        """
        if value < 0:
            raise ValidationError(f"Campo '{field_name}' não pode ser negativo")
    
    @staticmethod
    def validate_date(date_str: str, field_name: str) -> None:
        """
        Valida formato de data (DD/MM/YYYY).
        
        Raises:
            ValidationError: Se data for inválida
        """
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            raise ValidationError(
                f"Campo '{field_name}' deve estar no formato DD/MM/YYYY"
            )
    
    @staticmethod
    def validate_record(record: Dict[str, Any]) -> None:
        """
        Valida registro completo de dados agrícolas.
        
        Args:
            record: Dicionário com dados do registro
            
        Raises:
            ValidationError: Se alguma validação falhar
        """
        # Valida campos obrigatórios
        DataValidator.validate_not_empty(record.get("categoria", ""), "Categoria")
        DataValidator.validate_not_empty(record.get("descricao", ""), "Descrição")
        
        # Valida data
        DataValidator.validate_date(record.get("data", ""), "Data")
        
        # Valida valor numérico
        try:
            valor = float(record.get("valor", 0))
            DataValidator.validate_positive_number(valor, "Valor")
        except (ValueError, TypeError):
            raise ValidationError("Campo 'Valor' deve ser um número válido")
        
        # Valida quantidade se fornecida
        if "quantidade" in record and record["quantidade"]:
            try:
                quantidade = float(record["quantidade"])
                DataValidator.validate_positive_number(quantidade, "Quantidade")
            except (ValueError, TypeError):
                raise ValidationError("Campo 'Quantidade' deve ser um número válido")