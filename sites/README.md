# Folder sites xVAULT

`xVAULT` obsługuje własny katalog `sites/` na poziomie dodatku, zgodny ze strukturą `plugin.video.xstream/sites`.

- Jeśli znajdują się tu moduły providerów (`*.py`), są ładowane w pierwszej kolejności.
- Jeśli katalog jest pusty, `xVAULT` nadal automatycznie używa dotychczasowych providerów legacy z `scrapers/scrapers_source/de`.

Dzięki temu oba dodatki można utrzymywać z tą samą strukturą katalogów.
