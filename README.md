# Next Salah API

## Overview

Next Salah API is a simple and personal project designed to provide the next prayer time for Muslims.
This API calculates time left before the upcoming Salah (prayer) time based on the user's location.

## Features
- Retrieves all prayer times for a given day.
- Provides the next prayer time based on the user's location.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/usefmahmud/next-salah-api.git
    ```
2. Navigate to the project directory:
    ```bash
    cd next-salah-api
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI development server:
    ```bash
    uvicorn main:app --reload
    ```

## API Endpoints


### Get All Salah Times

#### `GET /all_salah`

Retrieves all prayer times for a given day based on the provided address.

**Parameters:**
- address: The address to get the prayer times for. Default is 'Cairo, Egypt'.
- date: The date to get the prayer times for. Default is today's date.

**Response:**
```json
[
    {
        "name": "Fajr",
        "time": "05:00"
    },
    {
        "name": "Dhuhr",
        "time": "12:00"
    },
    {
        "name": "Asr",
        "time": "15:00"
    },
    {
        "name": "Maghrib",
        "time": "18:00"
    },
    {
        "name": "Isha",
        "time": "20:00"
    }
]
```

### Get Next Salah Time

#### `GET /next_salah`

Retrieves the next prayer time based on the provided address.

**Parameters:**
- address: The address to get the next prayer time for. Default is 'Cairo, Egypt'.

**Response:**
```json
{
    "next": {
        "name": "Dhuhr",
        "time": "12:00"
    },
    "time_left": 3600
}
```