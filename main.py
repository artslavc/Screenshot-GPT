# -> Сторонние Библиотеки
import sys
from PIL import ImageGrab, Image
import pytesseract
# -> Скрипты
from gpt_engine import neiro_zapros

# sudo apt install tesseract-ocr-[lang]

type_gpt = 0

def choose_gpt():
    global type_gpt
    
    print('Выберите режим:\n'
      '1. Пересказ\n'
      '2. Выбрать Ответ\n'
      '3. Перевод\n'
      '4. Решение Задачи\n'
      '5. Взять Текст\n'
      '6. Развернутый Ответ')
    while True:
        try:
            type_gpt = int(input('[*] #: '))
            break
        except ValueError:
            pass
    if type_gpt == 1: type_gpt = 'Перескажи Текст Кратко или что ты видишь имея текст'
    elif type_gpt == 2: type_gpt = 'Выбери ответ одним словом без лишнего. Перепроверь себя.'
    elif type_gpt == 3: type_gpt = 'Переведи Текст'
    elif type_gpt == 4: type_gpt = 'Реши Задачу. Ответ напиши одной цифрой или одним словом в зависимости от задачи. Перепроверь себя.'
    elif type_gpt == 5: type_gpt = 'Взять Текст'
    elif type_gpt == 6: type_gpt = 'Напиши решение для задачи'
    else: print('[-] Ошибка!'); sys.exit(0)

choose_gpt()

while True:
    yr = input('[*] Вы сохранили фото в буфер обмена? [y/n] #: ')

    if yr == 'y' or yr == 'yes':
        print('[+] Подгружаю фото...')
        im = ImageGrab.grabclipboard()

        print('[+] Разделяю текст и картинку...')
        text = pytesseract.image_to_string(im, lang='all', config=r'--oem 3 --psm 6 -l eng+rus')
        if type_gpt == 'Взять Текст': # Нейросеть Обрабатывает
            print(text)
        else:
            print(f'[+] Ответ от нейросети: \n'
                  f'{neiro_zapros(text, type_gpt)}')
    elif yr == 'n' or yr == 'no':
        choose_gpt()
    else:
        print(':) Bye-Bye!')
        sys.exit(0)