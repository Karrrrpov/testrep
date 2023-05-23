import time

def watch_time(func):
    def checktime(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        checktime.execution_time = execution_time
        return result
    return checktime
@watch_time
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

result = factorial(5)
execution_time = factorial.execution_time

print("Ответ:", result)
print("время работы программы:", execution_time)


# #
# # #!!!!!!!Пример декоратора с запуском (сделать также)!!!!!!!!
# # # def combine_decs(*decs):
# # #     def deco(f):
# # #         for dec in decs:
# # #             f = dec(f)
# # #         return f
# # #
# # #     return deco
# # #
# # # @allure.title('Пакеты размещений. Проверка публикации объявления с мульти из пакета на публикацию')
# # #     def test_79210_buy_package_commercial_and_published_multilisting(self):
# #
# # #new
# # #ДОМАШКА ПОВЫШЕННАЯ СЛОЖНОСТЬ
# #
# class Person:
#     def __init__(self, firstName, lastName, mail, phone, workplace):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.mail = mail
#         self.phone = phone
#         self.workplace = workplace
#
#     def __str__(self):
#         return f"{self.firstName} {self.lastName}, email: {self.mail}, phone: {self.phone}, workplace: {self.workplace}"
#
# class AddressBook:
#     def __init__(self):
#         self.people = []
#
#     def add_person(self, person):
#         self.people.append(person)
#
#     def delete_person(self, person):
#         self.people.remove(person)
#
#     def show_people(self):
#         if len(self.people) == 0:
#             print("Такого нет")
#         else:
#             for person in self.people:
#                 print(person)
#     def save_to_file(self, filename):
#         with open(filename, 'w') as f:
#             for person in self.people:
#                 f.write(f"{person.firstName};{person.lastName};{person.mail};{person.phone};{person.workplace}\n")
#
#     def load_from_file(self, filename):
#         self.people = []
#         with open(filename, 'r') as f:
#             for line in f:
#                 firstName, lastName, mail, phone, workplace = line.strip().split(';')
#                 person = Person(firstName, lastName, mail, phone, workplace)
#                 self.add_person(person)
#
#                 # @contextmanager
#                 # def processor():
#                 #     print('--> start processing')
#                 #     yield
#                 #     print('<-- stop processing')
#
# # book = AddressBook()
# #
# # person1 = Person("Тест", "Тестович", "test@mail.ru", "88005553535", "ЦИАН")
# # person2 = Person("Боб", "Марли", "bob@gmail.com", "87654563211", "Авито")
# #
# # book.add_person(person1)
# # book.add_person(person2)
#
# # book.show_people()
# #
# # book.delete_person(person1)
#
# # book.show_people()
# #
# # book.save_to_file('people.txt')
# newBook = AddressBook()
# newBook.load_from_file('people.txt')
# newBook.show_people()
# #
# # book.show_people()
