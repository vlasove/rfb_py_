## Лекция 19. PIP и сторонние пакеты

* **PIP** - менеджер установки пакетов в `Python` (`pypi.org` - хранилище всех пакетов среди разработчиков `Python`)

* Для того, чтобы устанавливать пакеты через `pip`:
    1. Проверить, что `pip` установлен : `pip --version`
    2. Для установки `pip install <package_name>`

### 0. Настройка pip через proxy

1) Через proxy:

```
pip install --proxy http://username:password@proxy:port <package_name>
или
pip install --proxy https://username:password@proxy:port <package_name>
```

2) Или в командной строке можно задать:
```
set HTTP_PROXY=http://username:password@proxy:port
set HTTPS_PROXY=https://username:password@proxy:port
и выполняете
pip install <package_name>
```