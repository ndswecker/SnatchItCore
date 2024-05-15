param(
    [switch]$lan
)

.venv\Scripts\activate

if ($lan) {
    python app\manage.py runserver 0.0.0.0:80
} else {
    python app\manage.py runserver localhost:80
}

