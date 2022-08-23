
# InstInt ☂️🎠🌈🎵

Repositório para armazenar configurações, testes, e softwares relacionados com a instalação interativa InstInt.

## 1. Configurações Iniciais

Os seguintes passos são necessários em uma nova instalação do Raspberry OS.

### 1.1 Configurar Acesso Remoto por SSH e VNC

Logo após concluir uma nova instalação do o Raspberry Pi OS em um cartão MicroSD, é necessário seguir o [tutorial oficial de configuração de acesso remoto ao Raspberry Pi](https://www.raspberrypi.com/documentation/computers/remote-access.html). Esse acesso remoto facilita significativamente futuras configurações de software e o desenvolvimento de comportamentos para o InstInt.

### 1.2 Configurar a Saída de Som por HDMI para liberar o PWM

Para garantir a conexão com o projetor e direcionar o som exclusivamente para a saída HDMI (necessário para garantir a estabilidade do PWM e o controle preciso dos LEDs RGB Neopixel) é necessário configurar o arquivo `config.txt`:

```
sudo nano /boot/config.txt
```

As seguintes linhas devem ser adicionadas ou descomentadas no arquivo aberto com o comando anterior:

```
hdmi_force_hotplug=1
hdmi_force_edid_audio=1
```

[Configuração adicional.](https://forums.raspberrypi.com/viewtopic.php?p=913285)

### 1.3 Instalar a Biblioteca Neopixel e Outras Dependências

Os seguintes comandos devem ser executados no terminal do Raspberry OS:

```
sudo apt-get install espeak
```
```
sudo pip3 install pyttsx3 rpi_ws281x adafruit-circuitpython-neopixel adafruit-circuitpython-led-animation
```
```
sudo python3 -m pip install --force-reinstall adafruit-blinka
```

## 2. Execução de Scripts

Os scripts em Python devem ser executados com privilégios de administrador (*root*) para que seja necessário utilizar a biblioteca Neopixel e controlar os LEDs RGB. Isso é possível por meio da execução direta de um script com o comando:

```
sudo python3 testes.py
```

Ou por meio da execução da IDE [Thonny](https://thonny.org/) com privilégios de administrador:

```
sudo thonny
```
## Outros Links Úteis

* [Tutorial sobre Python no Raspberry Pi](https://www.raspberrypi.com/documentation/computers/os.html#python)
* [Tutorial sobre Multitasking com Python no Raspberry Pi](https://learn.adafruit.com/cooperative-multitasking-in-circuitpython-with-asyncio)
* [Tutorial sobre Neopixels no Raspberry Pi](https://learn.adafruit.com/neopixels-on-raspberry-pi)
* [Informações técnicas sobre GPIO no Raspberry Pi](https://www.raspberrypi.com/documentation/computers/os.html#gpio-and-the-40-pin-header)
* [Tutorial sobre Animações com Neopixels](https://learn.adafruit.com/circuitpython-led-animations/)