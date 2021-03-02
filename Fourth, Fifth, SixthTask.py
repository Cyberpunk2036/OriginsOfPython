# Четвертое, пятое, шестое задания
class MyExceptions(Exception):
    def __init__(self, text):
        self.text = text

class StoreHouse:
    def __init__(self, destination="Конкретный склад", department="Подразделение компании", nums="Количество", goods='товар'):
        self.goods = goods
        self.diction = {"Информация о товаре":goods.information(), "Склад":destination, "Подразделение":department, "Количество":nums}
        
    @staticmethod   
    def validation(diction):
        """Проверяет соответствие поля 'Количество' числовому типу данных"""
        for k, v in diction.items():
            if k != "Информация о товаре":
                if k == "Количество":
                    try:
                        v = int(v)
                    except ValueError:
                        raise MyExceptions("В поле 'Количество' вы ввели нечисловой тип данных")
                    except MyExceptions as err:
                        print(err)
        
    def all_information(self):
        """Выводит всю информацию о товаре и партии"""
        for k, v in self.diction.items():
            if k != "Информация о товаре":
                print(f"{k}: {v}")
            else:
                for kk, vv in self.diction["Информация о товаре"].items():
                    print(f"{kk}: {vv}")
        print()
   

class OrgTech:
    def __init__(self, name="Наименование", manufacter="Производитель", ident="Уникальный номер"):
        self.name = name
        self.manufacter = manufacter
        self.ident = ident


class Printer(OrgTech):
    def __init__(self, name, manufacter, ident, type_pr="Тип принтера", colors=False):
        super().__init__(name, manufacter, ident)
        self.type_pr = type_pr
        self.colors = colors
        
    def information(self):
        """Создает инфомационный словарь товара"""
        self.ddd = {"Наименование": self.name,"Производитель": self.manufacter, "Уникальный номер":self.ident, "Тип принтера":self.type_pr, "Цветной":self.colors}
        # print(f"Информация о принтере:\nНаименование: {self.name}\nПроизводитель: {self.manufacter}\n"
        #       f"Уникальный номер: {self.ident}\nТип принтера: {self.type_pr}\nЦветной: {self.colors}\n")
        return self.ddd
    
    
class Scaner(OrgTech):
    def __init__(self, name, manufacter, ident, type_sc="Тип сканера", form_sc="Вид сканера"):
        super().__init__(name, manufacter, ident)
        self.type_sc = type_sc
        self.form_sc = form_sc
        
    def information(self):
        self.ddd = {"Наименование": self.name,"Производитель": self.manufacter, "Уникальный номер":self.ident, "Тип сканера":self.type_sc, "Вид сканера":self.form_sc}
        # print(f"Информация о сканере:\nНаименование: {self.name}\nПроизводитель: {self.manufacter}\n"
        #       f"Уникальный номер: {self.ident}\nТип сканера: {self.type_sc}\nВид сканера: {self.form_sc}\n")
        return self.ddd


class Xerox(OrgTech):
    def __init__(self, name, manufacter, ident, main_class="Тип ксерокса"):
        super().__init__(name, manufacter, ident)
        self.main_class = main_class
        
    def information(self):
        self.ddd = {"Наименование": self.name,"Производитель": self.manufacter, "Уникальный номер":self.ident, "Тип ксерокса":self.main_class}
        # print(f"Информация о ксероксе:\nНаименование: {self.name}\nПроизводитель: {self.manufacter}\n"
        #       f"Уникальный номер: {self.ident}\nТип ксерокса: {self.main_class}\n")
        return self.ddd


a = StoreHouse("Москва №21", "Аналитическое", "32", Printer("XP Printer 2000", "Microsoft", "pr#1192331", "Лазерный", True)) # Ввод данных
a.validation(a.diction)  # Проверка на соответствие типа
a.all_information() # Вывод полной информации
b = StoreHouse("Москва №1", "Аналитическое", "12", Scaner("ASP 12NS", "HP", "sc#12331", "Сканер изображений", "Ручной сканер"))
b.validation(b.diction)
b.all_information()
c = StoreHouse("Москва №21", "Маркетинга", "7", Xerox("EcoSys NZ-2001", "EcoSys", "x#23123", "Монохромный"))
c.validation(c.diction)
c.all_information()
