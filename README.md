# Flask MySQL Docker

A minimal Flask app that connects to a MySQL database and confirms the connection is working.

## What it does

Hits the `/` route, connects to MySQL, and returns the MySQL version if the connection succeeds — or the error message if it fails. Useful as a quick sanity check when setting up Flask + MySQL in a Dockerized environment.

## Requirements

- Python 3
- Flask
- mysql-connector-python
- A running MySQL instance (e.g. via Docker, reachable at host `mysql-db`)

## Environment Variables

| Variable              | Description                          | Default      |
|-----------------------|---------------------------------------|--------------|
| `MYSQL_ROOT_PASSWORD` | Password for the MySQL root user      | `secretpass` |

## Running Locally

\`\`\`bash
pip install flask mysql-connector-python
python app.py
\`\`\`

The app runs on `http://0.0.0.0:5000`.

## Running with Docker Compose

If using Docker Compose, make sure your MySQL service is named `mysql-db` and exposes a database called `testdb`, then start both services:

\`\`\`bash
docker-compose up
\`\`\`

Visit `http://localhost:5000` — you should see a success message with your MySQL version, or an error if the connection failed.

## Notes

- This is a learning/demo project, not production-ready (hardcoded credentials fallback, no input validation, etc.)
