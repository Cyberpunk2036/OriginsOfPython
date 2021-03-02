# Первое задание
class Date:
    def __init__(self, text):
        self.text = text
        
    @classmethod
    def extractor(cls, txt):
        try:
            cls.text = [int(i) for i in txt.split("-")] #Основное предстваление
        except TypeError:
            print("Неверный формат ввода!")
        else:
            print(".".join(map(lambda x: str(x), cls.text))) #Чтоб красивее было
            return cls.text
    
    @staticmethod
    def validation(date):
        if date[0] > 31:
            print("Номер месяца выходит за пределы 31 дня!")
            return False
        if date[1] > 12:
            print("Число месяца выходит за предел 12 месяцев! ")
            return False
            

Date.validation((Date.extractor("27-06-2021")))