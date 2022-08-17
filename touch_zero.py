from gpiozero import Button

touch1 = Button(10)
touch2 = Button(9)
touch3 = Button(11)
touch4 = Button(0)
touch5 = Button(5)

touch1.when_pressed = print("Sensor 1 tocado")
touch1.when_released = print("Sensor 1 solto")

touch2.when_pressed = print("Sensor 1 tocado")
touch2.when_released = print("Sensor 1 solto")

touch3.when_pressed = print("Sensor 1 tocado")
touch3.when_released = print("Sensor 1 solto")

touch4.when_pressed = print("Sensor 1 tocado")
touch4.when_released = print("Sensor 1 solto")

touch5.when_pressed = print("Sensor 1 tocado")
touch5.when_released = print("Sensor 1 solto")