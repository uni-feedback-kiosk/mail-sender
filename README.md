# mail-sender

Backend for sending mail. Connects to an SMTP server and sends the mail on request.

## How to

### Prerequisites

- Docker
- Docker compose

### Process

1. Clone the repo
2. Copy/Rename `.env.example` to `.env` and modify it to use your own settings
3. Run `docker compose up -d` to run containers in background

In result, you'll get the running API on the default address <http://localhost:8001>

Interactive docs (Swagger UI) will be available at <http://localhost:8001/docs>
