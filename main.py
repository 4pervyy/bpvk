import time
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType

def write_msg(rand_int, user_id, message):
    vk.method('messages.send', {'user_id': user_id,
                                'message': message, 'random_id': rand_int})
token = "317b18daa2147a7c317990991cc9d81b3545666b5be9c8a5d98fdceea59c43902872186c4245b27a7216b"
vk = vk_api.VkApi(token=token)
vk._auth_token()
longpoll = VkLongPoll(vk)
print("Бот успешно запущен." )
api = vk.get_api()
while True:
    time.sleep(5)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                randint = random.randint(100000000, 900000000)
                request = request.lower()
                chat_id = vk.method('messages.getConversations')
                chat_id = chat_id['items']
                print(chat_id)

                for check in request:
                    if request == "привет":
                        name = api.users.get(user_ids = event.user_id.name)
                        write_msg(randint, event.user_id, "Привет,Я Секретарь 4. Чем могу быть полезен?(func)")
                    elif request == "func":
                        write_msg(randint, event.user_id, "Время")
                    else:
                        write_msg(randint, event.user_id, "Повторите, не понял запроса.")
