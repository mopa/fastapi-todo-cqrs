# ToDo App with FastAPI & CQRS

This is a simple to-do application built using FastAPI and CQRS architectural pattern. The purpose of this project is purely educational, and it is not intended to be used in production.

## Requirements

- Docker
- Docker Compose

## Installation

- Clone this repository: `git clone https://github.com/mopa/fastapi-todo-cqrs.git`
- Navigate to the project directory: `cd fastapi-todo-cqrs`
- Build the Docker image: `make build`
- Run the Docker containers: `make start`
- Duplicate the `.env.example` to `.env` file and modify it with the data connection to your PostgreSQL database
- Run the first migration: `docker-compose run pythondev alembic upgrade head`
    - Other option is enter the docker container and run the command:
    - `docker exec -it todocqrs /bin/bash`
    - `alembic upgrade head`

## Usage

By default, when running the `make start` command, the application will be available at `http://localhost:8004`. You 
can also access the Swagger UI at `http://localhost:8004/docs` and stop the containers by running `make stop`.

## Roadmap

- [x] Add database migrations
- [x] `.env` file support
- [x] Add logging
- [ ] Separate in bounded contexts
- [ ] Separate by layers
- [ ] Add scripts for linting, formatting and sort imports
- [ ] Add unit tests
- [ ] Add integration tests
- [ ] Add end-to-end tests
- [ ] Add authentication
- [ ] Add authorization

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
