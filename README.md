# MSMP-cloud-api

This repository contains the web API component for the Monitoring System for Massive PC (MSMP). It is designed to handle device reservations/locking/unlocking and is intended to be used in conjunction with the main MSMP project.

This API is built with Flask and is designed for easy deployment on platforms like Render.

**Note:** This project is currently in a developmental stage and uses in-memory data storage. This means that all reservation data will be lost when the application is restarted. This is suitable for development and testing, but not for a production environment.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [Set Reservation](#set-reservation)
  - [Get Reservation](#get-reservation)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python 3 and pip installed on your system.

### Installation

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/youzThomas/MSMP-cloud-api.git
    cd MSMP-cloud-api
    ```

2.  **Create a virtual environment (optional but recommended):**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running the Application

You can run the application using either the Flask development server or a Gunicorn server.

-   **Using Flask's development server:**

    ```sh
    flask run
    ```

    The API will then be available at `http://127.0.0.1:5000`.

-   **Using Gunicorn:**

    ```sh
    gunicorn app:app
    ```

    The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

The API provides two endpoints for managing device reservations.

### Set Reservation

-   **Endpoint:** `/set-reservation`
-   **Method:** `POST`
-   **Description:** Creates or updates a reservation for a device.
-   **Request Body:**

    ```json
    {
        "device_id": "some_unique_device_id",
        "start_time": "2024-01-01T10:00:00Z",
        "end_time": "2024-01-01T12:00:00Z",
        "credential": "user_credential_string"
    }
    ```

-   **Success Response:**

    -   **Code:** `200 OK`
    -   **Content:**

        ```json
        {
            "status": "saved"
        }
        ```

-   **Error Response:**

    -   **Code:** `400 Bad Request`
    -   **Content:**

        ```json
        {
            "error": "device_id required"
        }
        ```

### Get Reservation

-   **Endpoint:** `/get-reservation`
-   **Method:** `GET`
-   **Description:** Retrieves the reservation details for a specific device.
-   **Query Parameters:**
    -   `device_id`: The ID of the device to retrieve the reservation for.
-   **Example Request:**

    ```
    GET /get-reservation?device_id=some_unique_device_id
    ```

-   **Success Response:**

    -   **Code:** `200 OK`
    -   **Content:**

        ```json
        {
            "start_time": "2024-01-01T10:00:00Z",
            "end_time": "2024-01-01T12:00:00Z",
            "credential": "user_credential_string"
        }
        ```

-   **Error Response:**

    -   **Code:** `404 Not Found`
    -   **Content:**

        ```json
        {
            "error": "not found"
        }
        ```

## Deployment

This project is configured for deployment on Render. The `render.yaml` file in the root of the repository defines the service. You can deploy this application by creating a new Web Service on Render and pointing it to your fork of this repository.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.