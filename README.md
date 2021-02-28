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
