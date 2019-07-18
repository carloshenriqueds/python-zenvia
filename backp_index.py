import os
from totalvoice.cliente import Cliente

numero_destino = "SEU_TELEFONE_55119844444"
voiceMessage = os.environ['VOICE_TEXT']
token = os.environ['TOTALVOICE_TOKEN']
url = os.environ['API_URI']
smsMessage = os.environ['SMS_TEXT']

cliente = Cliente(token, url)
response = cliente.tts.enviar(numero_destino, voiceMessage)
print(response)

response = cliente.sms.enviar(numero_destino, smsMessage);
print(response)

