# ctrl-layer-webpage


#### Tools
- install [Docker](https://www.docker.com/products/docker-desktop)
- install [eb cli](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html)


#### Run locally

- run `make migrations_dev` - run migrations locally using sqlite3
- run `make dev` run app locally using sqlite3
- go to [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)

#### Run container local

- run `make build_local` create proxy container with staticfiles and run the app. Debug is Off
- go to [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) staticfile should be served by proxy


#### Running terraform
Setup environment variables. Create a 'deploy/.env' file.
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- region=us-west-1

Run terraform init
- docker-compose -f deploy/docker-compose.yml run --rm terraform init 
- make terraform_init
