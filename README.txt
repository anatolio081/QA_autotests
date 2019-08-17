     Чтобы правильно запустить скрипт требуется
1)Склонировать репозиторий из гитахаба:
    git clone https://github.com/anatolio081/QA_autotests
2)Открыть директорию QA_autotests:
    cd QA_autotests
3)В терминале прописать параметры окружения:
    python3 -m venv env
4)В том же терминале активировать созданное окружение:
    source env/bin/activate
5)Обновить pip:
    pip install -U pip
6)Через обновленный pip установить зависимости:
    pip install -r requirements.txt
7)Дать права на исполнение тест-рана
    sudo chmod +x run.sh
5)Запустить тесты командой:
    ./run.sh
