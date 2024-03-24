users = ('Ivan', 'Boris', 'Roman', 'Emil', 'Adel', 'Sergey', 'Rovlan', 'Masha')
objects = ('text_0.txt', 'text_1.txt','text_2.txt','text_3.txt','text_4.txt','text_5.txt',)
acsesses = ('Чтение', 'Права на запись', 'Полный доспуп', 'права на исполнение', 'Права на передачу прав')
def main():
        while True:
            user_input = input("Введите имя пользователя: ")
            if user_input in users:
                print("Привет," + user_input + '!')
                break
            else:
                print("Пользователь не найден")






if __name__ == '__main__':
    main() 
#matrix_of_acsess = { 
#                   'Ivan':{
#                           'text_0.txt':['Чтние']
#                           }, 
#                   }
#
#