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

## Usage

By default, when running the `make start` command, the application will be available at `http://localhost:8004`. You 
can also access the Swagger UI at `http://localhost:8004/docs` and stop the containers by running `make stop`.

## Roadmap

- [ ] Add database migrations
- [ ] Add logging
- [ ] `.env` file support
- [ ] Add unit tests
- [ ] Add integration tests
- [ ] Add end-to-end tests
- [ ] Add authentication
- [ ] Add authorization

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.