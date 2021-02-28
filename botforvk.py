import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard

def write_message(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),'keyboard': key.get_keyboard()})


key = VkKeyboard(one_time=True)
key.add_button('Контакты')
key.add_line()
key.add_button('Официальная группа')
key.add_line()
key.add_button('Общая информация о ПГУТИ')
key.add_line()
key.add_button('Новости и мероприятия')

key.add_button('Режим работы')


token = maintoken

authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        reseived_message = event.text
        sender = event.user_id

        if reseived_message == "Контакты":
            write_message(sender, " vk.com/o.konyaeva (Руководитель ИТ-клуба)\n"
                                  " vk.com/idkypislonanukypi (Зам. руководителя ИТ-клуба)\n"
                                  " vk.com/raiimax (По вопросам сотрудничества)\n"
                                  " vk.com/rin_tyan1 (По вопросам рекламы/сотрудничества)\n"
                                  " e-mail: init.psuti@gmail.com")

        elif reseived_message == "Официальная группа":
            write_message(sender, " Ссылка на официальную группу IT клуба Университета Связи ПГУТИ:\n "
                                  "https://vk.com/itclub_psuti")

        elif reseived_message == "Общая информация о ПГУТИ":
            write_message(sender, "👇🏻 Тут находится общая информация об университете 👇🏻 \n "
                                  "https://samara.zoon.ru/education/povolzhskij_gosudarstvennyj_universitet_telekommunikatsij_i_informatiki_na_moskovskom_shosse/social/")

        elif reseived_message == "Новости и мероприятия":
            write_message(sender, " Можешь взять нужную тебе инфу по этой ссылке 🤓:\n "
                                  "https://itclub-psuti.vsite.biz/#wall-news")

        elif reseived_message == "Режим работы":
            write_message(sender, "Все что тебе нужно находится тут: https://disk.yandex.ru/i/2AnOlLJHLxImKQ")



        else:
            pass
