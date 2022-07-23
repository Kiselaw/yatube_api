## Yatube API

The project allows users to get data from the Yatube project via API.

### Technologies

- Python 3.9.5
- Django
- Django REST framework

### Installation and launch

Clone the repository and go to it using the command line:

```bash
git clone 
```

```bash
cd api_final_yatube
```

Create and activate a virtual environment:

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

Install dependencies from a file requirements.txt:

```bash
pip install -r requirements.txt
```

Make migrations:

Windows: 

```bash
py manage.py migrate
```

macOS/Linux:

```bash
python3 manage.py migrate
```

Launch:

Windows:

```bash
py manage.py runserver
```

macOS/Linux:

```bash
python3 manage.py runserver
```

### API documentation

[Link to documentation in Redoc format](http://127.0.0.1:8000/redoc/)

### License

MIT
