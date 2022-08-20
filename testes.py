###############################################################################
#                                                                             #
# Sequência de testes individuais de todas as funcionalidades do InstInt      #
#                                                                             #
###############################################################################

import time
import board
import neopixel
from adafruit_led_animation.animation.rainbow import Rainbow
from gpiozero import Button, MotionSensor, Motor
import pyttsx3

###############################################################################
#                                                                             #
# SETUP                                                                       #
#                                                                             #
###############################################################################

# Text-to-Speech (TTS)
tts = pyttsx3.init()
tts.setProperty("voice", "brazil")
tts.setProperty("rate", 120)


def comunicar(mensagem):
    print(mensagem)
    comunicar(mensagem)
    tts.runAndWait()

# Neopixels
pixels_count = 510
pixels = neopixel.NeoPixel(
    board.D12,
    pixels_count,
    auto_write=True,
    pixel_order=neopixel.GRB
)

# Toque
# toque_fita_1 = Button(10)
# toque_fita_2 = Button(9)
# toque_fita_3 = Button(11)
# toque_fita_4 = Button(0)
# toque_fita_5 = Button(5)

# Mais prático, testar
toque_fita = []
toque_fita[1] = Button(10)
toque_fita[2] = Button(9)
toque_fita[3] = Button(11)
toque_fita[4] = Button(0)
toque_fita[5] = Button(5)

# Presença
presenca_ir_1 = MotionSensor(8)
presenca_ir_2 = MotionSensor(7)
presenca_ir_3 = MotionSensor(1)
presenca_microondas = MotionSensor(23)  # TO-DO: testar compatibilidade

# Movimento
motor_abre_fecha = Motor(27, 22)
fim_abertura = Button(14)
fim_fechamento = Button(15)
motor_rotacao = Motor(13, 19)

#TO-DO: Bússola

###############################################################################
#                                                                             #
# TESTES: LEDs RGB                                                            #
#                                                                             #
###############################################################################


def testar_leds():
    comunicar("Todos os LEDs Vermelhos")
    pixels.fill((255, 0, 0))
    time.sleep(5)
    comunicar("Todos os LEDs Verdes")
    pixels.fill((0, 255, 0))
    time.sleep(5)
    comunicar("Todos os LEDs Azuis")
    pixels.fill((0, 0, 255))
    time.sleep(5)
    comunicar("Todos os LEDs Apagados")
    pixels.fill((0, 0, 0))
    time.sleep(5)
    comunicar("Todos os LEDs Brancos, preenchidos um a um")
    for i in range(pixels_count):
        pixels[i] = (255, 255, 255)
        time.sleep(0.01)
    time.sleep(5)
    pixels.fill((0, 0, 0))
    comunicar("Animação de Arco-Íris")
    rainbow = Rainbow(pixels, speed=0.1, period=5)
    rainbow.animate()

###############################################################################
#                                                                             #
# TESTES: Toque nas Fitas                                                     #
#                                                                             #
###############################################################################


def testar_toque(fita):
    primeiro_led_fita = (fita - 1) * 90
    ultimo_led_fita = primeiro_led_fita + 89
    comunicar("Toque na Fita " + str(fita))
    toque_fita[fita].wait_for_press()
    pixels[primeiro_led_fita:ultimo_led_fita] = (255, 255, 255) * 90
    toque_fita[fita].wait_for_release()
    pixels[primeiro_led_fita:ultimo_led_fita] = (0, 0, 0) * 90
    comunicar("Toque novamente na Fita " + str(fita))
    toque_fita[fita].wait_for_press()
    pixels[primeiro_led_fita:ultimo_led_fita] = (255, 255, 255) * 90
    toque_fita[fita].wait_for_release()
    pixels.fill((0, 0, 0))

###############################################################################
#                                                                             #
# TESTES: Presença                                                            #
#                                                                             #
###############################################################################


def testar_presenca():
    comunicar("Movimento no PIR 1")
    presenca_ir_1.wait_for_motion()
    pixels.fill((255, 255, 255))
    comunicar("Ausência de Movimento no PIR 1")
    presenca_ir_1.wait_for_no_motion()
    pixels.fill((0, 0, 0))
    #TO-DO: Repetir para presenca_ir_2-3 e microondas

###############################################################################
#                                                                             #
# TESTES: Abertura e Fechamento                                               #
#                                                                             #
###############################################################################


def testar_abertura_e_fechamento():
    comunicar("Abrir Estrutura")
    motor_abre_fecha.forward(speed=1)
    fim_abertura.wait_for_press()
    motor_abre_fecha.stop()
    comunicar("Fechar Estrutura")
    motor_abre_fecha.backward(speed=0.5)
    fim_fechamento.wait_for_press()
    motor_abre_fecha.stop()

###############################################################################
#                                                                             #
# TESTES: Rotação                                                             #
#                                                                             #
###############################################################################


def testar_rotacao():
    comunicar("Rotacionar Estrutura para a Direita")
    motor_rotacao.forward(speed=0.5)
    time.sleep(5)
    motor_rotacao.stop()
    comunicar("Rotacionar Estrutura para a Esquerda")
    motor_rotacao.backward(speed=0.5)
    time.sleep(5)
    motor_rotacao.stop()
    # TO-DO: Utilizar a bússola para controlar a parada

###############################################################################
#                                                                             #
# Executar Testes                                                             #
#                                                                             #
###############################################################################

comunicar("Inicializando Testes")

testar_leds()
testar_toque()
testar_presenca()
testar_abertura_e_fechamento()
testar_rotacao()
