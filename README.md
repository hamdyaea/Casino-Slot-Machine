# Slot Machine — Virtual Credits Demo

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

A modern Python 3/Tkinter slot-machine **simulation using virtual credits only**. There is no real-money betting, payment system or external service. The rules have been redesigned to be explicit: 100 starting credits, 10 credits per spin, 20 credits for two matching symbols, 50 credits for three matching symbols, zero otherwise. The balance never goes below zero.

```sh
python3 CasinoSlot.py
python3 CasinoSlot.py --text
python3 -m unittest discover -s tests -v
```

No EasyGUI, audio driver or third-party Python package is required. Historical version: [old branch](https://github.com/hamdyaea/Casino-Slot-Machine/tree/old).
