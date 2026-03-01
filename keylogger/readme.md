# 🛡️ Desafio Prático: Simulação de Keylogger

Este repositório contém o projeto prático desenvolvido como parte do **Bootcamp Riachuelo - Cibersegurança da DIO**. O objetivo deste laboratório é aplicar conceitos de segurança ofensiva e defensiva através da criação de um Keylogger simulado em Python, operando em um ambiente 100% controlado e educacional.

Como definido no material do curso, um Malware é "qualquer tipo de programa ou código que foi criado com uma intenção prejudicial". Dentro dessa categoria, focamos no desenvolvimento de um Spyware, especificamente um keylogger.

---

## 🎯 Objetivos do Projeto
* Desenvolver um script em Python capaz de interceptar e registrar entradas de teclado (*keystrokes*).
* Compreender a mecânica de captura de dados sensíveis e credenciais em tempo real.
* Documentar os artefatos gerados pelo script (arquivos de log) para aprimorar a capacidade de detecção de ameaças.
* Elaborar estratégias de mitigação e defesa de endpoints.

---

## 💻 Implementação do Keylogger Simulado

O script foi desenvolvido utilizando a biblioteca `pynput` para escutar passivamente os eventos do teclado. 

**Comportamento do Script:**
1. **Captura:** O *listener* roda em segundo plano, registrando cada tecla pressionada pelo usuário.
2. **Armazenamento:** As teclas são formatadas e salvas sequencialmente em um arquivo local chamado `log.txt`. 
3. **Evidências de Captura:** Durante os testes, o script demonstrou sucesso em capturar dados variados, desde conversas ("fofoca da empresa") até potenciais credenciais ("senha 123") e acessos a URLs sensíveis, como páginas de configuração de senhas de aplicativo de contas do Google.

---
**Aviso Legal:** *Os códigos aqui presentes foram desenvolvidos unicamente para fins de estudo e conscientização em segurança da informação. Não utilize estes scripts em ambientes de produção ou sem autorização.*
