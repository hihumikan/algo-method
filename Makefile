No = 1

up:
	docker-compose up -d

t:
	docker-compose run --rm python python scripts/run_test/run_test.py ${No}

g:
	docker-compose run --rm python python scripts/get_question/get_question.py ${No}
