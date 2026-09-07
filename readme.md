# GPW Grafana raport

Aplikacja wyswietla na żywo dane dotyczące wartści wybranych indeksów i spółek z GPW.
Webscraping odbywa się przy użyciu  **Python** i **Beautiful Soup**, a wizualizacja za pomocą **Grafaną**. Komunikacja miedzy dashboardem a aplikacją pobierajacą dane odbywa się przy użyciu **Rest API**.  Projet uruchamiany jest w środowisku  **Docker**.

![Podgląd widoku raportu](/image.png)

## 📋 Wymagania

Przed uruchomieniem projektu upewnij się, że masz zainstalowane:

- [Docker](https://www.docker.com/)
- Docker Compose
- Git — opcjonalnie

Sprawdzenie instalacji:

```bash
docker --version
docker compose version
```


## 🚀 Uruchomienie

Sklonuj repozytorium:

```bash
git clone <URL_REPOZYTORIUM>
cd <NAZWA_PROJEKTU>
```

Uruchom kontenery:

```bash
docker compose up -d --build
```

Sprawdź status:

```bash
docker compose ps
```

Logi aplikacji Python:

```bash
docker compose logs -f python-app
```

Logi Grafany:

```bash
docker compose logs -f grafana
```

## 🌐 Dostęp do usług

Po uruchomieniu:

| Usługa | Adres | Opis |
|---|---|---|
| Webscraper| http://localhost:8010 | Aplikacja Python |
| Grafana | http://localhost:8000 | Dashboardy  |

## 🚀 Pierwsze uruchomienie Grafana

Domyślne dane logowania do Grafany:

```text
Login: grafana
Hasło: grafana
```

Po pierwszym zalogowaniu Grafana może poprosić o zmianę hasła.

Po uruchomieniu  należy przejść do zakładki Connection -> Add new datasorce i zainstalować Infinity
Następnie należy przejsć do Connection -> Datasorce i dodać zainstalowane Infinity 
W zakładce Dashboards należy kliknąć New a następnie Import dashboard
Plik do inport znajduje się w folderze (/grafana/gpw_raport.json)

## 🐍 Aplikacja Python

Aplikacja Python działa w osobnym kontenerze Docker. Pełni role 





## 🐳 Docker Compose

Przykładowa konfiguracja:

```yaml
services:
  grafana:
    image: grafana/grafana
    container_name: grafana
    restart: unless-stopped
    ports:
      - '8000:3000'
    environment:
      - GF_SECURITY_ADMIN_USER=grafana     
      - GF_SECURITY_ADMIN_PASSWORD=grafana
    volumes:
      -  grafana-stor:/var/lib/grafana
  webscraper:
    build:
      context: ./webscraper
      dockerfile: Dockerfile 
    ports:
     - "8010:8000" 
    volumes:
     - ./app:/app 

volumes:
  grafana-stor: {}
```

## 🔄 Zatrzymanie projektu

Aby zatrzymać kontenery:

```bash
docker compose down
```

Aby zatrzymać kontenery i usunąć również wolumeny:

```bash
docker compose down -v
```

> ⚠️ Usunięcie wolumenu spowoduje usunięcie danych przechowywanych przez Grafanę.

## 🔧 Przebudowanie aplikacji

Po zmianie kodu Python można przebudować kontener:

```bash
docker compose up -d --build
```

Można również wykonać:

```bash
docker compose build
docker compose up -d
```



## 📌 Technologie

Projekt wykorzystuje:

- **Python**
- **Fast API**
- **Beautiful Soup**
- **Docker**
- **Docker Compose**
- **Grafana**


