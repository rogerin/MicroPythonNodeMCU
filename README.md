# Configurações
- [Como baixar e configurar o driver do NodeMCU](#secao-0)
- [Tutorial de Configuração do NodeMCU com MicroPython](#secao-1)
- [Tutorial: Como instalar a extensão PyMark no Visual Studio Code](#secao-2)
- [Configurando OTA no ESP](#secao-3)
- [Preparando firmware para atualização](#secao-4)
  
# Sobre esse repositório/tutorial

Este tutorial oferece um guia abrangente para desenvolvedores e entusiastas da IoT interessados em trabalhar com o NodeMCU, uma plataforma popular baseada no ESP8266. Abrange desde a configuração inicial do driver e a programação com MicroPython até técnicas avançadas como atualizações Over-The-Air (OTA) e preparação de firmware. É ideal para quem deseja explorar o desenvolvimento de projetos de Internet das Coisas, com foco em habilidades práticas como instalação de extensões no Visual Studio Code para melhorar a produtividade, e configuração de OTA para atualizações de firmware sem fio. Através de passo a passo detalhados, os leitores aprenderão a instalar drivers, configurar o ambiente de desenvolvimento, programar o NodeMCU, e implementar atualizações OTA, tornando este tutorial valioso tanto para iniciantes quanto para usuários avançados interessados em aprofundar seus conhecimentos em IoT.


# Como baixar e configurar o driver do NodeMCU <a id="secao-0" name="secao-0"></a>

O NodeMCU é uma plataforma de desenvolvimento IoT baseada no ESP8266, amplamente utilizada para projetos de Internet das Coisas. Para programar e interagir com o NodeMCU em seu computador, você precisará instalar o driver correto para estabelecer uma conexão com a placa. Neste artigo, vamos guiá-lo passo a passo no processo de baixar e configurar o driver do NodeMCU em um sistema Windows.

## Passo 1: Verifique sua versão do Windows

Antes de começar, verifique se você está executando uma versão do Windows que requer um driver específico para o NodeMCU. Normalmente, os sistemas Windows 10 reconhecem automaticamente a placa e não exigem instalação de drivers adicionais. No entanto, se você estiver usando uma versão mais antiga do Windows, como o Windows 7, pode ser necessário instalar o driver manualmente.

## Passo 2: Acesse o site do fabricante

Vá até o site oficial do fabricante do NodeMCU ou do fabricante do chip ESP8266 para baixar o driver correto. Normalmente, você pode encontrar o driver na seção "Downloads" ou "Suporte" do site.

Aqui você pode achar os links dos drive: <a href="https://www.robocore.net/tutoriais/instalando-driver-do-nodemcu?gclid=CjwKCAjwq4imBhBQEiwA9Nx1BpUQT_64qYnKiBq6Y63KeAOdbJHWPzJkii_DEWZk364TbgJyFLHbDBoCzcMQAvD_BwE">Acessar tutorial</a>

## Passo 3: Baixe o driver

Procure a versão mais recente do driver compatível com o seu sistema operacional Windows e faça o download do arquivo executável (geralmente com extensão .exe).

## Passo 4: Instale o driver

Após o download, execute o arquivo .exe para iniciar o assistente de instalação do driver. Siga as instruções na tela para concluir a instalação.

## Passo 5: Conecte o NodeMCU ao computador

Agora que o driver está instalado, conecte o NodeMCU à porta USB do seu computador usando um cabo adequado.

## Passo 6: Verifique a conexão

Para garantir que o driver foi instalado corretamente e o NodeMCU está se comunicando com o computador, siga os passos abaixo:

1. Abra o Gerenciador de Dispositivos no Windows.
2. Procure a seção "Portas (COM e LPT)".
3. Você deve ver uma entrada relacionada ao NodeMCU ou ao chip ESP8266, geralmente indicada como "USB-SERIAL CH340 (COMx)", onde "x" é o número da porta COM atribuída.

Se você conseguir visualizar a entrada acima sem nenhum ícone de erro, isso significa que o NodeMCU está configurado corretamente e pronto para ser usado para seus projetos.

## Conclusão

Parabéns! Agora você baixou e configurou com sucesso o driver do NodeMCU em seu sistema Windows. Você está pronto para começar a desenvolver seus projetos de IoT com o NodeMCU.

Lembre-se de que, se você estiver usando um sistema operacional diferente, como macOS ou Linux, as etapas podem ser um pouco diferentes, mas geralmente não exigem drivers adicionais, pois esses sistemas já suportam o NodeMCU nativamente.


-----

# Tutorial de Configuração do NodeMCU com MicroPython <a id="secao-1" name="secao-1"></a>

Neste tutorial, vamos aprender como configurar o NodeMCU para trabalhar com MicroPython. O NodeMCU é uma placa de desenvolvimento que utiliza o microcontrolador ESP8266, e o MicroPython é uma implementação do Python para dispositivos embarcados. Com essa combinação, é possível desenvolver projetos de IoT (Internet of Things) de forma simples e rápida.

## Passo 1: Instalação do Firmware MicroPython no NodeMCU

1. Acesse o site oficial do MicroPython (https://micropython.org/download) e faça o download do firmware apropriado para o NodeMCU. Escolha a versão compatível com o modelo do seu NodeMCU.

2. Conecte o NodeMCU ao seu computador usando um cabo USB e verifique em qual porta COM ele está conectado. Você pode verificar isso no Gerenciador de Dispositivos (Windows) ou usando o comando `ls /dev/tty*` no terminal (Linux/Mac).

3. Utilizando o esptool.py, um utilitário para gravação de firmware no ESP8266, abra o terminal e execute o seguinte comando (substitua `COMx` pela porta COM identificada no passo anterior):
   ```
    esptool.py --chip esp32 --port COMx erase_flash
   ```

4. Agora, grave o firmware do MicroPython no NodeMCU usando o comando (substitua `firmware.bin` pelo caminho completo do arquivo do firmware que você baixou):
   ```
   esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 firmware.bin
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

-------

# Tutorial: Como instalar a extensão PyMark no Visual Studio Code <a id="secao-2" name="secao-2"></a>

O PyMark é uma extensão para o Visual Studio Code que permite a visualização e edição de documentos escritos em Markdown, ao mesmo tempo que fornece recursos adicionais específicos para documentos que contenham código em Python. Neste tutorial, explicaremos como instalar essa extensão no Visual Studio Code.

## Passo 1: Abrir o Visual Studio Code

Se você ainda não tem o Visual Studio Code instalado, faça o download e instale-o em seu sistema operacional a partir do site oficial (https://code.visualstudio.com/).

## Passo 2: Abrir a guia de extensões

No Visual Studio Code, abra a guia de extensões clicando no ícone da extensão localizado na barra lateral esquerda ou use o atalho `Ctrl+Shift+X` (Windows/Linux) ou `Cmd+Shift+X` (Mac).

## Passo 3: Pesquisar a extensão PyMark

Na caixa de pesquisa da guia de extensões, digite "PyMark" e pressione `Enter`. Isso filtrará as extensões disponíveis e mostrará a extensão PyMark na lista de resultados.

## Passo 4: Instalar a extensão

Clique no botão "Instalar" ao lado da extensão PyMark para iniciar o processo de instalação. Espere até que a instalação seja concluída. Uma vez instalada, o botão "Instalar" mudará para "Recarregar". Clique em "Recarregar" para ativar a extensão.

## Passo 5: Configurações adicionais (opcional)

Após a instalação, você pode ajustar algumas configurações da extensão PyMark, se necessário. Para acessar as configurações, clique no ícone de engrenagem no canto inferior direito da guia de extensões e selecione "Configurações". Na barra de pesquisa, digite "pymark" para encontrar as opções específicas da extensão. Ajuste as configurações conforme suas preferências.

## Passo 6: Começar a usar o PyMark

Agora que a extensão PyMark está instalada, você pode criar ou abrir um arquivo Markdown com código Python no Visual Studio Code. A extensão PyMark fornecerá recursos extras para facilitar a edição e visualização desses arquivos, como realce de sintaxe aprimorado, suporte para visualização de resultados de código inline e outros recursos específicos do PyMark.

Parabéns! Você instalou com sucesso a extensão PyMark no Visual Studio Code e está pronto para aproveitar seus recursos aprimorados ao trabalhar com documentos Markdown que contenham código Python.

-------

# Configurando OTA no ESP <a id="secao-3" name="secao-3"></a>

Para configurar o Over-The-Air (OTA) no ESP32 com MicroPython para enviar atualizações via Wi-Fi, você pode seguir os passos a seguir. Certifique-se de ter o MicroPython instalado no seu ESP32 e uma rede Wi-Fi configurada antes de prosseguir.

1. **Instale o Firmware do ESP32 com suporte a OTA**: Certifique-se de que o firmware do seu ESP32 suporta OTA. Você pode verificar isso ao compilar o firmware do MicroPython com suporte a OTA ou procurar uma versão pré-compiled com suporte a OTA. O suporte a OTA geralmente é ativado por padrão nas compilações recentes.

2. **Conecte-se à Rede Wi-Fi**:

   ```python
   import network

   ssid = "SUA_REDE_WIFI"
   password = "SUA_SENHA_WIFI"

   wlan = network.WLAN(network.STA_IF)
   wlan.active(True)
   wlan.connect(ssid, password)

   while not wlan.isconnected():
       pass

   print("Conectado à rede Wi-Fi")
   ```

3. **Defina o Nome do Host**:

   Defina um nome de host para o seu ESP32. Isso é útil para identificar o dispositivo na rede. Você pode fazer isso com o seguinte código:

   ```python
   import machine

   hostname = "nome-do-seu-esp32"
   machine.hostname(hostname)
   ```

4. **Configurar o OTA no ESP32**:

   Você precisará importar o módulo `ota_updater` no seu código e configurá-lo com as informações corretas do servidor OTA.

   ```python
   from ota_updater import OTAUpdater

   ota_host = "http://seu-servidor-ota.com/atualizacoes"
   ota_username = "seu-usuario"
   ota_password = "sua-senha"

   ota_updater = OTAUpdater(ota_host, ota_username, ota_password)
   ```

5. **Verifique e Instale Atualizações**:

   Você pode verificar e instalar atualizações chamando as funções apropriadas do `OTAUpdater`. Aqui está um exemplo básico de como verificar atualizações:

   ```python
   if ota_updater.check_for_update():
       ota_updater.download_and_install_update()
   ```

6. **Inicialize o Código Principal do Seu Projeto**:

   Após a verificação e/ou instalação das atualizações, você pode inicializar o código principal do seu projeto.

7. **Loop de Verificação de Atualizações**:

   Coloque o código para verificar atualizações em um loop para verificar periodicamente as atualizações disponíveis. Você pode usar temporizadores para isso:

   ```python
   import time

   while True:
       if ota_updater.check_for_update():
           ota_updater.download_and_install_update()
       # Seu código principal aqui
       time.sleep(3600)  # Verifica atualizações a cada 1 hora (ajuste conforme necessário)
   ```

8. **Implemente o Servidor OTA**:

   Certifique-se de ter um servidor OTA configurado para fornecer as atualizações. O servidor OTA deve conter os binários das versões do firmware e disponibilizá-los para download conforme solicitado pelo ESP32.

Lembre-se de que a segurança é uma consideração importante ao implementar o OTA. Certifique-se de proteger a comunicação entre o ESP32 e o servidor OTA e de autenticar o dispositivo de forma adequada para evitar atualizações não autorizadas.

Este é um exemplo básico de como configurar o OTA em um ESP32 com MicroPython. Você pode adaptar e estender este código de acordo com as necessidades específicas do seu projeto e implementação do servidor OTA. Certifique-se de consultar a documentação e as práticas recomendadas do MicroPython para obter informações mais detalhadas.


--------
# Preparando firmware para atualização <a id="secao-4" name="secao-4"></a>

Para implementar um código de atualização OTA (Over-The-Air) simples que realiza apenas um blink no ESP32, você pode criar um arquivo binário que contém esse código e disponibilizá-lo em seu servidor OTA. Aqui estão os passos para criar um arquivo de firmware binário para um blink e fornecê-lo em seu servidor OTA:

1. **Crie o código de blink**:

   Crie um código de blink simples em um arquivo Python que pisque um LED no seu ESP32. Por exemplo:

   ```python
   import machine
   import time

   led = machine.Pin(2, machine.Pin.OUT)

   while True:
       led.value(not led.value())
       time.sleep(1)
   ```

   Salve esse código em um arquivo chamado `main.py`.

2. **Compile o código em um arquivo binário**:

   Você pode usar o utilitário `esptool.py` para compilar o código em um arquivo binário que pode ser atualizado via OTA. Use o seguinte comando para criar o arquivo binário:

   ```
   esptool.py --chip esp32 elf2image --flash_mode dio --flash_freq 40m --flash_size 4MB -o firmware.bin main.py
   ```

   Certifique-se de ajustar as opções conforme necessário, dependendo da configuração do seu ESP32.

3. **Crie um servidor OTA simples**:

   Você pode criar um servidor OTA simples usando uma biblioteca Python, como Flask, para fornecer o arquivo binário. Aqui está um exemplo mínimo usando Flask:

   ```python
   from flask import Flask, send_file

   app = Flask(__name__)

   @app.route('/atualizacoes')
   def firmware_update():
       return send_file('firmware.bin', as_attachment=True)

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=80)
   ```

   Certifique-se de que o arquivo `firmware.bin` esteja na mesma pasta que este código do servidor OTA.

4. **Execute o servidor OTA**:

   Execute o servidor OTA usando o comando `python`:

   ```
   python seu_servidor_ota.py
   ```

5. **Configure o ESP32 para verificar atualizações e atualizar via OTA**:

   Use o código que mencionei anteriormente para verificar atualizações e atualizar via OTA. Certifique-se de que o ESP32 possa acessar o servidor OTA no endereço `http://seu-servidor-ota.com/atualizacoes`.

Depois de seguir esses passos, o ESP32 verificará periodicamente as atualizações disponíveis em seu servidor OTA e, quando uma atualização estiver disponível, irá baixá-la e atualizar seu firmware. Certifique-se de que o servidor OTA esteja configurado para fornecer o arquivo `firmware.bin` que você criou e que o ESP32 tenha acesso à rede para realizar as atualizações.


-----

# Verificando versão 

Para implementar uma verificação de versão antes de atualizar o firmware via OTA (Over-The-Air), você precisa manter um número de versão em seu código e no servidor OTA. Aqui estão os passos para fazer isso:

**No ESP32 (Cliente)**:

1. **Defina uma versão no código**: Adicione uma variável global que represente a versão do firmware no seu código ESP32. Por exemplo:

   ```python
   firmware_version = "1.0"
   ```

2. **Recupere a versão do servidor OTA**: Quando o ESP32 verifica as atualizações, faça uma solicitação HTTP para o servidor OTA para obter a versão mais recente disponível. Você pode fazer isso usando uma API REST simples no servidor OTA que retorne a versão atual.

   ```python
   import urequests

   def get_latest_version():
       try:
           response = urequests.get("http://seu-servidor-ota.com/versao")
           if response.status_code == 200:
               return response.text
           else:
               return None
       except Exception as e:
           print("Erro ao obter a versão:", e)
           return None
   ```

3. **Compare as versões e atualize se necessário**: Após obter a versão mais recente do servidor OTA, compare-a com a versão atual no ESP32 e decida se deve atualizar ou não.

   ```python
   latest_version = get_latest_version()

   if latest_version and latest_version != firmware_version:
       print("Nova versão disponível. Atualizando...")
       # Chame a função de atualização OTA aqui
   else:
       print("O firmware está atualizado.")
   ```

**No Servidor OTA**:

1. **Forneça a versão mais recente**: Crie uma rota no seu servidor OTA para fornecer a versão mais recente do firmware quando solicitada.

   ```python
   from flask import Flask

   app = Flask(__name__)

   latest_version = "1.0"  # Atualize para a versão mais recente disponível

   @app.route('/versao')
   def get_latest_firmware_version():
       return latest_version

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=80)
   ```

Dessa forma, o ESP32 verificará a versão atual no servidor OTA antes de decidir se deve ou não iniciar a atualização OTA. Se a versão do servidor OTA for diferente da versão atual do ESP32, a atualização será iniciada.

Lembre-se de manter a versão atualizada em ambos os lados, no ESP32 e no servidor OTA, sempre que você criar uma nova versão do firmware.
