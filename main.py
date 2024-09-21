#систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.

#Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
class User:
    def __init__(self, staff_id, name, access_level = 'user'):
        self.__staff_id = staff_id
        self.__name = name
        self.__access_level = access_level

    def users_getter(self):
        info = {"id" : self.__staff_id, "name" : self.__name, "access_level" : self.__access_level}
        print(info)

    def users_setter(self, staff_id, name):
        self.__staff_id = staff_id
        self.__name = name

#Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
class Admin(User):
    def __init__(self, staff_id, name, access_level = 'admin'):
        super().__init__(staff_id, name, access_level)

    def users_getter(self):
        super().users_getter()

    def users_setter(self, staff_id, name):
        super().users_setter(staff_id, name)

# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка
# (представь, что это просто список экземпляров User).
    def add_user(self, person):
        all_stuff_list.append(person)

    def remove_user(self, person):
        all_stuff_list.remove(person)

#Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).
user1 = User(1, "Derry")              #создали юзера
admin1 = Admin(77777777777, "Marie")   #создали админа
admin1.users_getter()                 #вывод данных
user1.users_getter()                 #вывод данных
admin1.users_setter(222, "Ivan")    #замена данных
user1.users_setter(333, "Ivan")    #замена данных
admin1.users_getter()                #вывод изменненных данных
user1.users_getter()                #вывод изменненных данных

all_stuff_list = []
admin1.add_user(user1)  #функция добавления
admin1.add_user(user1)  #функция добавления
admin1.add_user(admin1)  #функция добавления
print(all_stuff_list)
admin1.remove_user(user1)  #удаление лишней записи
print(all_stuff_list)
