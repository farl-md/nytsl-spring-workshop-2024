default: local

local:
	docker-compose up --build

nginx: 
	docker-compose -f docker-compose.nginx.yml up --build

dev-cmd:
	docker exec -it arklet_minter /bin/bash

dev-psql:
	source docker/env.local && docker exec -it arklet_db psql -U "$$POSTGRES_USER" -d "$$POSTGRES_DB"