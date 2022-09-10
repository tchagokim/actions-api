build:
	docker-compose build
	
run:
	docker-compose up

stop:
	docker-compose stop

create:
	docker-compose run --rm -T actions-api bash -c "python create-action.py ${action}"