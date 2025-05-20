# Bill Tracker

Django Project for tracking bill votes

## Prerequisites

Make sure you have the following software installed on your system:

[Docker](https://www.docker.com/)

[Docker Compose](https://docs.docker.com/compose/)

## Running with Docker

**1. Build the image**
```
docker-compose build
```
This should:
- Install project dependencies
- Apply database migrations
- Load initial data
- Start Django server
  
2. Start the container
```
docker-compose up
```
3. access it through the following url:
```
http://localhost:8000/
```

Stopping container:
```
docker-compose down
```
