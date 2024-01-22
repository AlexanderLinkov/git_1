import webbrowser,time

url = input('Введите ссылку: ')

while True:
    try:
        dur = int(input('Время просмотра: '))
        break
    except:
        print('Введите время просмотра: ')

while True:
    try:
        wtc = int(input('Сколько просмотров сделать: '))
        break
    except:
        print('Введите кол-во просмотров: ')

for i in range(wtc):
    webbrowser.open_new(url)
    time.sleep(dur)