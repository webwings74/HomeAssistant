# HomeAssistant
Projecten met betrekking tot het gebruik van het **Home Assistant OS** (HAOS), overwegend op een **Raspberry Pi 5**.
O.a. voor het uitlezen van gegevens van een warmtepomp en daarna als doel het besturen ervan, met
als input allerlei omgevings sensoren en weersvoorspelling.

# Jinja2
In HAOS kunnen sjalonen (templates) worden gemaakt, m.b.v. een [scripttaal Jinja2](https://jinja.palletsprojects.com/en/latest/templates/),
dit moet verder worden uitgezocht hoe dit in zijn werk gaat. Het is een tool die andere scripttalen "maaktt", dus waarschijnlijk converteerd
het op de achtergrond een script naar een eigen HAOS gebruikt script.

# Python
HAOS maakt het mogelijk om Python programma's te starten, dit moet ook nog verder worden uitgezocht hoe dit exact in 
zijn werk gaat. Er is een begin van een voorbeeld op de website van Home Assistant zelf: [Python op Home Assistant](https://www.home-assistant.io/integrations/python_script/)

Even zelf overgestapt op **"pyscript**, deze lijkt nu correct te zijn geïnstalleerd.
Nu nog een script werkend zien te krijgen. Lastig omdat de bijgeleverde "documentatie" erg summier is.

# ESPHome
Er kan een module worden geinstalleerd, die het aansturen en uitlezen van o.a. ESP32 microcontrollers mogelijk maakt, deze 
gebruik ik regelmatig i.c.m. MicroPython/MySQL om verschillende sensoren aan te sturen, zoals voor temperatuur, luchtvochtigheid
en luchtdruk, bewegingssensoren (PIR) etc. Deze module heet [ESPHome](https://www.esphome.io/) en kan een waardevolle toevoeging
zijn in de toekomst. 

# AppleTV
Home Assistant is via de Apple TV als "Bridge" te gebruiken. Nu kun je makkelijk de Home/Thuis app van Apple gebruiken om alles
thuis of buitenshuis via het internet te schakelen.

# Raspberry Pi 5
Zelf heb ik ook een RP5 aangeschaft, en met HAOS voorzien en in gebruik gesteld om te experimenteren met Home Assistant.
Veel mogelijkheden om uit te zoeken.
