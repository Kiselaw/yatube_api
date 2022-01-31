### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone 
```

```bash
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

Windows:

```bash
py -3 -m venv env
```

```bash
. venv/Scripts/activate 
```

```bash
py -m pip install --upgrade pip
```

macOS/Linux:

```bash
python3 -m venv .venv
```

```bash
source env/bin/activate
```

```bash
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Выполнить миграции:

Windows: 

```bash
py manage.py migrate
```

macOS/Linux:

```bash
python3 manage.py migrate
```

Запустить проект:

Windows:

```bash
py manage.py runserver
```

macOS/Linux:

```bash
python3 manage.py runserver
```