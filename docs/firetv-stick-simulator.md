# Symulator Fire TV Stick

Ten symulator odwzorowuje profile Fire OS oparte na Androidzie dla wariantów Fire TV Stick. Nie jest emulatorem FireOS-ROM i nie zawiera firmware Amazon, komponentów DRM ani własnościowych usług Amazon. Vega OS celowo nie jest uwzględniony.

Celem jest szybkie laboratorium kompatybilności dla xVAULT:

- wybór profilu Fire TV Stick,
- podgląd Fire OS, wersji Androida, poziomu API, modelu build, RAM, pamięci, ABI i klasy kodeków,
- sprawdzenie `addon.xml` xVAULT względem najważniejszych ryzyk Fire TV,
- eksport symulowanych wartości systemu Android jako wynik podobny do `getprop`, JSON albo wartości środowiskowe Windows,
- zaplanowanie profilu testowego Android-TV-AVD według podejścia Amazon AVD.

## Użycie

Wszystkie polecenia uruchamia się z katalogu głównego repozytorium.

```powershell
python tools/firetv_stick_simulator.py list
python tools/firetv_stick_simulator.py show fire-tv-stick-4k-max-2nd-gen-2023
python tools/firetv_stick_simulator.py check fire-tv-stick-2nd-gen-2016
python tools/firetv_stick_simulator.py matrix
python tools/firetv_stick_simulator.py properties aftkm --format json
python tools/firetv_stick_simulator.py avd-plan aftkrt
```

Dla testów Kodi z zainstalowanym xVAULT dostępny jest dodatkowo symulator Kodi. Domyślnie używany jest profil `aftmm`, czyli Fire TV Stick 4K - 1st Gen (2018), ponieważ Fire OS 6 / API 25, 1.5 GB RAM i 8 GB pamięci tworzą krytyczną granicę.

```powershell
python tools/kodi_firetv_test.py limits --profile aftmm
python tools/kodi_firetv_test.py smoke --profile aftmm --action root
python tools/kodi_firetv_test.py db-stress --profile aftmm
python tools/kodi_firetv_test.py all --profile aftmm --keep-profile
```

Symulator Kodi stubuje najważniejsze moduły Kodi Python (`xbmc`, `xbmcaddon`, `xbmcgui`, `xbmcplugin`, `xbmcvfs`) i uruchamia xVAULT przeciw tymczasowemu profilowi. Test DB-stress sprawdza lokalne magazyny Pickle i `playcount.db` pod kątem spójności po wielu zapisach, symuluje błędy pełnej pamięci i wykonuje `PRAGMA integrity_check` dla SQLite.

Profile można wybierać po ID, aliasie albo modelu build. Przykłady:

- `aftkrt` dla Fire TV Stick 4K Max - 2nd Gen (2023),
- `aftkm` dla Fire TV Stick 4K - 2nd Gen (2023),
- `aftss` dla klasy Fire TV Stick Lite / HD,
- `aftt` dla Fire TV Stick 2nd Gen / Basic Edition.

## Zakres

Uwzględnione są warianty Fire TV Stick oparte na Androidzie z Fire OS 5, 6, 7 i 8. Dla xVAULT szczególnie istotne są te granice:

- Fire OS 8 / Android 11 / API 30: aktualny cel Android,
- Fire OS 7 / Android 9 / API 28: szeroka baza 1080p i 4K,
- Fire OS 6 / Android 7.1 / API 25: baza legacy 4K,
- Fire OS 5 / Android 5.1 / API 22: bardzo stary cel z wysokim ryzykiem Kodi.

## Ograniczenia

Symulator nie uruchamia prawdziwego Fire OS. Symuluje profile i ryzyka kompatybilności, ale nie:

- Amazon Launcher, Appstore, Alexa, DRM ani zachowania Widevine,
- prawdziwą pipeline mediów Android,
- prawdziwe zdarzenia pilota,
- samego Kodi,
- sideloadingu ani firmware urządzenia.

Do prawdziwych testów runtime nadal potrzebny jest fizyczny Fire TV Stick albo emulator Androida z porównywalnym poziomem API. Emulator Androida nie zastępuje w pełni Fire OS, ponieważ brakuje usług specyficznych dla Fire TV i interfejsu Fire TV.

## Android-TV-AVD według wzorca Amazon

Amazon opisuje dla Fire Tablets podejście przez Android Virtual Device Manager: utworzyć profil sprzętowy, ustawić pamięć i ekran, a następnie utworzyć wirtualne urządzenie Android. Strona Amazon jasno mówi, że te kroki nie symulują Fire TV. Dla xVAULT podejście nadal jest użyteczne jako przybliżenie Android TV.

Narzędzie tworzy przez `avd-plan` checklistę dla Android Studio:

- Device Type: TV,
- Screen: 1080p albo 4K zgodnie z klasą sticka,
- Memory: RAM profilu Fire TV Stick,
- Input: Remote/D-Pad zamiast dotyku,
- Sensors i Cameras: wyłączone,
- System image: Android TV z najbliższym pasującym poziomem API.

Przykład:

```powershell
python tools/firetv_stick_simulator.py avd-plan fire-tv-stick-4k-2nd-gen-2023
```

Dzięki temu można wcześnie testować nawigację Kodi, nacisk layoutu, poziom API i granice RAM. Amazon Launcher, Appstore, Alexa, DRM, właściwości dekoderów i dokładne zachowanie Fire OS pozostają testami dla prawdziwego sprzętu.

## Fokus AFTMM

Fire TV Stick 4K - 1st Gen (2018), model build `AFTMM`, jest szczególnie interesującym profilem problemowym:

- Fire OS 6 / Android 7.1 / API 25,
- 32-bit ABI,
- 1.5 GB RAM,
- 8 GB pamięci,
- obsługa 4K/HDR, ale bez AV1.

Zalecany przebieg dla tego profilu:

```powershell
python tools/kodi_firetv_test.py all --profile aftmm --iterations 500 --keep-profile
```

Jeśli pojawi się `FAIL`, przyczyna jest bezpośrednio wskazana w wyniku. `WARN` oznacza granice, które należy dodatkowo sprawdzić na prawdziwym sprzęcie.

## Baza danych

Profile bazują na oficjalnych stronach developerskich Amazon:

- https://developer.amazon.com/docs/device-specs/device-specifications-fire-tv-streaming-media-player.html
- https://developer.amazon.com/docs/device-specs/identify-fire-tv-devices.html
- https://developer.amazon.com/docs/fire-tablets/ft-testing-without-an-amazon-device.html
