# 🛡️ Desafio Prático: Simulação de Malware e Reflexão sobre Defesas

Este repositório contém os scripts e a documentação do projeto prático do **Bootcamp Riachuelo - Cibersegurança da DIO**. O objetivo deste laboratório foi compreender o funcionamento sob o capô de duas ameaças clássicas (Ransomware e Keylogger) utilizando Python em um ambiente estritamente educacional e controlado.

## 🎯 Objetivos de Aprendizagem
- Desenvolver provas de conceito (PoC) de criptografia de arquivos e captura de *keystrokes*.
- Compreender a mecânica de exfiltração de dados e sequestro de informações.
- Analisar os artefatos gerados por essas ameaças para aprimorar a capacidade de resposta a incidentes.

---

## 💻 Implementação dos Laboratórios

### 1. Ransomware Simulado (`ransomware.py`)
Utilizei a biblioteca `cryptography` (módulo Fernet) para demonstrar como a criptografia simétrica pode ser usada de forma maliciosa.
* **Comportamento:** O script localiza o arquivo alvo de teste (`senhas.txt`), lê o conteúdo em bytes, aplica a criptografia gerada por uma chave local e sobrescreve o arquivo original, deixando uma nota de resgate (`LEIA ISSO.txt`).

### 2. Keylogger Simulado (`keylogger.py`)
Através da biblioteca `pynput`, construí um *listener* que monitora e registra os eventos de hardware do teclado.
* **Comportamento:** O script roda em segundo plano capturando as teclas e salvando-as de forma sequencial no arquivo `log.txt` (incluindo backspaces, enters e caracteres alfanuméricos).

---

## 🛑 Reflexão sobre Defesa e Mitigação

Criar essas ferramentas deixou claro o quão perigosas elas são na vida real. Abaixo, detalho como ambientes corporativos podem se proteger contra os comportamentos que simulei nestes scripts:

### Detecção e Resposta (EDR / Antivírus)
[Soluções de segurança modernas não dependem mais apenas de assinaturas de arquivos conhecidos (hashes). Ferramentas de EDR (Endpoint Detection and Response) de mercado, como o SentinelOne ou Microsoft Defender, monitoram a telemetria contínua do sistema operacional em busca de comportamentos anômalos. Quando um script de Ransomware é executado, ele gera um padrão de execução altamente suspeito: um processo não padrão (como o interpretador Python) começa a abrir dezenas de arquivos em frações de segundo, injeta dados de alta entropia (característica inerente a dados criptografados) e pode tentar alterar extensões em massa. Esse pico rápido de operações de I/O (leitura e gravação) em disco dispara alertas heurísticos críticos. Em um ambiente bem configurado, o EDR age matando (kill) o processo malicioso e isolando o host da rede corporativa automaticamente, contendo a ameaça antes que o dano se espalhe]

### Controles de Rede e Firewall
[Descreva como bloquear a exfiltração do Keylogger. Se o script tenta enviar o arquivo `log.txt` por e-mail usando a porta 587 (SMTP), como uma regra de firewall bloqueando saídas SMTP não autorizadas para a internet impediria o atacante de receber os dados?]

### Sandboxing e Controle de Privilégios
[Comente sobre o Princípio do Menor Privilégio. Se o usuário que executou o Ransomware não tiver permissões de escrita em pastas de rede (File Servers) ou pastas de sistema do Windows, o alcance do ataque é drasticamente reduzido.]

---
**Aviso Legal:** *Os códigos aqui presentes foram desenvolvidos unicamente para fins de estudo e conscientização em segurança da informação. Não utilize estes scripts em ambientes de produção ou sem autorização.*
