
# InstInt ☂️🎠🌈🎵

Repositório para armazenar configurações, testes, e softwares relacionados com a instalação interativa InstInt.

## 1. Configurações Iniciais

Os seguintes passos são necessários em uma nova instalação do Raspberry OS.

### 1.1 Configurar Acesso Remoto por SSH e VNC

Logo após concluir uma nova instalação do o Raspberry Pi OS em um cartão MicroSD, é necessário seguir o [tutorial oficial de configuração de acesso remoto ao Raspberry Pi](https://www.raspberrypi.com/documentation/computers/remote-access.html). Esse acesso remoto facilita significativamente futuras configurações de software e o desenvolvimento de comportamentos para o InstInt.

### 1.2 Configurar a Saída de Som por HDMI para liberar o PWM

Para garantir a conexão com o projetor e direcionar o som exclusivamente para a saída HDMI (necessário para garantir a estabilidade do PWM e o controle preciso dos LEDs RGB Neopixel) é necessário configurar o arquivo `/boot/config.txt`:

```
sudo nano /boot/config.txt
```

As seguintes linhas devem ser adicionadas ou descomentadas no arquivo aberto com o comando anterior:

```
hdmi_force_hotplug=1
hdmi_force_edid_audio=1
```

### 1.3 Ativar e Configurar o SPI

Como alternativa ao PWM, os LEDs RGB Neopixel podem ser controlados por SPI sem a necessidade de executar o script com privilégios de administrador. Para isso, é necessário configurar os arquivos `/boot/config.txt` e `/boot/cmdline.txt`:

```
sudo nano /boot/config.txt
```

As seguintes linhas devem ser adicionadas ou descomentadas no arquivo aberto com o comando anterior:

```
dtparam=spi=on
enable_uart=1
core_freq=500
core_freq_min=500
```

```
sudo nano /boot/cmdline.txt
```

A seguinte linha deve ser adicionada no arquivo aberto com o comando anterior:


```
spidev.bufsiz=32768
```

Lembre-se de reiniciar o sistema operacional após realizar as alterações.

### 1.4 Instalar a Biblioteca Neopixel e Outras Dependências

Os seguintes comandos devem ser executados no terminal do Raspberry OS:

```
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel adafruit-circuitpython-led-animation pydub
```
```
sudo python3 -m pip install --force-reinstall adafruit-blinka
```

## 2. Execução do Script InstInt

O script aceita um parâmetro livre para ser utilizado no nome dos logs gerados. Se esse parâmetro for `prototipo`, a quantidade de LEDs será ajustada para 10 de acordo com o protótipo construído para testar o software:

Executar o script em modo normal:


```
python3 instint.py
```

Executar o script em modo normal com um nome específico para o log:


```
python3 instint.py nome_especifico_para_o_log
```

Executar o script em modo de prototipo (apenas 10 LEDs):


```
python3 instint.py prototipo
```

## Outros Links Úteis

* [Tutorial sobre Python no Raspberry Pi](https://www.raspberrypi.com/documentation/computers/os.html#python)
* [Tutorial sobre Multitasking com Python no Raspberry Pi](https://learn.adafruit.com/cooperative-multitasking-in-circuitpython-with-asyncio)
* [Tutorial sobre Neopixels no Raspberry Pi](https://learn.adafruit.com/neopixels-on-raspberry-pi)
* [Informações técnicas sobre GPIO no Raspberry Pi](https://www.raspberrypi.com/documentation/computers/os.html#gpio-and-the-40-pin-header)
* [Tutorial sobre Animações com Neopixels](https://learn.adafruit.com/circuitpython-led-animations/)