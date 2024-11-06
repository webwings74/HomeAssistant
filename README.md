# HomeAssistant
Projecten met betrekking tot het gebruik van het **Home Assistant OS** (HAOS), overwegend op een **Raspberry Pi 5**.
O.a. voor het uitlezen van gegevens van een warmtepomp en daarna als doel het besturen ervan, met
als input allerlei omgevings sensoren en weersvoorspelling.

## Helpers
Via **helpers** kun je eigen stukken scripts maken en gegevens manipuleren die je wilt laten zien of gebruiken in 
HomeAssistant. Zelf heb ik o.a. het volgende stukje "sjabloon" gebruikt om het verschil tussen het terug geleverde
vermogen en het totale PV vermogen dat op het moment word opgeleverd:

`{{ '%0.1f' | format((states('sensor.solaredge_huidig_vermogen') | float) - (states('sensor.inverse_p1_vermogen') | float)) }}`

## Jinja2
In HAOS kunnen sjalonen (templates) worden gemaakt, m.b.v. een
[scripttaal Jinja2](https://jinja.palletsprojects.com/en/latest/templates/),
dit moet verder worden uitgezocht hoe dit in zijn werk gaat.
Het is een tool die andere scripttalen "maaktt", dus waarschijnlijk converteerd
het op de achtergrond een script naar een eigen HAOS gebruikt script.

## Python
HAOS maakt het mogelijk om Python programma's te starten, dit moet ook nog verder worden uitgezocht hoe dit exact in 
zijn werk gaat. Er is een begin van een voorbeeld op de website van Home Assistant zelf:
[Python op Home Assistant](https://www.home-assistant.io/integrations/python_script/)

De website: [HACS PyScript](https://hacs-pyscript.readthedocs.io/en/latest/installation.html) geeft aan hoe dit
geïnstalleerd dient te worden. (**even lastig**).
Een extra hulp is [het YouTube filmpje](https://www.youtube.com/watch?v=Kr1rAJnVBrI)

Dit "hoofdstuk" is nog niet afgesloten, v.w.b. expirimenteren met Python/Jupyter op de Raspberry Pi. Los van het feit
dat Jupyter zeker iets interessants is, los van het Home Assistant project. (Markdown en Python Scripts als Notebook)

## ESPHome
Er kan een module worden geinstalleerd, die het aansturen en uitlezen van o.a. **ESP32 microcontrollers** mogelijk maakt, deze 
gebruik ik regelmatig i.c.m. **MicroPython/MySQL** om verschillende sensoren aan te sturen,
zoals voor temperatuur, luchtvochtigheid en luchtdruk, bewegingssensoren (PIR) etc. Ook LED's via de GPIO's zijn in
automatiseringen op te nemen. Deze module heet [ESPHome](https://www.esphome.io/).

De beide test yaml configuraties zijn hier opgenomen onder:
1. esphome-web-8b413c.yaml
2. esphome-web-a2caf0.yaml

### PIR Module
Ik heb een **ESP32 WROOM** DevKit module geflashed met ESPHome, en in Home Assistant kan ik deze met sensoren bijwerken.
Het eerste projectje was een LED aan of uit met als trigger een PIR module (bewegingssensor), deze werkt erg mooi samen.
Als test de keukenverlichting aan, indien iemand tussen zonsondergang en zonsopgang langs de sensor loopt. (Deze automatisering moet ik nog maken in Home Assistant)

### Zonnestroom LED's
Een **ESP32 WROVER-E** module heeft twee LED's (rood en groen) via een "helper" script gaat de rode LED aan als er netstroom
gebruikt word, en een groene LED als er stroom komt vanaf de zonnepanelen. (Bijkomend effect: Als beide LED's aan staan
is er niet genoeg stroom van de zonnepanelen t.o.v. het verbruik).

## AppleTV
Home Assistant is via de Apple TV als "Bridge" te gebruiken. Nu kun je makkelijk de Home/Thuis app van Apple gebruiken om alles
thuis of buitenshuis via het internet te schakelen. Bij gebruik van een Raspberry Pi is dit niet noodzakelijk. 
Via de Home Assistant app op het mobiele device kun je ook een interne en een externe toegang krijgen.
Zie **Mobiele Home Assistant Applicatie**

## Raspberry Pi 5
Zelf heb ik ook een RP5 aangeschaft, en met HAOS voorzien en in gebruik gesteld om te experimenteren met Home Assistant.
Veel mogelijkheden om uit te zoeken. De 8123 poort voor HAOS is ook exposed naar het internet om de applicatie van buiten 
toegang te kunnen geven.

## Mobiele Home Assistant Applicatie
Via iOS of Android kun je gebruik maken van de Home Assistant App. Ook een manier om automatisch tussen een interne en een externe
verbinding te schakelen op de mobiele telefoon.
