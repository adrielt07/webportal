# ctrl-layer-webpage


## Tools
- install [Docker](https://www.docker.com/products/docker-desktop)
- install [eb cli](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html)


## Run locally

- run `make migrations_dev` - run migrations locally using sqlite3
- run `make dev` run app locally using sqlite3
- go to [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)

## Run container local

- run `make build_local` create proxy container with staticfiles and run the app. Debug is Off
- go to [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) staticfile should be served by proxy


## Setup terraform
Initial setup on how to run terraform locally. We'll use docker-compose, so there's no need to install anything


Setup environment variables. Create a 'deploy/.env' file.
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- region=us-west-1


Run terraform init first
- installs the plugins
  - docker-compose -f deploy/docker-compose.yml run --rm terraform init 
  - make terraform_init

Create a workspace (dev, staging, prod)
- create a terraform workspace for dev, staging, prod (don't use prod for testing)
  - make terraform_create_workspace
  - docker-compose -f deploy/docker-compose.yml run --rm terraform workspace new <workspace_name>


## Pushing your changes using terraform

The name of the resources will be "${var.prefix}-${terraform.workspace}-< Some resource name >" Example: web_portal-dev-ubuntuserver

- var.prefix - You will be prompted to specify this when applying your change
- terraform.workspace - the name of the workspace you're using


**1. Change workspace to dev or default. You can create your own workspace, but this will create new resources (make sure to detroy it afterwards)**
  * ```make terraform_change_workspace workspace=dev ```
  * ```docker-compose -f deploy/docker-compose.yml run --rm terraform workspace select ${workspace} ```

**2. Run terraform validate and fmt**
  * Checks for incorrect syntax, resource, etc *
  * ```docker-compose -f deploy/docker-compose.yml run --rm terraform validate ```
  * ```make terraform_validate```

**3. fix the formatting and indentation**
  * ``` docker-compose -f deploy/docker-compose.yml run --rm terraform fmt ```
  * ``` make terraform_fmt ```

**4. Run terrafrom plan**
  * this will show the changes that you'll make to infrastructure. Run this first and validate
  * ``` docker-compose -f deploy/docker-compose.yml run --rm terraform plan ```
  * ``` make terraform_plan ```

(NOTE: you can use any prefix that you want for testing. But make sure to destroy it afterwards.)

**5. Apply your change**
  * this will push your change to infrastructure
  * ``` docker-compose -f deploy/docker-compose.yml run --rm terraform apply ```
  * ``` make terraform_apply ```

**6. Destroy your change**
  * Destroy the infrastructure. Do this if you have specified a different "var.prefix"
  * ``` docker-compose -f deploy/docker-compose.yml run --rm terraform destroy ```

