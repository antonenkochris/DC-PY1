import random
import string


def get_random_password(n=8, digits=True) -> str:
    abc_ = string.ascii_letters
    if digits:
        abc_ += string.digits
    return "".join(random.sample(abc_, n))


print(get_random_password())   # сюда можно подставить нужное кол-во символов для пароля (до 62]
