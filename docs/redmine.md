# Redmine для проекта «ТелекомСервис»

Система управления проектом развёрнута вручную на виртуальной машине UbuntuOC
(Ubuntu 26.04 LTS), так как в репозиториях Ubuntu 26.04 пакета Redmine нет.

| Компонент | Версия |
|---|---|
| Redmine | 6.1.4 |
| Ruby / Rails | 3.3.8 / 7.2 |
| СУБД | PostgreSQL 18 |
| Веб-сервер | Apache 2.4 + Passenger |

- Каталог приложения: `/home/redmine/redmine-6.1.4`
- Адрес: `http://<IP ВМ>/redmine/`
- База данных `redmine`, настройки в `config/database.yml`
- Виртуальный хост: `/etc/apache2/sites-available/master.conf`
- Резервная копия: скрипт `/home/redmine/backup_redmine.sh`
  (дамп БД, файлы вложений, настройки и темы)
