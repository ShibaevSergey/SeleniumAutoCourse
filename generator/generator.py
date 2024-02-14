import random
from datetime import date
from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()
subjects = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        age=random.randint(20, 90),
        gender_index=random.randint(1, 3),
        mobile_number=random.randint(1000000000, 9999999999),
        date_of_birth=date(random.randint(1950, 2023), random.randint(1, 12), random.randint(1, 28)).strftime('%d %B %Y'),
        subjects=subjects[random.randint(0, 13)],
        hobbie_index=random.randint(1, 3),
        salary=random.randint(50000, 100000),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )

def generated_file():
    path = fr'C:\Users\shibaev_SA\Desktop\{random.randint(1, 999)}.txt'
    with open(path, 'w+') as file:
        file.write(f'Рандомное число: {random.randint(1, 999)}')
    return path