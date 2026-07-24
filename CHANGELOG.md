# Changelog xVAULTalpha

## 2026.07.23.6

Deweloper: mojomedia1812

- Cały widoczny interfejs xVAULTalpha został przetłumaczony na język polski: menu Kodi, ustawienia, dialogi, LiveTV, Sync, Trakt, Plus, Support, MediaInfo, aktualizacje i komunikaty startowe.
- xVAULTalpha zgłasza się w statystykach jako kanał `alpha` z wersją `2026.07.23.6-alpha`, aby dane Alpha były jednoznacznie odseparowane od standardowego xVAULT.
- Metadane TMDB, plakaty, fanarty, zwiastuny, domyślne napisy i listy języków preferują teraz język polski oraz region PL.
- GitHub Pages, README, podręcznik, dokumentacja synchronizacji, metadane repozytorium i generowane listy pobierania są publikowane po polsku dla repozytorium xvaultalpha.
- Pakiety `plugin.video.xvaultalpha-2026.07.23.6.zip`, katalog repozytorium i indeks Kodi zostały przebudowane z polską lokalizacją.

## 2026.07.23.5

- Repozytorium Alpha zostało rozdzielone od standardowego xVAULT i publikuje pakiety pod adresem `https://mojomedia1812.github.io/xvaultalpha/`.
- Metadane repozytorium i ZIP repozytorium wskazują na stronę xvaultalpha GitHub Pages.
- README i strona pobierania opisują wyłącznie wariant `plugin.video.xvaultalpha`.
- Automatyczny generator repozytorium czyści dawne linki strony xVAULT i utrzymuje aktualne archiwa Alpha.

## 2026.07.23.4

- LiveTV w xVAULTalpha przełączono na polskie kanały; katalog, cache, ulubione, EPG i dopasowanie logo używają Polski oraz domen `.pl`.
- LiveTV lite korzysta z tej samej polskiej listy kanałów xVAULTalpha.
- Kanały niemieckie, austriackie, szwajcarskie i inne jawnie obcojęzyczne są filtrowane z katalogu, cache i ulubionych.
- Jeśli `huhu.to` jest niedostępne, LiveTV próbuje `oha.to`, a następnie `vavoo.to` jako hostów zapasowych.

## 2026.07.23.3

- W ustawieniach Plus dodano opcję powrotu z xVAULTalpha do standardowego xVAULT przez pobranie najnowszej stabilnej wersji.
- Mechanizm aktualizacji zachowuje rozdzielenie identyfikatorów dodatków i nie miesza repozytoriów xvaultalpha oraz xVAULT.
- Informacje wsparcia i status dodatku pokazują wariant Alpha w sposób zgodny z nowym repozytorium.

## 2026.07.19.1

- Domyślna akcja odtwarzania używa własnego wyboru xVAULT zamiast problematycznego enum Kodi.
- Tryby `Dialog`, `Katalog` i `Autoodtwarzanie` są przechowywane w profilu dodatku, a starsze wartości są migrowane przy starcie.
- Streamy Vixcloud zachowują wymagane nagłówki manifestu również w ścieżce odtwarzania Kodi.

## 2026.07.13.1

- xVAULT może działać jako odtwarzacz dla TMDbHelper i przyjmuje parametry filmów oraz odcinków przez własną trasę `playTMDbHelper`.
- Wywołania TMDbHelper korzystają z logiki źródeł xVAULT, resolverów, monitorowania Trakt i wybranego trybu wyboru streamu.
- Metadane odtwarzania są budowane ostrożniej, aby listy, ulubione i starsze wpisy Kodi nie wymuszały brakujących pól.

## 2026.07.10.1

- Dodano LiveTV lite jako szybki, osobny punkt menu.
- Streamy HLS są sprawdzane przed startem, aby martwe źródła nie kończyły się błędem odtwarzania Kodi.
- Źródła wymagające wyłącznie przeglądarki albo osadzeń chronionych są rozpoznawane i zatrzymywane z czytelnym komunikatem.

## 2026.07.05.1

- LiveTV sprawdza aktualne segmenty HLS przed startem i wybiera pasujący stream zapasowy, gdy główny kanał jest niestabilny.
- Cache kanałów, EPG i logo został uporządkowany, aby odświeżenie listy nie wymagało ręcznej naprawy profilu.
- Ustawienia silnika HLS pozwalają używać trybu automatycznego, wewnętrznego Kodi, FFmpeg Direct albo InputStream Adaptive.

## 2026.06.29.1

- LiveTV zostało włączone jako samodzielny moduł xVAULT z kategoriami, wyszukiwaniem, ulubionymi i odświeżaniem listy.
- EPG pokazuje aktualny i następny program dla obsługiwanych kanałów.
- Ustawienia LiveTV obsługują cache EPG, dialog programu i konfigurację bufora.

## 2026.06.28.8

- Usunięto stary obszar livestreamów i dopasowano metadane dodatku do filmów, seriali oraz LiveTV.
- Listy sezonów i odcinków odświeżają się po odtwarzaniu bez opuszczania widoku.
- Status obejrzenia sezonów i seriali jest przeliczany po zakończeniu odcinka.

## 2026.06.01

- Dodano integrację Trakt: status, watchlist, collection, import obejrzanych, scrobbling i oceny.
- Synchronizacja xVAULT zapisuje ulubione, stany binge i postęp odtwarzania dla wielu urządzeń.
- Ulubione są scalane po stronie serwera, a jawnie usunięte wpisy nie wracają ze starszych snapshotów.

## 2026.05.01

- Rozbudowano obsługę źródeł filmów i seriali, filtrowanie języka streamu oraz sortowanie jakości.
- Autoodtwarzanie respektuje aktualny tryb wyboru streamu i ogranicza zawieszone resolvery przez timeouty.
- Lista źródeł jest krótkotrwale cache'owana, aby zmiana streamu nie pobierała ponownie wszystkich stron indeksu.

## 2026.04.01

- Dodano specjalne odcinki sezonu TMDB 0 i poprawiono mapowanie nietypowych odcinków u providerów.
- Scraperzy otrzymują tytuł odcinka i datę premiery, aby lepiej rozpoznawać przypadki specjalne.
- Playcount, zakładki i synchronizacja zachowują normalny tytuł bez dopisków hostera.

## 2026.03.01

- Poprawiono zgodność z Kodi 21, Android TV i Fire TV przez lżejsze metadane list oraz ostrożniejsze InfoTagi.
- Dodano narzędzia testowe i symulator Fire TV do kontroli wydajności, zgodności kodeków i struktury dodatku.
- Dokumentacja instalacji oraz obsługi została uporządkowana pod publikację przez GitHub Pages.

## Starsza historia

- Starsze wydania rozwijały podstawowe menu filmów, seriali, wyszukiwania, historii, ulubionych i dostawców źródeł.
- Stopniowo dodawano obsługę napisów, MediaInfo, downloaderów, JDownloader, pyLoad, DNS over HTTPS i bezpieczniejszych requestów.
- Kolejne aktualizacje usuwały błędy odtwarzania, poprawiały cache, ujednolicały ustawienia i przygotowały bazę pod obecny wariant xVAULTalpha.
