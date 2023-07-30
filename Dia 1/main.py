from machine import Pin, ADC
from time import sleep
import network
import urequests
sensorLuz = ADC(Pin(36))

def ler_sensor():
    valor_analogico = sensorLuz.read()
    return valor_analogico

# print('START')
# while True:
#     val = pin.read()
#     print(val)
#     sleep(0.5)
    





# Defina o pino ADC do NodeMCU conectado ao sensor de umidade do solo
SENSOR_PIN = 0

# Intervalo de tempo para hibernação em segundos (aqui definimos 30 minutos)
# HIBERNATE_TIME = 1800
HIBERNATE_TIME = 1800

# Configuração da rede Wi-Fi
WIFI_SSID = 'Vivo-Internet-AF5C'
WIFI_PASSWORD = 'peterpan'

# URL da API ou serviço web para envio dos dados
API_URL = 'http://192.168.1.101:3000/iot2?luz='


# Função para ler o valor do sensor de umidade do solo
def read_soil_moisture():
    adc = machine.ADC(SENSOR_PIN)
    # Faça a leitura ADC e converta o valor para uma escala de 0 a 100 (0 = solo seco, 100 = solo molhado)
    value = adc.read()
    moisture_percent = (value / 1023) * 100
    return moisture_percent

# Função para conectar-se à rede Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando-se à rede Wi-Fi...')
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            pass
    print('Conectado à rede Wi-Fi:', WIFI_SSID)
    print('Endereço IP:', wlan.ifconfig()[0])

# Função para enviar os dados via requisição HTTP
def send_data(data):
    try:
        # response = urequests.post(API_URL, json=data)
        response = urequests.get(API_URL+str(data))
        print('Requisição enviada:', response.text)
    except Exception as e:
        print('Erro ao enviar a requisição:', e)

# Função para entrar no modo deep sleep
def enter_deep_sleep():
    print("Entrando no modo de hibernação 2...")
    # Desligue a alimentação dos sensores ou outros dispositivos externos, se necessário
    # Desligue a impressão para economizar energia
    # machine.freq(160000000)  # Reduza a frequência da CPU para economizar energia
    machine.deepsleep(HIBERNATE_TIME * 1000000)  # Converta segundos em microssegundos

# Função principal

try:
    # Conecte-se à rede Wi-Fi
    connect_wifi()
    
    while True:
        # Leia a umidade do solo
        # soil_moisture = read_soil_moisture()
        
        # Exiba os dados no console do MicroPython
        #print("Umidade do Solo: {:.2f}%".format(soil_moisture))
        
        # Enviar os dados via requisição HTTP
        # data = {'luminosidade': pin.read()}
        data = ler_sensor()
        print(data)
        send_data(data)

        # Aguarde alguns segundos antes de fazer uma nova leitura
        tempo_sono_ms = 500

        # Espera um evento no pino GPIO 2 ou aguarda o tempo especificado
        #machine.lightsleep(tempo_sono_ms)
        sleep(5)
        

except KeyboardInterrupt:
    print("Interrupção de teclado. Encerrando o programa.")




# from machine import Pin, ADC
# from time import sleep

# import network
# import urequests

# pot = ADC(0)

# WIFI_SSID = 'cariri'
# WIFI_PASSWORD = '0987654321'

# # Função para conectar-se ao Wi-Fi
# def connect_to_wifi(ssid, password):
#     station = network.WLAN(network.STA_IF)
#     station.active(True)
#     station.connect(ssid, password)
#     while not station.isconnected():
#         pass
#     print('Conectado ao Wi-Fi 2:', ssid)

# # Função para enviar uma solicitação GET e retornar a resposta
# def send_get_request(url):
#     response = urequests.get(url)
#     return response.text

# # Conecte-se ao Wi-Fi
# connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)

# try:
#     while True:
#         pot_value = pot.read()
#         print(pot_value)
#         URL = 'https://eo4o0rur87j0pcd.m.pipedream.net/?luminosity='+str(pot_value)
#         response_text = send_get_request(URL)
#         print('Resposta do servidor:')
#         print(response_text)

#         sleep(3)
    
# except Exception as e:
#     print('Erro ao enviar a solicitação GET:', e)


# # while True:
# #     led.on()
# #     time.sleep(0.5)
# #     led.off()
# #     time.sleep(0.5)nao