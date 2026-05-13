# Особенности рашения

## Task 2

### Сборка
Для сборки docker-образа использовать команду(из корня проекта):
```bash
docker build -f task_2/Dockerfile -t http-checker:latest .

```

### Запуск
Для запуска docker-контейнера:
```bash
docker run --name task-2 http-checker:latest
```

### Логи
Для прочтения логов docker-контейнера:
```bash
docker logs task-2
```

Пример вывода логов:
```log
2026-05-13 13:17:11,230 - ERROR - Received an error status code: 502
2026-05-13 13:17:11,508 - INFO - Success response, status code: 200
2026-05-13 13:17:11,713 - INFO - Success response, status code: 301
2026-05-13 13:17:11,965 - ERROR - Received an error status code: 408
2026-05-13 13:17:12,168 - ERROR - Received an error status code: 502
```


