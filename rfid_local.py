import MFRC522
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

tags_liberadas = {
    (197, 12, 12, 171, 110): 'rafael',
    (68, 138, 241, 197, 250): 'joao'
}

LeitorRFID = MFRC522.MFRC522()

def libera_porta():
    GPIO.output(7, 1)
    #print('Porta Aberta')
    time.sleep(3)
    #print('Porta Fechada')
    GPIO.output(7, 0)

print('Aproxime a TAG')
try:
    while True:
        # Verifica se existe TAG no leitor
        (status, TagType) = LeitorRFID.MFRC522_Request(LeitorRFID.PICC_REQIDL)

        # Leitura da TAG
        if status == LeitorRFID.MI_OK:
            print('TAG Detectada!')
            (status, uid) = LeitorRFID.MFRC522_Anticoll()
            uid=tuple(uid)

            if uid in tags_liberadas.keys():
                print(f'ID: {tags_liberadas[uid]} - Acesso Liberado!')
                libera_porta()

            else:
                print('ID: inválido - Acesso Negado!')
        time.sleep(.5)

except KeyboardInterrupt:
    GPIO.cleanup()