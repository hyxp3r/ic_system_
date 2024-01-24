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
	poetry run python -m src.manage runserver 127.0.0.1:8000

.PHONY: check
check:
	poetry run python -m src.manage check

.PHONY: shell
shell:
	poetry run python -m src.manage shell