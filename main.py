import os
import json
import argparse
import datetime


def current_time():
    return datetime.datetime.now().isoformat()


if not os.path.exists('tasks.json'):
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


parser = argparse.ArgumentParser(description='Task CLI - управление задачами через командную строку')
subparsers = parser.add_subparsers(dest='command', required=True)

add_parser = subparsers.add_parser('add', help='Добавить новую задачу')
add_parser.add_argument('description', type=str, help='Описание задачи')

update_parser = subparsers.add_parser('update', help='Обновить задачу')
update_parser.add_argument('id', type=int, help='ID задачи')
update_parser.add_argument('description', type=str, help='Новое описание задачи')

delete_parser = subparsers.add_parser('delete', help='Удалить задачу')
delete_parser.add_argument('id', type=int, help='ID задачи')

mark_in_progress = subparsers.add_parser('mark-in-progress', help='Отметить задачу как в процессе выполнения')
mark_in_progress.add_argument('id', type=int, help='ID задачи')

mark_done_parser = subparsers.add_parser('mark-done', help='Отметить задачу как выполненную')
mark_done_parser.add_argument('id', type=int, help='ID задачи')

list_parser = subparsers.add_parser('list', help='Вывести список задач')
list_parser.add_argument('status', nargs='?', type=str, choices=["todo", "in-progress", "done"],
                         help="Фильтр по статусу (необязательно)")

if __name__ == "__main__":
    try:
        args = parser.parse_args()  # Получаем аргументы командной строки
    except SystemExit as e:
        parser.print_help()  # Показываем справку, если команда не указана
        exit(1)
    tasks_data = load_tasks()  # Загрузка задач

    if args.command == 'add':
        new_id = max((task['id'] for task in tasks_data['tasks']), default=0) + 1
        new_task = {
            "id": new_id,
            "description": args.description,
            "status": "todo",
            "createdAt": current_time(),
            "updatedAt": current_time()
        }
        tasks_data['tasks'].append(new_task)
        save_tasks(tasks_data)
        print(f"Задача успешно добавлена (ID: {new_id})")

    elif args.command == 'update':
        for task in tasks_data['tasks']:
            if task['id'] == args.id:
                task['description'] = args.description
                task['updatedAt'] = current_time()
                save_tasks(tasks_data)
                print(f"Задача с ID {args.id} успешно обновлена")
                break
        else:
            print(f"Задача с ID {args.id} не найдена")

    elif args.command == 'delete':
        tasks_data['tasks'] = [task for task in tasks_data['tasks'] if task['id'] != args.id]
        save_tasks(tasks_data)
        print(f"Задача с ID {args.id} успешно удалена")

    elif args.command == "mark-in-progress":
        # Отметить задачу как в процессе выполнения
        for task in tasks_data["tasks"]:
            if task["id"] == args.id:
                task["status"] = "in-progress"
                task["updatedAt"] = current_time()
                save_tasks(tasks_data)
                print(f"Задача с ID {args.id} успешно отмечена как 'в процессе выполнения'")
                break
        else:
            print(f"Задача с ID {args.id} не найдена")

    elif args.command == 'mark-done':
        # Отметить задачу как выполнен
        for task in tasks_data['tasks']:
            if task['id'] == args.id:
                task['status'] = 'done'
                task["updatedAt"] = current_time()
                save_tasks(tasks_data)
                print(f"Задача с ID {args.id} успешно отмечена как 'выполненная'")
                break
        else:
            print(f"Задача с ID {args.id} не найдена")

    elif args.command == 'list':
        # Вывод задач
        if args.status:
            filtered_tasks = [task for task in tasks_data["tasks"] if task["status"] == args.status]
        else:
            filtered_tasks = tasks_data['tasks']
        if not filtered_tasks:
            print("Нет задач для отображения")

        else:
            for task in filtered_tasks:
                print(f"ID: {task['id']}")
                print(f"Описание: {task['description']}")
                print(f"Статус: {task['status']}")
                print(f"Создано: {task['createdAt']}")
                print(f"Обновлено: {task['updatedAt']}")
                print("-" * 40)

