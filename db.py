import sqlite3  # Импорт модуля sqlite3 для работы с базой данных SQLite

from employee import Employee  # Импорт класса Employee из модуля employee
import time  # Импорт модуля time для замера времени
import random
import string


class Database:
    def __init__(self, db_name):
        # Инициализация и подключение к базе данных
        self.conn = sqlite3.connect(db_name)
        self.create_table()  # Создание таблицы при инициализации

    def create_table(self):
        # Создание таблицы сотрудников в базе данных
        with self.conn:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                full_name TEXT NOT NULL,
                dob TEXT NOT NULL,
                gender TEXT NOT NULL
            )
            """)

    def add_employee(self, employee):
        # Добавление нового сотрудника в базу данных
        with self.conn:
            self.conn.execute("INSERT INTO employees (full_name, dob, gender) VALUES (?, ?, ?)",
                              (employee.full_name, employee.dob, employee.gender))

    def get_all_employees(self):
        # Получение всех сотрудников из базы данных
        cursor = self.conn.execute("SELECT full_name, dob, gender FROM employees ORDER BY full_name")
        employees = []
        for row in cursor:
            # Убедимся, что все поля корректно обрабатываются
            full_name = row[0].strip()
            dob = row[1].strip()
            gender = row[2].strip()
            emp = Employee(full_name, dob, gender)
            employees.append(emp)
        return employees


    def fill_database(self):
        # Генерация случайных данных
        def random_name():
            return ''.join(random.choices(string.ascii_uppercase, k=5)) + ' ' + ''.join(random.choices(string.ascii_lowercase, k=7))

        def random_date():
            year = random.randint(1950, 2010)
            month = random.randint(1, 12)
            day = random.randint(1, 28)  # упрощенный вариант
            return f"{year:04d}-{month:02d}-{day:02d}"

        def random_gender():
            return random.choice(['Male', 'Female'])

        employees = [
            (random_name(), random_date(), random_gender())
            for _ in range(1000000)
        ]

        # Вставка данных пакетами
        with self.conn:
            self.conn.executemany("INSERT INTO employees (full_name, dob, gender) VALUES (?, ?, ?)", employees)

        # Добавление 100 записей с фамилией, начинающейся на "F"
        special_employees = [
            ('F' + ''.join(random.choices(string.ascii_lowercase, k=4)) + ' ' + ''.join(random.choices(string.ascii_lowercase, k=7)), random_date(), 'Male')
            for _ in range(100)
        ]
        with self.conn:
            self.conn.executemany("INSERT INTO employees (full_name, dob, gender) VALUES (?, ?, ?)", special_employees)

    def query_criteria(self):
        # Метод для выполнения запроса с критериями и замера времени выполнения
        start_time = time.time()  # Замер времени начала выполнения запроса
        cursor = self.conn.execute("SELECT * FROM employees WHERE gender='Male' AND full_name LIKE 'F%'")
        end_time = time.time()  # Замер времени окончания выполнения запроса
        duration = end_time - start_time  # Подсчет времени выполнения
        # Вывод результатов запроса и времени выполнения
        for row in cursor:
            print(row)
        print(f"Query executed in {duration} seconds.")
