# InstInt

Repositório para armazenar configurações, testes, e softwares relacionados com a instalação interativa InstInt.

Os seguintes passos são necessários em uma nova instalação do Raspberry OS.

## Configurar de Som e PWM

Para garantir a conexão com o projetor e direcionar o som exclusivamente para a saída HDMI (necessário para garantir a estabilidade do PWM e o controle preciso dos LEDs RGB) é necessário configurar o arquivo `config.txt`:

`sudo nano /boot/config.txt`

As seguintes linhas devem ser adicionadas ou descomentadas:

```
hdmi_force_hotplug=1
hdmi_force_edid_audio=1
```

## Instalar Neopixel e Dependências

Os seguintes comandos devem ser executados no terminal do Raspberry OS:

```
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
```

## Executar Scripts

Lembre-se de executar os scripts com privilégios de administrador (root), isso é necessário para poder utilizar o GPIO.

## Links Úteis

* [Configurar acesso remoto ao Raspberry Pi](https://www.raspberrypi.com/documentation/computers/remote-access.html)
* [Breve tutorial sobre uso do Python no Raspbery Pi](https://www.raspberrypi.com/documentation/computers/os.html#python)
* [Informações técnicas sobre GPIO no Raspberry Pi](https://www.raspberrypi.com/documentation/computers/os.html#gpio-and-the-40-pin-header)