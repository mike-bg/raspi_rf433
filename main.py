import RPi.GPIO as GPIO
import time

# Configura el pin GPIO donde está conectado el receptor
RF_PIN = 17  # Cambia este número al pin GPIO que estás usando

# Configura el GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RF_PIN, GPIO.IN)


def read_rf_signal():
    print("Esperando señal RF...")
    while True:
        # Lee el estado del pin GPIO
        if GPIO.input(RF_PIN) == GPIO.HIGH:
            print("Señal alta detectada")
        else:
            print("Señal baja detectada")

        # Espera un poco para evitar lecturas demasiado rápidas
        time.sleep(0.1)


if __name__ == "__main__":
    try:
        read_rf_signal()
    except KeyboardInterrupt:
        print("Finalizando...")
    finally:
        GPIO.cleanup()
