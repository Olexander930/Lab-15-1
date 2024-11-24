import pandas as pd

# Початковий словник учнів
students = {
    "Vitaly_Prikhodko": 203,
    "Dmytro_Kropyvnytskyi": 196,
    "Mikhail_Romanenko": 193,
    "Maxim_Derizemlya": 188,
    "Victoria_Zhuk": 182,
    "Andrey_Kuryanov": 177,
    "Oksana_Dubovets": 175,
    "Nikita_Stroganov": 173,
    "Karina_Nikolaenko": 169,
    "Eugenia_Dron": 167
}

# Функція перетворення словника на датафрейм
def create_dataframe(students_dict):
    return pd.DataFrame(list(students_dict.items()), columns=['Surname', 'Height'])

# Додавання нового учня
def add_student(df_students, surname, height):
    new_student = {"Surname": surname, "Height": height}
    return pd.concat([df_students, pd.DataFrame([new_student])], ignore_index=True)

# Видалення учня
def remove_student(df_students, surname):
    if surname in df_students['Surname'].values:
        df_students = df_students[df_students['Surname'] != surname].reset_index(drop=True)
        print(f"Учень {surname} видалений.")
    else:
        print(f"Учня з прізвищем {surname} не знайдено.")
    return df_students

# Агрегація даних
def aggregate_data(df_students):
    return df_students.agg({'Height': ['mean', 'min', 'max']}).rename(columns={'Height': 'Value'})

# Групування за інтервалами
def group_by_height(df_students):
    bins = [150, 170, 190, 210]
    labels = ['150-170', '171-190', '191-210']
    df_students['Height_Group'] = pd.cut(df_students['Height'], bins=bins, labels=labels, right=True)
    return df_students.groupby('Height_Group', observed=False).size().reset_index(name='Count')

# Меню для користувача
def menu():
    df_students = create_dataframe(students)
    while True:
        print("\nМеню:")
        print("1. Показати список учнів")
        print("2. Додати нового учня")
        print("3. Видалити учня")
        print("4. Показати агрегацію даних")
        print("5. Групування за інтервалами зросту")
        print("6. Вийти")

        choice = input("Виберіть дію (1-6): ")

        if choice == '1':
            print("\nСписок учнів:")
            print(df_students)

        elif choice == '2':
            surname = input("Введіть прізвище нового учня: ")
            try:
                height = int(input("Введіть зріст нового учня (в см): "))
                df_students = add_student(df_students, surname, height)
                print(f"Учень {surname} доданий.")
            except ValueError:
                print("Некоректне значення зросту. Спробуйте ще раз.")

        elif choice == '3':
            surname = input("Введіть прізвище учня для видалення: ")
            df_students = remove_student(df_students, surname)

        elif choice == '4':
            print("\nАгрегація даних:")
            print(aggregate_data(df_students))

        elif choice == '5':
            print("\nГрупування учнів за інтервалами зросту:")
            print(group_by_height(df_students))

        elif choice == '6':
            print("Вихід із програми.")
            break

        else:
            print("Некоректний вибір. Спробуйте ще раз.")

# Запуск програми
if __name__ == "__main__":
    menu()