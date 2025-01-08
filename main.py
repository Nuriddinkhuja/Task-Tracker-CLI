import os
import json
import argparse

if os.path.exists('tasks.json'):
    with open('tasks.json', 'w') as file:
        json.dump({'tasks': []}, file)  # создаем базовую структуру
        print('tasks.json создан с базовый структурой.')


def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'tasks': []}


def save_tasks(data):
    with open('tasks.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    tasks_data = load_tasks()  # Загрузка задач
    print("Текущие задачи:", tasks_data)

    # Добавь тестовые данные и сохрани их
    tasks_data["tasks"].append({
        "id": 1,
        "description": "Test task",
        "status": "todo",
        "createdAt": "2025-01-08T10:00:00",
        "updatedAt": "2025-01-08T10:00:00"
    })
    save_tasks(tasks_data)

    # Убедись, что данные сохраняются
    print("Обновленные задачи:", load_tasks())
