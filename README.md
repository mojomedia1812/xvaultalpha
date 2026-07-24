# xVAULT Alpha

xVAULT Alpha to polsko zlokalizowany dodatek wideo Kodi do wyszukiwania i odtwarzania filmów, seriali oraz LiveTV. To repozytorium dotyczy wyłącznie wariantu `plugin.video.xvaultalpha`.

## Aktualna wersja

Aktualny stan: `2026.07.23.6`

Głównym źródłem wersji jest [`addon.xml`](addon.xml). Po każdej zmianie wersji w `addon.xml` należy sprawdzić i w razie potrzeby zaktualizować tę README.

## Instalacja

1. Pobierz aktualny ZIP dodatku z [mojomedia1812.github.io/xvaultalpha](https://mojomedia1812.github.io/xvaultalpha/).
2. W Kodi otwórz **Dodatki > Zainstaluj z pliku ZIP**.
3. Wybierz plik `plugin.video.xvaultalpha-2026.07.23.6.zip`.
4. Uruchom xVAULT Alpha.

Alternatywnie można zainstalować ZIP repozytorium: [https://mojomedia1812.github.io/xvaultalpha/repository.xvault.zip](https://mojomedia1812.github.io/xvaultalpha/repository.xvault.zip). Po instalacji Kodi będzie znajdować nowe wersje xVAULTalpha przez repozytorium Alpha.

Kodi instaluje oficjalne zależności z skonfigurowanych repozytoriów. Moduły niedostępne w oficjalnym repozytorium Kodi, takie jak ResolveURL, są doinstalowywane przy pierwszym starcie z oficjalnych źródeł.

Więcej informacji o zależnościach znajduje się w [`DEPENDENCIES.md`](DEPENDENCIES.md).

## Użycie

- Szczegółowy podręcznik jest dostępny na [mojomedia1812.github.io/xvaultalpha/handbuch/](https://mojomedia1812.github.io/xvaultalpha/handbuch/).
- Filmy, seriale i osoby można wyszukiwać z menu xVAULT.
- LiveTV korzysta wyłącznie z polskiej listy kanałów z kategoriami, wyszukiwaniem i ulubionymi.
- Źródła można uruchamiać przez dialog, katalog albo autoodtwarzanie.
- Ulubione i stany odtwarzania można opcjonalnie synchronizować przez obszar kont.
- Status obejrzenia filmów, sezonów, seriali i odcinków jest wyliczany z bieżących stanów odtwarzania.

## Funkcje

- Polskie menu Kodi, ustawienia, dialogi, komunikaty, metadane dodatku, komunikaty Trakt/Sync/Plus/Support oraz strony publikacji.
- Wyszukiwanie i odtwarzanie filmów, seriali, odcinków specjalnych i LiveTV.
- xVAULT może działać jako player dla TMDbHelper bez utraty własnej logiki źródeł, wyboru resolvera i monitorowania odtwarzania.
- Etykieta odtwarzania pokazuje hoster oraz stronę indeksującą, np. `VOE @ SerienStream`.
- Domyślna akcja `Dialog`, `Katalog` albo `Autoodtwarzanie` jest odczytywana z aktualnych ustawień dodatku, z lokalnym plikiem profilu jako fallbackiem.
- Listy źródeł są krótko cache'owane w bieżącej sesji Kodi, a linki hosterów są nadal świeżo rozwiązywane i testowane.
- Język streamów może być preferowany lub filtrowany; źródła wielojęzyczne mogą być dopuszczane według ustawień.
- Serie obsługują odcinki specjalne z sezonu TMDB 0 jako osobne wpisy.
- LiveTV i LiveTV lite używają tylko polskiej listy xVAULTalpha. Kanały niemieckie, austriackie, szwajcarskie i jasno obcojęzyczne są filtrowane z katalogu, cache i ulubionych.
- LiveTV używa lokalnego cache, polskich kategorii, logo kanałów, polskiego EPG, sprawdzania dostępności kanałów oraz fallbacków hostów `huhu.to`, `oha.to` i `vavoo.to`.
- Dostępne są pobieranie, napisy i zewnętrzne menedżery pobierania.
- Dostępna jest synchronizacja ulubionych i stanów odtwarzania przez host API `xvault-sql.ddnss.de`.
- Trakt obsługuje logowanie kodem urządzenia, watchlistę, kolekcję, import/eksport obejrzanych, scrobbling i oceny.
- DNS over HTTPS jest domyślnie aktywny i można go wyłączyć w ustawieniach ogólnych.
- Narzędzia wsparcia tworzą redigowany pakiet diagnostyczny, który po potwierdzeniu może zostać przesłany i udostępniony przez krótką identyfikację usługi.
- Opcjonalne statystyki użycia identyfikują ten wariant jako kanał `alpha` i wersję `2026.07.23.6-alpha`.
- Obszar Plus pozwala wrócić z xVAULTalpha do standardowego dodatku xVAULT przez instalację najnowszej wersji standardowej.

## Zgłaszanie błędów i propozycji

Błędy i propozycje zmian prosimy zgłaszać przez [GitHub Issues xvaultalpha](https://github.com/mojomedia1812/xvaultalpha/issues).

Dobre zgłoszenie zawiera:

- używaną wersję xVAULTalpha,
- wersję Kodi i system,
- dokładne kroki odtworzenia,
- oczekiwane i rzeczywiste zachowanie,
- zrzuty ekranu lub logi, jeśli są dostępne.

## Umami Analytics

Umami jest używane do prywatnościowej statystyki odwiedzin strony GitHub Pages. Identyfikator strony znajduje się w kodzie śledzenia HTML w `docs/`.

Szanujemy Do Not Track, parametry wyszukiwania URL nie są zbierane, a kliknięcia linków do pobrań, plików repozytorium, GitHuba i ważnych linków wewnętrznych są rejestrowane jako zdarzenia Umami. Nazwy zdarzeń nie zawierają prywatnych danych użytkowników.

Do repozytorium nie trafiają dane logowania, sekrety, prywatne klucze API ani osobiste treści.

## Statystyki użycia dodatku

Opcjonalne statystyki użycia xVAULT korzystają z Supabase jako backendu i można je włączyć lub wyłączyć w obszarze ustawień **Statystyki**.

Zbierane są tylko techniczne dane cyklu życia: utworzenie instalacji, start dodatku, zakończenie dodatku, heartbeat co 10 minut, wersja Kodi, wersja xVAULT, klasa systemu operacyjnego, klasa urządzenia, status online i ostatnia aktywność. Dodatek nie wysyła tytułów, zapytań wyszukiwania, adresów streamów, ulubionych, danych logowania, sekretnych kluczy API, prywatnych ścieżek ani osobistych wpisów.

Lokalny identyfikator instalacji jest losowo wygenerowanym UUID. W Supabase jest zapisywany w postaci hasha przez funkcję ingest. Bezpośredni dostęp do tabel jest blokowany przez RLS; dodatek używa tylko publicznego endpointu RPC Supabase z Publishable Key.

## Współpraca

Informacje dla osób współpracujących znajdują się w [`CONTRIBUTING.md`](CONTRIBUTING.md).

Przy zmianach wersji, ustawień lub funkcji należy sprawdzić i w razie potrzeby zaktualizować README.

## Changelog

- Zmiany repozytorium i dokumentacji: [`CHANGELOG.md`](CHANGELOG.md)
- Historia wersji dodatku: [`CHANGELOG.txt`](CHANGELOG.txt)

## Kompatybilność

xVAULT jest dodatkiem Kodi dla Pythona 3 i deklaruje w [`addon.xml`](addon.xml) `xbmc.python` od wersji `3.0.0`. LiveTV-HLS działa na Windows, Linux i Androidzie: xVAULT używa automatycznie FFmpeg Direct, jeśli jest zainstalowany i aktywny na platformie, a w przeciwnym razie przechodzi na wewnętrzne odtwarzanie HLS Kodi. InputStream Adaptive pozostaje ręcznie wybieralną alternatywą.

Dla testów urządzeń Fire TV Stick opartych na Androidzie dostępny jest profilowy symulator w [`docs/firetv-stick-simulator.md`](docs/firetv-stick-simulator.md). Nie zastępuje prawdziwego emulatora FireOS-ROM, ale pomaga sprawdzać Fire OS, poziom Android API, RAM, klasę kodeków i ryzyka Kodi.

Dla Kodi z zainstalowanym xVAULT dostępny jest także `tools/kodi_firetv_test.py`. Domyślny przebieg celuje w `aftmm`, czyli Fire TV Stick 4K - 1st Gen, i sprawdza smoke testy Kodi oraz spójność lokalnych baz danych przy symulowanym nacisku na pamięć i błędy zapisu.
