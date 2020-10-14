from fastapi import FastAPI, HTTPException
import redis

from services import fibonacci


app = FastAPI()
cache = redis.Redis(host='redis', port=6379)


@app.get("/fibonacci")
def service(from_idx: int, to_idx: int):

    if (from_idx < 0) or (to_idx < 0):
        raise HTTPException(status_code=400, detail="Indexes must be positive numbers")

    elif from_idx > to_idx:
        raise HTTPException(status_code=400, detail="to_idx cannot be less than from_idx")

    fibonacci_slice = [fibonacci(x, cache) for x in range(from_idx, to_idx+1)]
    return {"fibonacci_slice": fibonacci_slice}
