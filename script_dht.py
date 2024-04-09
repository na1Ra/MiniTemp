# script_dht.py
import dht
import machine
import time

def main():
    def read_dht_sensor(pin):
        # DHT-Sensor initialisieren
        dht_sensor = dht.DHT11(machine.Pin(pin))

        # Dateiname für die HTML-Datei
        html_filename = 'output.html'

        # Liste für die Speicherung der letzten 2 Einträge
        data = []

        while True:
            try:
                # Temperatur und Luftfeuchtigkeit auslesen
                dht_sensor.measure()
                temperature_c = dht_sensor.temperature()
                humidity = dht_sensor.humidity()

                # Werte zur Liste hinzufügen
                data.append((temperature_c, humidity))

                # Wenn mehr als 2 Einträge in der Liste sind, den ältesten Eintrag entfernen
                if len(data) > 2:
                    data.pop(0)

                # HTML-Datei öffnen und die Daten schreiben
                with open(html_filename, 'w') as f:
                    f.write('<html><head><meta charset="utf-8"></head><body style="background-color:black;">')
                    for temp, hum in data:
                        f.write('<div style="background-color:gray; width:100%; height:20%; position:relative;">')
                        f.write(f'<div style="background-color:red; width:{temp}%; height:100%;"></div>')
                        f.write(f'<span style="position:absolute; left:5px; color:white; font-family: URW Gothic Book ;">{temp}°C</span>')
                        f.write('</div>')
                        f.write('<div style="background-color:gray; width:100%; height:20%; position:relative;">')
                        f.write(f'<div style="background-color:blue; width:{hum}%; height:100%;"></div>')
                        f.write(f'<span style="position:absolute; left:5px; color:white; font-family: URW Gothic Book ;">{hum}%</span>')
                        f.write('</div>')
                    f.write('</body></html>')

            except OSError as e:
                # Fehlermeldung ausgeben
                print(f"Fehler beim Auslesen des Sensors: {e}")

            # Wartezeit erhöhen
            time.sleep(5)

    # Beispielaufruf der Funktion
    read_dht_sensor(14)  # Hier musst du den Pin angeben, an den der DHT11-Sensor angeschlossen ist

if __name__ == "__main__":
    main()

