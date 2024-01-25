.PHONY: superuser
superuser:
	 poetry run python -m src.manage createsuperuser

.PHONY: install
install:
	poetry install

.PHONY: migrations
migrations:
	poetry run python -m src.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python -m src.manage migrate

.PHONY: run-server
run-server:
	poetry run python -m manage runserver 127.0.0.1:8000

.PHONY: check
check:
	poetry run python -m manage check

.PHONY: shell
shell:
	poetry run python -m src.manage shell

.PHONY: celery-windows
celery-windows:
	poetry run celery -A ic_system worker -l info -P eventlet

.PHONY: celery-windows_beat
celery-windows_beat:
	poetry run celery -A ic_system  beat -l info