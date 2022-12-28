# Lyre
Приложение-эмулятор лиры с графическим интерфейсом и глобальным захватом клавиатуры

## Библиотеки
GUI - PyQt5\
Звуки - pygame\
Захват клавиатуры - keyboard

## Запуск
`Скачать готовый .exe файл из Releases` \
или
1. `git clone https://github.com/qod3r/lyre.git && cd lyre`
2. `git branch sem`
3. `pip install -r requirements.txt`
4. `pyinstaller main.spec`

## Использование
В главном окне можно загрузить текстовые файлы с нотами (поддерживается Drag-and-drop), либо включить плеер без них
![](https://i.imgur.com/vYE3tPH.png)
После добавления выбираем трек и нажимаем Play
![](https://i.imgur.com/hLumpUg.png)
В плеере будут показаны ноты, для приостановки захвата клавиатуры есть кнопка снизу, либо сочетание `LShift + RShift`
![](https://i.imgur.com/HaxgHzj.pngs)
