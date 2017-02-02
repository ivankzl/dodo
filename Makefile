SETTINGS := dodo.settings.base
CHECK := check --settings=$(SETTINGS)
CONSOLE := shell --settings=$(SETTINGS)
CONSOLE_PLUS := shell_plus --settings=$(SETTINGS)
DBSHELL := dbshell --settings=$(SETTINGS)
DOCKER := docker-compose run app
DOCKER_ALL_CONTAINERS := docker ps -a -q
CONTAINER_DB := trac -p 5438 -h localhost -U trac


check:
		@echo 'Verificando...'
		@$(DOCKER) python manage.py $(CHECK)

up:
		@echo 'Iniciando docker compose...'
		@docker-compose up

build:
		@echo 'Reconstruyendo containers y e iniciando...'
		@docker-compose up --build

console:
		@echo 'Iniciando consola en container app...'
		@$(DOCKER) bash

stop:
		@echo 'Deteniendo docker compose...'
		@docker-compose stop

stopall:
		@echo 'Deteniendo todos los containers...'
		@docker stop `$(DOCKER_ALL_CONTAINERS)`


shell:
		@echo 'Iniciando shell de Django...'
		@$(DOCKER) python manage.py $(CONSOLE)

shell_plus:
		@echo 'Iniciando shell_plus de Django...'
		@$(DOCKER) python manage.py $(CONSOLE_PLUS)

dbshell:
		@echo 'Iniciando consola de db...'
		@psql $(CONTAINER_DB)
