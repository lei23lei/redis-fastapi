import redis
from fastapi import FastAPI
import uvicorn

# Redis connection
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Redis FastAPI!"}

@app.get("/health")
async def health():
    try:
        redis_client.ping()
        return {"status": "Redis connected"}
    except:
        return {"status": "Redis not connected"}

@app.get("/test")
async def test():
    try:
        # Set a test key
        redis_client.set("test_key", "Hello Redis!")
        # Get the test key
        value = redis_client.get("test_key")
        return {"message": f"Redis test successful: {value}"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
