Uruchomienie aplikacji poprzez komendę:

sudo docker-compose up --build

Adresy:

https://localhost:8080/    - dotychczasowa aplikacja klienta
https://localhost:8081/    - dotychczasowa aplikacja obsługująca pliki pdf
https://localhost:8082/    - aplikacja kuriera
https://localhost:8083/    - aplikacja paczkomatu
https://localhost:8084/    - aplikacja służąca jako pośrednik do komunikacji przez web-sockets


Dodatkowe uwagi:
Bardzo ważne jest, aby najpierw odwiedzić wszystkie wyżej wymienione witryny, aby zaakceptować blokadę ryzyka.

Dla Pana wygody pod ukrytym adresem:

https://localhost:8082/register
jest formularz rejstracji nowych kurierów z podstawową walidacją

https://localhost:8082/register_kurier_oauth
jest link do rejstracji nowych kurierów przez oAuth





Pod adresem
https://localhost:8083/show_packages_p1_0
i
https://localhost:8083/show_packages_p2_0
znajduje się lista paczek z paginacją.
Niestety możliwe, że nie da się dostać tam (póki co) inaczej, niż bezpośrednio przez te adresy.

https://localhost:8082/login_kurier_oauth
jest możliwe jedynie zalogowanie się na konto kuriera, rejstracja jest niemożliwa (chyba że pod adresem https://localhost:8082/register_kurier_oauth)