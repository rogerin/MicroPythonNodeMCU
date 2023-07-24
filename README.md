# Tutorial de Configuração do NodeMCU com MicroPython

Neste tutorial, vamos aprender como configurar o NodeMCU para trabalhar com MicroPython. O NodeMCU é uma placa de desenvolvimento que utiliza o microcontrolador ESP8266, e o MicroPython é uma implementação do Python para dispositivos embarcados. Com essa combinação, é possível desenvolver projetos de IoT (Internet of Things) de forma simples e rápida.

## Passo 1: Instalação do Firmware MicroPython no NodeMCU

1. Acesse o site oficial do MicroPython (https://micropython.org/download) e faça o download do firmware apropriado para o NodeMCU. Escolha a versão compatível com o modelo do seu NodeMCU.

2. Conecte o NodeMCU ao seu computador usando um cabo USB e verifique em qual porta COM ele está conectado. Você pode verificar isso no Gerenciador de Dispositivos (Windows) ou usando o comando `ls /dev/tty*` no terminal (Linux/Mac).

3. Utilizando o esptool.py, um utilitário para gravação de firmware no ESP8266, abra o terminal e execute o seguinte comando (substitua `COMx` pela porta COM identificada no passo anterior):
   ```
   esptool.py --port COMx erase_flash
   ```

4. Agora, grave o firmware do MicroPython no NodeMCU usando o comando (substitua `firmware.bin` pelo caminho completo do arquivo do firmware que você baixou):
   ```
   esptool.py --port COMx --baud 115200 write_flash --flash_size=detect 0 firmware.bin
   ```

5. O firmware do MicroPython deve estar instalado no NodeMCU agora.

## Passo 2: Acesso ao REPL (Read-Eval-Print Loop)

1. Desconecte o NodeMCU do computador e, em seguida, reconecte-o via USB.

2. Abra um terminal ou prompt de comando e acesse a porta serial do NodeMCU com o seguinte comando (substitua `COMx` pela porta COM correta):
   ```
   screen COMx 115200
   ```

3. Aguarde alguns segundos até que a conexão seja estabelecida. Agora você deve estar interagindo com o REPL do MicroPython no NodeMCU.

## Passo 3: Upload de Código Python para o NodeMCU

1. Escreva ou abra o código Python que você deseja executar no NodeMCU usando um editor de texto.

2. Salve o arquivo com a extensão `.py` no seu computador.

3. Agora, utilizaremos o ampy, uma ferramenta para enviar arquivos para o NodeMCU. No terminal, instale o ampy com o seguinte comando:
   ```
   pip install adafruit-ampy
   ```

4. Em seguida, faça o upload do arquivo Python para o NodeMCU (substitua `main.py` pelo nome do seu arquivo):
   ```
   ampy --port COMx put main.py
   ```

5. O código Python foi enviado para o NodeMCU. Caso você tenha um código chamado `main.py`, ele será executado automaticamente ao reiniciar o NodeMCU.

## Conclusão

Parabéns! Agora você configurou com sucesso o seu NodeMCU para trabalhar com MicroPython. Você pode criar projetos interessantes de IoT e aproveitar toda a facilidade e poder do Python em dispositivos embarcados. Explore a documentação do MicroPython para conhecer as bibliotecas disponíveis e divirta-se desenvolvendo!
