"""

https://uneex.org/LecturesCMC/PythonIntro2021/Homework_BnopnyAnna

Примеры
Входные данные
…содержимое файла…

Результат работы
она. - Не говорите, пожалуйста, со мной про оперу, вы ничего не понимаете  в

"""


import sys

all_encodings = ['cp1026', 'cp1140', 'cp1256', 'cp273', 'cp437', 'cp500', 'cp775', 'cp850', 'cp852', 'cp855',
                 'cp857', 'cp860', 'cp861', 'cp862', 'cp863', 'cp865', 'cp866', 'gb18030', 'hp_roman8', 'iso8859_10',
                 'iso8859_11', 'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_16', 'iso8859_2', 'iso8859_4',
                 'iso8859_5', 'iso8859_9', 'koi8_r', 'mac_cyrillic', 'mac_greek', 'mac_latin2', 'mac_roman', 'utf_8']

basic_letters = {chr(c) for c in range(ord('а'), ord('я') + 1)}

all_chars = {'V', 's', 'ч', 'з', 'Ф', 'ь', 'T', 'B', 'X', ')', 'Щ', 'Э', 'ш', 'y', 'п', 'v', 'K', 'Я', 'г', '?',
             'О', 'Х', 'i', 'р', 'ж', 'Z', 'Г', 'л', 'e', '-', 'N', 'U', 'Ш', 'К', '(', 'Ж', 'Н', 'C', 'W', 'l',
             'u', 'D', 'S', 'к', '0', 'б', 'g', 'o', '!', 'c', 'Б', '3', 'q', 'ц', 'В', 'А', 'в', 'Д', '\n', 'M',
             'П', 'L', 'И', 'a', '7', 'J', 'O', 'H', 'х', 'w', 'м', 'P', ';', 'ф', 'З', 'Ю', 'и', 'Ц', 'й', '1',
             '8', 'f', ' ', 'я', 'о', 'У', 'k', 'Л', 'b', '5', '.', 'э', 'I', 'ъ', 'щ', 'p', '2', 'h', 'z', 'm',
             "'", 'n', 'x', 'r', 'М', 'Q', 'Т', 'а', 'н', 'Ч', 'д', 't', 'R', 'у', 'е', 'т', ':', 'd', ',', 'Е',
             'ы', 'С', 'ю', 'с', '4', 'E', '"', 'F', 'A', 'Y', '6', 'Р', 'j', '9'}

good_pairs = []


def get_good_pairs():
    global good_pairs
    check_str = "".join(basic_letters)
    for i in range(len(all_encodings)):
        for j in range(len(all_encodings)):
            if i == j:
                continue
            enc1 = all_encodings[i]
            enc2 = all_encodings[j]
            try:
                encoded_str = check_str.encode("utf_8")
                encoded_str = encoded_str.decode(enc1)
                encoded_str = encoded_str.encode(enc2)
                encoded_str = encoded_str.decode(enc2)
                encoded_str = encoded_str.encode(enc1)
                encoded_str = encoded_str.decode("utf_8")
            except Exception:
                continue
            else:
                if check_str == encoded_str:
                    good_pairs += [(enc2, enc1)]


def get_text(data, depth=0):
    try:
        text = data.decode("utf-8")
    except Exception:
        pass
    else:
        for el in text:
            if el not in all_chars:
                break
        else:
            print(text.split('\n')[0])
            exit(0)

    if depth > 2:
        return

    for enc1, enc2 in good_pairs:
        try:
            decoded_data = data.decode(enc1)
            encoded_data = decoded_data.encode(enc2)
        except Exception:
            pass
        else:
            get_text(encoded_data, depth + 1)


if __name__ == "__main__":
    get_good_pairs()
    input_data = sys.stdin.buffer.read().rstrip()
    get_text(input_data)