# Book Store Backend

Welcome to the backend repository for the Book Store application! This project serves as the backend infrastructure for managing the book store's inventory, handling user authentication, and facilitating order management. The backend is built using Django Rest Framework and deployed using Docker Compose.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Book Store backend provides a robust and secure API for interacting with the book store application. It handles tasks such as user authentication, book management, order processing, and more.

## Features

- **User Authentication**: Secure authentication mechanisms are implemented to ensure that only authorized users can access the application.
- **Book Management**: API endpoints are available for managing book listings, including adding new books, updating existing listings, and removing books from the inventory.
- **Order Processing**: Endpoints for managing orders, including viewing order details, updating order status, and handling order fulfillment.
- **Docker Compose**: Services are containerized using Docker Compose, allowing for easy deployment and scaling of the backend infrastructure.

## Installation

To set up the Book Store backend locally using Docker Compose, follow these steps:

1. Clone this repository:
`git clone https://github.com/sjdfani/book_store_backend.git`

2. Navigate to the `book_store_backend` directory:
`cd book_store_backend`

3. Create a `.env` file in the root directory and define environment variables as needed. Refer to `.env.example` for an example configuration.

4. Build and start the Docker containers:
`docker-compose up --build`

5. Once the containers are running, the backend services should be accessible at `http://127.0.0.1:8000`.

## Usage

Access the API endpoints using tools like Postman or integrate them into your frontend application. The documentation for the API endpoints can be found in the [API documentation](API_DOCUMENTATION.md).

## API Endpoints

The Book Store backend exposes the following API endpoints:

- **Books**: `/api/books/`
- **Carts**: `/api/cart/`
- **Users**: `/api/users/`

For detailed documentation on each endpoint and their usage, refer to the [API documentation](API_DOCUMENTATION.md).

## Contributing

Contributions to the Book Store backend are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the `main` branch of the original repository.

## License

This project is licensed under the [MIT License](LICENSE).

