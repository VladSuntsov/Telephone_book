import os


class TelephoneBook:
    def __init__(self,
                 second_name: str,
                 first_name: str,
                 sur_name: str,
                 organization: str,
                 telephone_work: int,
                 telephone_you: int
                 ):
        self.second_name = second_name
        self.first_name = first_name
        self.sur_name = sur_name
        self.organization = organization
        self.telephone_work = telephone_work
        self.telephone_you = telephone_you

    def build_note(self):
        with open(f"{self.second_name + self.first_name}.txt", "w", encoding="utf-8") as file:
            file.write(self.second_name + self.first_name)
        print(f"Контакт {self.second_name + self.first_name} создан!")

    def create_note(self):
        second_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        sur_name = input('Введите отчество: ')
        organization = input('Введите название организации: ')
        telephone_work = input('Введите номер телефона личный: ')
        telephone_you = input('Введите номер рабочий: ')
        return self.build_note()

    def read_note(self):
        second_name = input("Введите фамилию: ")
        if os.path.isfile(second_name):
            with open(second_name, 'r') as file:
                contens = file.read()
            print(contens)
        else:
            print('Контакт не найден')

    def edit_note(self):
        second_name = input("Введите фамилию: ")
        if os.path.isfile(second_name):
            with open(second_name, 'r') as file:
                contens = file.read()
                print(contens)
            new_contens = input('Введите фамилию: ')
            with open(second_name, 'w') as file:
                file.write(new_contens)
        else:
            print('Контакт не найден')

    def delete_note(self):
        second_name = input("Введите фамилию: ")
        if os.path.isfile(second_name):
            os.remove(second_name)
        else:
            print('Контакт не найден')

    def __str__(self):
        with open(f"{self.second_name + self.first_name}.txt", "r") as file:
            lst_page = file.read().splitlines()
        return f'{lst_page}'


contact = TelephoneBook()
print(contact.create_note())
