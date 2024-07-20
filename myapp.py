import argparse  # Импорт модуля argparse для обработки аргументов командной строки

from db import Database  # Импорт класса Database из модуля db
from employee import Employee  # Импорт класса Employee из модуля employee


def main():
    parser = argparse.ArgumentParser(description="Employee Directory Application")
    parser.add_argument('mode', type=int, help='Mode of the application')
    parser.add_argument('args', nargs='*', help='Arguments for the specified mode')

    args = parser.parse_args()
    mode = args.mode

    db = Database('employees.db')

    if mode == 1:
        db.create_table()
    elif mode == 2:
        if len(args.args) != 3:
            print("Invalid arguments. Usage: myApp 2 'Full Name' YYYY-MM-DD Gender")
            return
        full_name, dob, gender = args.args
        employee = Employee(full_name, dob, gender)
        db.add_employee(employee)
    elif mode == 3:
        employees = db.get_all_employees()
        for emp in employees:
            print(emp)
    elif mode == 4:
        db.fill_database()
    elif mode == 5:
        db.query_criteria()
    else:
        print("Invalid mode specified.")


if __name__ == "__main__":
    main()  # Вызов функции main при запуске скрипта
