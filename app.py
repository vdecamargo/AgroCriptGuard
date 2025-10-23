
"""
Interface principal do AgroCryptGuard usando Streamlit.
Aplicação para gestão segura e criptografada de dados agrícolas.
"""

import streamlit as st
from typing import Optional

from auth import AuthManager
from crypto import CryptoManager
from storage import StorageManager
from validators import DataValidator, ValidationError
from utils import format_currency, format_date_display, get_current_date, sanitize_record
from config import DATA_CATEGORIES


# Configuração da página
st.set_page_config(
    page_title="AgroCryptGuard",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)


def initialize_session_state():
    """Inicializa variáveis de sessão."""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'crypto_manager' not in st.session_state:
        st.session_state.crypto_manager = None
    if 'storage_manager' not in st.session_state:
        st.session_state.storage_manager = None


def show_header():
    """Exibe cabeçalho da aplicação."""
    st.title("🔒 AgroCryptGuard")
    st.markdown("*Gestão segura e criptografada de dados agrícolas*")
    st.divider()


def show_registration_page(auth_manager: AuthManager):
    """Página de cadastro de senha mestra."""
    st.header("Cadastro de Senha Mestra")
    st.info("Configure sua senha mestra para proteger seus dados agrícolas.")
    
    with st.form("registration_form"):
        password = st.text_input("Senha Mestra", type="password", 
                                help="Escolha uma senha forte")
        password_confirm = st.text_input("Confirmar Senha", type="password")
        
        submit = st.form_submit_button("Criar Conta", type="primary")
        
        if submit:
            # Validações
            if not password or not password_confirm:
                st.error("❌ Todos os campos são obrigatórios")
                return
            
            if password != password_confirm:
                st.error("❌ As senhas não coincidem")
                return
            
            if len(password) < 8:
                st.error("❌ A senha deve ter no mínimo 8 caracteres")
                return
            
            # Cria usuário
            if auth_manager.create_user(password):
                st.success("✅ Conta criada com sucesso! Faça login para continuar.")
                st.rerun()
            else:
                st.error("❌ Erro ao criar conta. Tente novamente.")


def show_login_page(auth_manager: AuthManager):
    """Página de login."""
    st.header("Login")
    st.info("Digite sua senha mestra para acessar seus dados.")
    
    with st.form("login_form"):
        password = st.text_input("Senha Mestra", type="password")
        
        submit = st.form_submit_button("Entrar", type="primary")
        
        if submit:
            if not password:
                st.error("❌ Digite sua senha")
                return
            
            # Verifica senha
            if auth_manager.verify_password(password):
                # Deriva chave criptográfica
                key = auth_manager.derive_key(password)
                
                if key:
                    # Armazena na sessão
                    st.session_state.crypto_manager = CryptoManager(key)
                    st.session_state.storage_manager = StorageManager(
                        st.session_state.crypto_manager
                    )
                    st.session_state.authenticated = True
                    st.success("✅ Login realizado com sucesso!")
                    st.rerun()
                else:
                    st.error("❌ Erro ao derivar chave de criptografia")
            else:
                st.error("❌ Senha incorreta")


def show_data_form(storage_manager: StorageManager):
    """Formulário para adicionar novo registro."""
    st.subheader("📝 Adicionar Novo Registro")
    
    with st.form("data_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            categoria = st.selectbox("Categoria", DATA_CATEGORIES)
            descricao = st.text_input("Descrição")
            data = st.text_input("Data (DD/MM/YYYY)", value=get_current_date())
        
        with col2:
            valor = st.number_input("Valor (R$)", min_value=0.0, step=0.01)
            quantidade = st.number_input("Quantidade", min_value=0.0, step=0.1)
            observacoes = st.text_area("Observações", height=100)
        
        submit = st.form_submit_button("Adicionar Registro", type="primary")
        
        if submit:
            try:
                # Cria registro
                record = {
                    "categoria": categoria,
                    "descricao": descricao,
                    "data": data,
                    "valor": valor,
                    "quantidade": quantidade,
                    "observacoes": observacoes
                }
                
                # Sanitiza e valida
                record = sanitize_record(record)
                DataValidator.validate_record(record)
                
                # Salva
                if storage_manager.add_record(record):
                    st.success("✅ Registro adicionado com sucesso!")
                    st.rerun()
                else:
                    st.error("❌ Erro ao salvar registro")
                    
            except ValidationError as e:
                st.error(f"❌ Erro de validação: {str(e)}")
            except Exception as e:
                st.error(f"❌ Erro inesperado: {str(e)}")


def show_data_list(storage_manager: StorageManager):
    """Exibe lista de registros."""
    st.subheader("📊 Registros Salvos")
    
    data = storage_manager.load_data()
    
    if data is None:
        st.error("❌ Erro ao carregar dados. Verifique sua senha ou integridade dos arquivos.")
        return
    
    if not data:
        st.info("Nenhum registro encontrado. Adicione seu primeiro registro acima.")
        return
    
    # Filtros
    col1, col2 = st.columns(2)
    with col1:
        filter_category = st.selectbox(
            "Filtrar por Categoria",
            ["Todas"] + DATA_CATEGORIES
        )
    
    # Aplica filtro
    filtered_data = data if filter_category == "Todas" else [
        r for r in data if r.get("categoria") == filter_category
    ]
    
    st.write(f"Total de registros: {len(filtered_data)}")
    
    # Exibe registros
    for idx, record in enumerate(filtered_data):
        with st.expander(
            f"{record.get('categoria')} - {record.get('descricao')} "
            f"({format_date_display(record.get('data', ''))})"
        ):
            col1, col2, col3 = st.columns([2, 2, 1])
            
            with col1:
                st.write(f"Valor: {format_currency(record.get('valor', 0))}")
                st.write(f"Quantidade: {record.get('quantidade', 'N/A')}")
            
            with col2:
                st.write(f"Data: {format_date_display(record.get('data', ''))}")
                st.write(f"Observações: {record.get('observacoes', 'N/A')}")
            
            with col3:
                # Botão de exclusão
                original_idx = data.index(record)
                if st.button("🗑 Excluir", key=f"del_{original_idx}"):
                    if storage_manager.delete_record(original_idx):
                        st.success("✅ Registro excluído!")
                        st.rerun()
                    else:
                        st.error("❌ Erro ao excluir")


def show_main_app(storage_manager: StorageManager):
    """Interface principal da aplicação."""
    show_header()
    
    # Sidebar
    with st.sidebar:
        st.header("Menu")
        st.divider()
        
        if st.button("🚪 Sair", type="secondary", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.crypto_manager = None
            st.session_state.storage_manager = None
            st.rerun()
        
        st.divider()
        st.caption("🔒 Seus dados estão protegidos com criptografia AES-GCM")
    
    # Conteúdo principal
    tab1, tab2 = st.tabs(["📝 Novo Registro", "📊 Visualizar Dados"])
    
    with tab1:
        show_data_form(storage_manager)
    
    with tab2:
        show_data_list(storage_manager)


def main():
    """Função principal."""
    initialize_session_state()
    
    auth_manager = AuthManager()
    
    # Fluxo de autenticação
    if not st.session_state.authenticated:
        show_header()
        
        # Verifica se precisa cadastrar
        if not auth_manager.user_exists():
            show_registration_page(auth_manager)
        else:
            show_login_page(auth_manager)
    else:
        # Usuário autenticado
        show_main_app(st.session_state.storage_manager)


if name == "main":
    main()