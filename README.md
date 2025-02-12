# Task CLI

Task CLI — это приложение командной строки для управления задачами. Оно позволяет создавать, обновлять, удалять задачи и отслеживать их статус (todo, in-progress, done). Все данные хранятся в JSON-файле.

## Возможности

- Добавление новой задачи.
- Обновление описания задачи.
- Удаление задачи.
- Изменение статуса задачи (“в процессе” или “выполнено”).
- Вывод списка задач с фильтрацией по статусу.

## Установка

1. Убедитесь, что у вас установлен Python версии 3.6 или выше.
2. Склонируйте или загрузите репозиторий с этим проектом.
3. Убедитесь, что файл `tasks.json` будет автоматически создан в текущей директории при первом запуске приложения.

## Использование

### Добавление новой задачи
```bash
python task-cli.py add "Купить продукты"
```
**Результат:**
```
Задача успешно добавлена (ID: 1)
```

### Обновление задачи
```bash
python task-cli.py update 1 "Купить продукты и приготовить ужин"
```
**Результат:**
```
Задача с ID 1 успешно обновлена
```

### Удаление задачи
```bash
python task-cli.py delete 1
```
**Результат:**
```
Задача с ID 1 успешно удалена
```

### Изменение статуса задачи

- Отметить задачу как "в процессе выполнения":
```bash
python task-cli.py mark-in-progress 1
```
**Результат:**
```
Задача с ID 1 успешно отмечена как 'в процессе выполнения'
```

- Отметить задачу как "выполненную":
```bash
python task-cli.py mark-done 1
```
**Результат:**
```
Задача с ID 1 успешно отмечена как 'выполненная'
```

### Вывод списка задач

- Вывести все задачи:
```bash
python task-cli.py list
```

- Вывести задачи со статусом "выполненные":
```bash
python task-cli.py list done
```

- Вывести задачи со статусом "в процессе выполнения":
```bash
python task-cli.py list in-progress
```

**Результат:**
```
ID: 1      Описание: Купить продукты     Статус: todo        Создано: 2025-01-08T10:00:00 Обновлено: 2025-01-08T10:00:00
-----------------------------------------------------------------------------------------
```

## Структура данных

Каждая задача в JSON-файле имеет следующую структуру:
```json
{
    "id": 1,
    "description": "Купить продукты",
    "status": "todo",
    "createdAt": "2025-01-08T10:00:00",
    "updatedAt": "2025-01-08T10:00:00"
}
```

## Ошибки и обработка исключений
- Если команда не указана:
  ```bash
  python task-cli.py
  ```
  **Результат:**
  ```
  Ошибка: команда не указана или указана неверно.
  usage: task-cli.py [-h] {add,update,delete,mark-in-progress,mark-done,list} ...
  ```

- Если задача с указанным ID не найдена:
  ```bash
  python task-cli.py update 99 "Новое описание"
  ```
  **Результат:**
  ```
  Задача с ID 99 не найдена
  ```

## Разработчики

- **Нуриддин**

## Лицензия

Этот проект находится под лицензией MIT. Используйте свободно!

[Сслыка на проект: https://github.com/Nuriddinkhuja/Task-Tracker-CLI](https://roadmap.sh/projects/task-tracker)
