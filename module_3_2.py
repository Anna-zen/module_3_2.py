

# Домашняя работа по уроку "Способы вызова функции"
# Задача "Рассылка писем"


def send_email ( message, recipient,*, sender = "university.help@gmail.com") :
    if recipient == sender :
        print ("Нельзя отправить письмо самому себе!")
    elif ("@" in (recipient) and (".com" in (recipient) or ".ru" in (recipient)  or ".net" in (recipient))) :

        #print ("собачка и домен получателя верные ")
        if ("@" in (sender) and (".com" in (sender) or ".ru" in (sender) or ".net" in (sender))):

            #print ("собачка и домен отправителя верные")
            if sender == 'university.help@gmail.com' :
                print ('Письмо успешно отправлено с адреса: ', sender, 'на адрес: ',recipient)

            else :
                print ("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, " на адрес ", recipient)

        else :
           print ("Невозможно отправить письмо с адреса : ", sender, "на адрес", recipient)




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.net', sender = 'urban.teacher@mail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

