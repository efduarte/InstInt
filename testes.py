################################################################################
#                                                                              #
# Sequência de testes individuais de todas as funcionalidades do InstInt       #
#                                                                              #
################################################################################

import time
import board
import neopixel
from gpiozero import Button, MotionSensor, Motor
import pyttsx3

################################################################################
#                                                                              #
# SETUP                                                                        #
#                                                                              #
################################################################################

#Text-to-Speech (TTS)
tts = pyttsx3.init()
tts.setProperty("voice", "brazil")
tts.setProperty("rate", 120)
tts.say("Inicializando Testes")
tts.runAndWait()

#Neopixels
pixels_count = 510
pixels = neopixel.NeoPixel(
    board.D12,
    pixels_count,
    auto_write=True,
    pixel_order=neopixel.GRB
)

#Toque
toque_fita_1 = Button(10)
toque_fita_2 = Button(9)
toque_fita_3 = Button(11)
toque_fita_4 = Button(0)
toque_fita_5 = Button(5)

#Presença
presenca_ir_1 = MotionSensor(8)
presenca_ir_2 = MotionSensor(7)
presenca_ir_3 = MotionSensor(1)
presenca_microondas = MotionSensor(23) #TO-DO: testar compatibilidade

#Movimento
motor_abre_fecha = Motor(27, 22)
fim_abertura = Button(14)
fim_fechamento = Button(15)
motor_rotacao = Motor(13, 19)

#TO-DO: Bússola

################################################################################
#                                                                              #
# TESTES: LEDs RGB                                                             #
#                                                                              #
################################################################################

tts.say("Todos os LEDs Vermelhos")
tts.runAndWait()
pixels.fill((255, 0, 0))
time.sleep(5)

tts.say("Todos os LEDs Verdes")
tts.runAndWait()
pixels.fill((0, 255, 0))
time.sleep(5)

tts.say("Todos os LEDs Azuis")
tts.runAndWait()
pixels.fill((0, 0, 255))
time.sleep(5)

tts.say("Todos os LEDs Apagados")
tts.runAndWait()
pixels.fill((0, 0, 0))
time.sleep(5)

tts.say("Todos os LEDs Brancos, preenchidos um a um")
tts.runAndWait()
for i in range(pixels_count):
    pixels[i] = (255, 255, 255)
    time.sleep(0.01)
time.sleep(5)
pixels.fill((0, 0, 0))

tts.say("Animação de Arco-Íris")
tts.runAndWait()
rainbow = Rainbow(pixels, speed=0.1, period=5)
rainbow.animate()

################################################################################
#                                                                              #
# TESTES: Toque nas Fitas                                                      #
#                                                                              #
################################################################################

tts.say("Toque na Fita 1")
tts.runAndWait()
toque_fita_1.wait_for_press()
pixels[0:89] = (255, 255, 255) * 90
toque_fita_1.wait_for_release()
pixels[0:89] = (0, 0, 0) * 90

tts.say("Toque novamente na Fita 1")
tts.runAndWait()
toque_fita_1.wait_for_press()
pixels[0:89] = (255, 255, 255) * 90
toque_fita_1.wait_for_release()
pixels.fill((0, 0, 0))

#TO-DO: Repetir para fitas 2-5

################################################################################
#                                                                              #
# TESTES: Presença                                                             #
#                                                                              #
################################################################################

tts.say("Movimento no PIR 1")
tts.runAndWait()
presenca_ir_1.wait_for_motion()
pixels.fill((255, 255, 255))

tts.say("Ausência de Movimento no PIR 1")
tts.runAndWait()
presenca_ir_1.wait_for_no_motion()
pixels.fill((0, 0, 0))

#TO-DO: Repetir para presenca_ir_2-3 e microondas

################################################################################
#                                                                              #
# TESTES: Abertura e Fechamento                                                #
#                                                                              #
################################################################################

tts.say("Abrir Estrutura")
tts.runAndWait()
motor_abre_fecha.forward(speed=1)
fim_abertura.wait_for_press()
motor_abre_fecha.stop()

tts.say("Fechar Estrutura")
tts.runAndWait()
motor_abre_fecha.backward(speed=0.5)
fim_fechamento.wait_for_press()
motor_abre_fecha.stop()

################################################################################
#                                                                              #
# TESTES: Rotação                                                              #
#                                                                              #
################################################################################

tts.say("Rotacionar Estrutura para a Direita")
tts.runAndWait()
motor_rotacao.forward(speed=0.5)
time.sleep(5)
motor_rotacao.stop()

tts.say("Rotacionar Estrutura para a Esquerda")
tts.runAndWait()
motor_rotacao.backward(speed=0.5)
time.sleep(5)
motor_rotacao.stop()

#TO-DO: Utilizar a bússola para controlar a parada