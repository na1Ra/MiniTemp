import network
import usocket as socket
import time
import ujson as json

# Funktion zum Laden der WLAN-Daten aus einer JSON-Datei
def load_wifi_credentials():
    try:
        with open('wlan_config.json', 'r') as f:
            credentials = json.load(f)
            return credentials.get('ssid'), credentials.get('password')
    except OSError:
        print("Fehler beim Laden der WLAN-Daten aus der JSON-Datei")
        return None, None

# Verbinde den Pico mit dem Netzwerk
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

ssid, password = load_wifi_credentials()

if ssid and password:
    wifi.connect(ssid, password)
else:
    print("WLAN-Daten nicht verfügbar.")

# Warte auf die Verbindung zum WLAN
while not wifi.isconnected():
    time.sleep(1)

# Handler für HTTP-Anfragen definieren
def handle_request(client):
    request = client.recv(1024)
    print(request)
    
    # Analyse der angeforderten URL
    request_str = str(request)
    url = request_str.split(' ')[1][1:]
    
    # Lese die entsprechende HTML-Datei und sende sie als Antwort
    try:
        with open(url, 'r') as f:
            response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n" + f.read()
            client.send(response)
    except OSError:
        # Falls die Datei nicht gefunden wird, sende eine 404 Fehlermeldung
        client.send("HTTP/1.1 404 Not Found\n\n404 Not Found")
    
    client.close()

# Erstelle einen Socket und binde ihn an den Port 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

print("Server läuft")

# Akzeptiere eingehende Verbindungen und bearbeite Anfragen
while True:
    client, addr = s.accept()
    print('Verbunden mit', addr)
    handle_request(client)
