init-config:
	cp .env.example .env

run:
	docker compose up --build -d

stop:
	docker compose down
