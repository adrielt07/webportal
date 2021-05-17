
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
	./ctrl_web_portal_project/manage.py makemigrations web_portal --settings=ctrl_web_portal.local_settings
	./ctrl_web_portal_project/manage.py migrate --settings=ctrl_web_portal.local_settings

dev: ## Run application locally. No container
	./ctrl_web_portal_project/manage.py runserver --settings=ctrl_web_portal.local_settings

createsuperuser:
	./ctrl_web_portal_project/manage.py createsuperuser --settings=ctrl_web_portal.local_settings

dev_test:
	cd ./ctrl_web_portal_project/ && python3 manage.py test --settings=ctrl_web_portal.local_settings

shell:
	./ctrl_web_portal_project/manage.py shell --settings=ctrl_web_portal.local_settings

terraform_init:
	docker-compose -f deploy/docker-compose.yml run --rm terraform init
