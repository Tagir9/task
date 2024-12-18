#"Способы вызова функции"

def send_email(message, recipient, sender = "university.help@gmail.com"):
    if not '@' in sender or not '@' in recipient or not "." in sender[-4:-2:] or not "." in recipient[-4:-2:]:
    #if not '@' in sender or not '@' in recipient or not sender.endswith('.ru') or not recipient.endswith('.ru') \
            #or not sender.endswith('.com') or not recipient.endswith('.com') or not sender.endswith('.net') \
            #or not recipient.endswith('.net') :
        print("Невозможно отправить письмо с адреса <", (sender), "> на адрес <", (recipient),">.")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе")
        return

    if sender != recipient:
        print("Письмо успешно отправлено с адреса <", (sender), "> на адрес <", (recipient),">.")
        return

    print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <", (sender), "> на адрес <", (recipient),">.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
#send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
#send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')