# Synchronizacja xVAULT

## Cel

Synchronizacja xVAULT zapisuje ulubione Kodi i stany odtwarzania przypisane do użytkownika, aby można je było przywrócić lub połączyć po ponownej instalacji, zmianie urządzenia albo równoległym używaniu na kilku urządzeniach.

## Punkty końcowe API

API przyjmuje JSON i zawsze odpowiada JSON-em.

Aktualny host produkcyjny: `http://xvault-sql.ddnss.de/index.php?action=`

- `POST /index.php?action=register`
- `POST /index.php?action=login`
- `POST /index.php?action=favorites_push`
- `GET /index.php?action=favorites_pull`
- `POST /index.php?action=binge_push`
- `GET /index.php?action=binge_pull`
- `POST /index.php?action=sync_push`
- `GET /index.php?action=sync_pull`
- `GET /index.php?action=status`

Gdy aktywne jest przepisywanie URL-i, działają również odpowiednie ścieżki `/api/...`.

## Tabele bazy danych

- `users`: konto użytkownika, hash hasła, hash klucza API i metadane logowania.
- `favorites_backups`: wersjonowane kopie zapasowe ulubionych dla każdego użytkownika. Nowe kopie są po stronie serwera łączone z aktualnym stanem serwera; jawne `deleted_keys` zapobiegają ponownemu pojawieniu się usuniętych ulubionych przez inne urządzenie.
- `binge_state`: aktualny stan odtwarzania/binge dla stabilnego `item_key`. Wpisy są łączone przez upsert dla każdego filmu lub odcinka; nowszy postęp wygrywa, a już ukończone wpisy pozostają oznaczone jako obejrzane.
- `sync_log`: techniczna historia synchronizacji bez treści wrażliwych.

## Zachowanie na wielu urządzeniach

- Przy starcie xVAULT pobiera aktualny stan binge z serwera i stosuje lokalnie zakładki oraz status obejrzenia.
- W trakcie pracy usługa w tle regularnie sprawdza zdalne zmiany. Dzięki temu ulubione i stan binge stają się widoczne na innych zalogowanych urządzeniach bez restartu.
- Ulubione są przed każdym pushem łączone z ostatnim stanem serwera. Równoległe dodatki z PC, Android TV i Raspberry pozostają zachowane.
- Usunięte ulubione są wysyłane jako skasowane klucze, aby równoległe urządzenie nie zapisało ich ponownie na serwerze ze starego snapshotu.
- Stan binge/obejrzenia jest przypisany do użytkownika. Gdy kilka urządzeń jest zalogowanych na tym samym koncie xVAULT, wszystkie widzą ten sam stan.

Tabele są tworzone automatycznie przy pierwszym wywołaniu API.

## Koncepcja bezpieczeństwa

- Hasła są zapisywane po stronie serwera przez `password_hash()`.
- Logowanie zwraca kryptograficznie losowy klucz API.
- W bazie danych zapisywany jest tylko hash SHA-256 klucza API.
- Dodatek Kodi zapisuje lokalnie tylko adres e-mail, klucz API, ID urządzenia, status synchronizacji oraz hashe i znaczniki czasu.
- Hasła nie są trwale zapisywane w dodatku.
- `api/config.php` jest wykluczony przez `.gitignore` i nie może trafić do repozytorium.

## Ustawienia dodatku

W sekcji `Ustawienia -> Konta` dostępne są:

- Włącz synchronizację
- Adres e-mail
- Status
- Ostatnia synchronizacja
- Zaloguj
- Zarejestruj
- Synchronizuj teraz
- Przywróć backup z serwera
- Pokaż status
- Pokaż informację o prywatności
- Wyloguj

## Przywracanie

Po zalogowaniu xVAULT sprawdza, czy istnieje backup ulubionych. Użytkownik decyduje, czy stan z serwera ma zastąpić lokalne ulubione, czy zostać z nimi połączony. Przed zapisem lokalny plik `favourites.xml` jest zabezpieczany jako `.xvault-backup-YYYYMMDDHHMMSS`.

## Deployment

Pliki serwerowe znajdują się w repozytorium w katalogu `api/`.

Na hoście docelowym obok `index.php` musi leżeć prawdziwy plik `config.php` z danymi dostępu do bazy. W repozytorium znajduje się tylko `config.example.php`.

Aktualny upload dla nowego miejsca Freehostia:

- `api/index.php` -> `/xvault-sql.ddnss.de/index.php`
- `api/.htaccess` -> `/xvault-sql.ddnss.de/.htaccess`
- lokalny, niewersjonowany `api/config.php` -> `/xvault-sql.ddnss.de/config.php`

## Sekrety

Nie commitować do Gita danych FTP, bazy danych, API ani haseł. Do testów lokalnych używać `api/config.php`, `.env` albo porównywalnych niewersjonowanych plików.
