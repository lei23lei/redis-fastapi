# Redis FastAPI Test Server

A FastAPI application to test Redis connectivity through nginx proxy.

## Features

- Redis health check endpoint
- Redis server information
- Key-value operations (set, get, delete)
- List all Redis keys
- Comprehensive test operations
- nginx proxy support with proper headers

## Setup

1. Install dependencies:

```bash
uv sync
```

2. Make sure Redis is running on your system:

```bash
redis-server
```

3. Start the FastAPI server:

```bash
uv run python main.py
```

The server will run on `http://127.0.0.1:8000`

## nginx Configuration

Your nginx configuration should proxy requests to the FastAPI server:

```nginx
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## API Endpoints

- `GET /` - Home page with API documentation
- `GET /health` - Redis health check
- `GET /redis/info` - Redis server information
- `POST /redis/set` - Set key-value pair
- `GET /redis/get/{key}` - Get value by key
- `DELETE /redis/delete/{key}` - Delete key
- `GET /redis/keys` - List all keys
- `GET /redis/test` - Test Redis operations

## Environment Variables

- `REDIS_HOST` - Redis host (default: localhost)
- `REDIS_PORT` - Redis port (default: 6379)
- `REDIS_DB` - Redis database (default: 0)

## Testing

1. Access the home page at `http://localhost/` (through nginx) or `http://127.0.0.1:8000/` (direct)
2. Test Redis connectivity at `/health`
3. View Redis information at `/redis/info`
4. Test Redis operations at `/redis/test`
# redis-fastapi
