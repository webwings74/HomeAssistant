# HomeAssistant
Projecten met betrekking tot het gebruik van het **Home Assistant OS** (HAOS), overwegend op een **Raspberry Pi 5**.
O.a. voor het uitlezen van gegevens van een warmtepomp en daarna als doel het besturen ervan, met
als input allerlei omgevings sensoren en weersvoorspelling.

# Jinja2
In HAOS kunnen sjalonen (templates) worden gemaakt, m.b.v. een
[scripttaal Jinja2](https://jinja.palletsprojects.com/en/latest/templates/),
dit moet verder worden uitgezocht hoe dit in zijn werk gaat.
Het is een tool die andere scripttalen "maaktt", dus waarschijnlijk converteerd
het op de achtergrond een script naar een eigen HAOS gebruikt script.

# Python
HAOS maakt het mogelijk om Python programma's te starten, dit moet ook nog verder worden uitgezocht hoe dit exact in 
zijn werk gaat. Er is een begin van een voorbeeld op de website van Home Assistant zelf:
[Python op Home Assistant](https://www.home-assistant.io/integrations/python_script/)

De website: [HACS PyScript](https://hacs-pyscript.readthedocs.io/en/latest/installation.html) geeft aan hoe dit
geïnstalleerd dient te worden. (**even lastig**).
Een extra hulp is [het YouTube filmpje](https://www.youtube.com/watch?v=Kr1rAJnVBrI)

# ESPHome
Er kan een module worden geinstalleerd, die het aansturen en uitlezen van o.a. **ESP32 microcontrollers** mogelijk maakt, deze 
gebruik ik regelmatig i.c.m. **MicroPython/MySQL** om verschillende sensoren aan te sturen,
zoals voor temperatuur, luchtvochtigheid en luchtdruk, bewegingssensoren (PIR) etc. Ook LED's via de GPIO's zijn in
automatiseringen op te nemen.
Deze module heet [ESPHome](https://www.esphome.io/) en kan een waardevolle toevoeging zijn in de toekomst. 

# AppleTV
Home Assistant is via de Apple TV als "Bridge" te gebruiken. Nu kun je makkelijk de Home/Thuis app van Apple gebruiken om alles
thuis of buitenshuis via het internet te schakelen. Dit werkte eerst prima (via de Raspberry Pi) maar nu lukt het buitenhuis schakelen niet zomaar, via de Synology in een Docker wel via de link [Synology DS718+ Home Assistant](http://webwings.synology.me:8123) 

# Raspberry Pi 5
Zelf heb ik ook een RP5 aangeschaft, en met HAOS voorzien en in gebruik gesteld om te experimenteren met Home Assistant.
Veel mogelijkheden om uit te zoeken.

# Mobiele Home Assistant Applicatie
Via iOS of Android kun je gebruik maken van de Home Assistant App.