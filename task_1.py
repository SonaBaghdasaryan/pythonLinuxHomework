# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и
# False в противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно.


# import subprocess
#
#
# def func(command, text):
#     result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
#     out = result.stdout
#     print(out)
#     if result.returncode == 0:
#         if text in out:
#             return True
#         else:
#             return False
#     else:
#         print("FAIL! CODE !=0")
#
#
# if __name__ == "__main__":
#     my_command = "ls -la"
#     my_text = "ta"
#
#     print(func(my_command, my_text))
#


# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился
# дополнительный режим работы, в котором вывод разбивается на слова с удалением всех
# знаков пунктуации (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.


import subprocess
import re

def check_word(command, text, mode='default'):
    try:
        output = subprocess.check_output(command, shell=True).decode()
        output_words = re.findall(r'\w+', output.lower())
        if mode == 'default':
            if text in output:
                return True
            else:
                return False
        elif mode == 'word':
            text_words = text.split()
            for word in text_words:
                word = word.lower()
                if word not in output_words:
                    return False
            return True
    except subprocess.CalledProcessError:
        return False


command = "echo 'Love all, trust a few, do wrong to none!'"
text = "wrong to none"
result = check_word(command, text, mode='word')
print(result)