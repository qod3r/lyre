# Lyre
Приложение-эмулятор лиры с графическим интерфейсом и глобальным захватом клавиатуры

## Библиотеки
```
GUI - PyQt5
Звуки - pygame
Захват клавиатуры - keyboard
```

## Запуск
```
Скачать готовый .exe файл из Releases
```
или
```
git clone https://github.com/qod3r/lyre.git && cd lyre
git checkout sem
pip install -r requirements.txt
pyinstaller main.spec
запустить /dist/main.exe
```

## Использование
В главном окне можно загрузить текстовые файлы с нотами (поддерживается Drag-and-drop), либо включить плеер без них
![](https://i.imgur.com/vYE3tPH.png)
После добавления выбираем трек и нажимаем Play
![](https://i.imgur.com/hLumpUg.png)
В плеере будут показаны ноты, для приостановки захвата клавиатуры есть кнопка снизу, либо сочетание `LShift + RShift`
![](https://i.imgur.com/HaxgHzj.pngs)
