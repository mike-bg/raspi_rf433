import RPi.GPIO as GPIO
import piVirtualWire


# Configura el pin GPIO donde está conectado el receptor
RF_PIN = 17

# Inicializa PiVirtualWire
vw = piVirtualWire(tx_pin=None, rx_pin=RF_PIN, speed=2000)  # 2000 bps como en el Arduino

def receive_rf_signal():
    print("Esperando señal RF...")
    while True:
        msg = vw.get_message()  # Intenta recibir un mensaje
        if msg:
            print("Mensaje recibido:", msg.decode('utf-8'))  # Imprime el mensaje recibido

if __name__ == "__main__":
    try:
        receive_rf_signal()
    except KeyboardInterrupt:
        print("Finalizando...")
    finally:
        GPIO.cleanup()