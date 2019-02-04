# Stdlib
import asyncio
from functools import wraps
import time
from typing import Callable

# External Libraries
from ratelimit import RateLimitException, limits


def ratelimit(requests: int, seconds: int, async_: bool = False) -> Callable[[Callable], Callable]:
    def decorator(func: Callable) -> Callable:

        limited = limits(calls=requests, period=seconds)(func)

        if async_:
            @wraps(func)
            async def inner(*args, **kwargs):
                while True:
                    try:
                        return await limited(*args, **kwargs)
                    except RateLimitException:
                        await asyncio.sleep(1)
        else:
            @wraps(func)
            def inner(*args, **kwargs):
                while True:
                    try:
                        return limited(*args, **kwargs)
                    except RateLimitException:
                        time.sleep(1)
        return inner
    return decorator
