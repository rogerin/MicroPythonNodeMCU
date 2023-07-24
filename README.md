# Configurações
- [Tutorial de Configuração do NodeMCU com MicroPython](#secao-1)
- [Tutorial: Como instalar a extensão PyMark no Visual Studio Code](#secao-2)


# Tutorial de Configuração do NodeMCU com MicroPython <a id="secao-1" name="secao-1"></a>

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
