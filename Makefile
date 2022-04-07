
workspace ?= default

clean-venv:
	rm -rf .venv

gitreset: # Checkout master brance and pull
	git checkout master && git reset --hard origin/master && git pull

venv:
	@test -d .venv || python3 -m venv .venv
	@echo ""
	@echo "Virtual environment is created!"
	@echo "Now run this to activate it:"
	@echo ""
	@echo "source .venv/bin/activate"
	@echo ""

build_local: ## Run application on container locally with Proxy and Debug off
	docker-compose -f docker-compose-proxy.yml up

migrations_dev: # Run migrations locally
	python3 ./web_portal_project/manage.py makemigrations web_portal --settings=web_portal_settings.local_settings
	python3 ./web_portal_project/manage.py migrate --settings=web_portal_settings.local_settings

dev: ## Run application locally. No container
	python3 ./web_portal_project/manage.py runserver --settings=web_portal_settings.local_settings 0.0.0.0:8000

createsuperuser:
	python3 ./web_portal_project/manage.py createsuperuser --settings=web_portal_settings.local_settings

dev_test:
	cd ./web_portal_project/ && python3 manage.py test --settings=web_portal_settings.local_settings

shell:
	python3 ./web_portal_project/manage.py shell --settings=web_portal_settings.local_settings

terraform_init:
	docker-compose -f deploy/docker-compose.yml run --rm terraform init

terraform_plan:
	docker-compose -f deploy/docker-compose.yml run --rm terraform plan

terraform_apply:
	docker-compose -f deploy/docker-compose.yml run --rm terraform apply

terraform_validate:
	docker-compose -f deploy/docker-compose.yml run --rm terraform validate

terraform_fmt:
	docker-compose -f deploy/docker-compose.yml run --rm terraform fmt

terraform_destroy:
	docker-compose -f deploy/docker-compose.yml run --rm terraform destroy


terraform_workspace_list:
	docker-compose -f deploy/docker-compose.yml run --rm terraform workspace list

terraform_create_workspace:
	-docker-compose -f deploy/docker-compose.yml run --rm terraform workspace new dev
	-docker-compose -f deploy/docker-compose.yml run --rm terraform workspace new prod
	-docker-compose -f deploy/docker-compose.yml run --rm terraform workspace new staging

terraform_change_workspace:
	docker-compose -f deploy/docker-compose.yml run --rm terraform workspace select ${workspace}

docker_run:
	docker run --rm -it -p 0.0.0.0:8000:8000/tcp  -v ${PWD}:/project adrielt07/ubuntu18:latest /bin/bash