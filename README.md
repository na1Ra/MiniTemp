# MiniTemp
 Beispiel Codes für Temp/Feuchte auslesen und Website hosten auf einem Pico W

## DHT-11 Sensor Projekt v2

Wir hatten das Projekt einen DHT-11 Sensor an einen Raspberry Pi anzuschließen und eine Website zu hosten. Dazu wurde uns ein Raspberry Pi 400 und ein DHT-11 Sensor zur Verfügung gestellt worden. Das habe ich auch mit meinem Partner Marc Stoppelkamp erfolgreich ausführen können.

Nun hatte ich aber noch sehr viel Langweile bis zur Abgabe und fand dieses Projekt sehr großartig da es mir die Welt von Sensoren und Microcontroller gezeigt hat. Da bin ich auf die Idee gekommen eine Version 2 dieses Projekts zu machen, Günstiger und Kompakter aber trotzdem mit Python da es die Hauptsprache ist, die an der Schule gelernt wird und wie wir alle wissen steht das Pi in Raspberry PI für Python.

## Hardware
Für das DHT-11 Sensor Projekt Version 2 habe ich einen Raspberry Pi Pico W und den DHT-11 Sensor verwendet. Der Raspberry Pi Pico W ist eine kompakte Version des "richtigen" Raspberry Pi, auf dem jedoch kein vollständiges Betriebssystem läuft. Auf einem Pico können wir die "normale" Arduino-C-Sprache verwenden oder MicroPython bzw. CircuitPython. Wir haben uns für MicroPython entschieden, da dies die empfohlene Sprache von Raspberry ist.

## Software
Als integrierte Entwicklungsumgebung (IDE) empfehle ich Thonny, da dort die Unterstützung für MicroPython für Mikrocontroller integriert ist und wir direkt auf das Gerät zugreifen können. Alternativ dazu gibt es auch Erweiterungen für MicroPython in VS-Code. Nachdem Thonny erfolgreich heruntergeladen wurde, müssen wir die MicroPython-Datei (utf2) herunterladen. Sobald wir diese Datei gefunden haben, nehmen wir den Pico, halten die Boot-Taste gedrückt und schließen ihn an den Computer an. Der Pico sollte nun auf dem Computer auftauchen. Dort kopieren wir die MicroPython-Datei hinein. Nach diesem Vorgang sollte sich der Pico selbst neu starten und in Thonny erreichbar sein.

## Anschließen 
Der DHT-11 Sensor verfügt über drei Pins: einen +, einen - und einen S-Pin. Der + Pin wird an den 3V-Pin des Pico angeschlossen, den wir auf Pin 5 des Pico finden, wenn der USB-Anschluss nach oben zeigt. Der - Pin wird an Ground angeschlossen. Am Pico gibt es mehrere Ground-Pins; ich habe ihn an Pin 13 angeschlossen. Der letzte Pin, der mit dem Pico verbunden werden muss, ist der Signal-Pin. Ich habe ihn an GP14 angeschlossen, der sich auf der rechten Seite des vorletzten Pins befindet.

<img src='./Pico w fritzing.png' width=60%>
          
Nun sind wir bereit, den Pico zu programmieren, um die Daten des Sensors auszulesen und sie auf einer Webseite darzustellen.


Die Beispiel Codes zum Auslesen und Hosten der Website finden sie in diesem Git-Repo
