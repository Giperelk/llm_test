init-config:
	sudo cp .env.example .env

run:
	sudo docker compose up --build

stop:
	sudo docker compose down
