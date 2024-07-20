from datetime import datetime  # Импорт класса datetime для работы с датами


class Employee:
    def __init__(self, full_name, dob, gender):
        self.full_name = full_name.strip()  # Полное имя сотрудника, убираем пробелы по краям
        self.dob = dob.strip()  # Дата рождения сотрудника, убираем пробелы по краям
        self.gender = gender.strip()  # Пол сотрудника, убираем пробелы по краям

    def __str__(self):
        age = self.calculate_age()  # Расчет возраста сотрудника
        return f"{self.full_name}, {self.dob}, {self.gender}, {age} years old"

    def calculate_age(self):
        try:
            # Преобразование строки даты в объект datetime
            birth_date = datetime.strptime(self.dob, '%Y-%m-%d')
            today = datetime.today()  # Получение текущей даты
            # Расчет возраста в полных годах
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age
        except ValueError as e:
            print(f"Error calculating age for {self.full_name}: {e}")
            return None
