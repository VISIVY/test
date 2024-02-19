import subprocess
import time

def create_unix_user(username, password):
    try:
        subprocess.run(["sudo", "useradd", "-m", username])
        subprocess.run(['echo', f'{username}:{password}', '|', 'sudo', 'chpasswd'], shell=True)

        print(f"Пользователь {username} успешно создан в Unix.")
    except subprocess.CalledProcessError as error:
        print(f"Ошибка при создании пользователя в Unix: {error}")

def create_samba_user(username, password):
    try:
        # Формируем команду для создания пользователя
        command = f"sudo smbpasswd -a {username}"

        # Запускаем команду через subprocess
        subprocess.run(command, input=password, text=True, check=True, shell=True)

        print(f"Пользователь {username} успешно создан в Samba.")
    except subprocess.CalledProcessError as err:
        print(f"Ошибка при создании пользователя в Samba: {err}")

def create_users():
    max_users = 2
    users_created = 0
    hour_limit = 1  # Создавать пользователей в течение 1 часа

    # Добавьте здесь ваш код для создания пользователя
    print(f"Максимальное количество пользователей которое надо создать:{max_users}. За какое время будем созвать пользователей:{hour_limit}")

    start_time = time.time()

    while users_created < max_users:
        # Генерируем уникальное имя пользователя, например, user_1, user_2, и так далее
        username = f"user_{users_created + 1}"
        password = "some_secure_password"

        # Создаем пользователя
        create_unix_user(username,password)
        create_samba_user(username, password)

        users_created += 1
        print(f"Создано пользователей: {users_created}/{max_users}")

        # Проверяем, прошло ли 1 час
        elapsed_time = time.time() - start_time
        if elapsed_time > hour_limit * 3600:
            print(f"Превышен лимит времени. Завершение создания пользователей.")
            break

    print("Создание пользователей завершено.")

# Запускаем создание пользователей
create_users()
