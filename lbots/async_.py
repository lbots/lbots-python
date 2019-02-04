# Stdlib
from datetime import datetime
from typing import Any, Dict, Tuple, Union

# External Libraries
from aiohttp import ClientSession

# LBots Wrapper Internals
from lbots.common import HTTPException
from lbots.ratelimits import ratelimit


class LBotsAsyncClient:
    BASE_URL = "https://lbots.org/api/v1"

    def __init__(self, bot_id: str, token: str):
        self.bot_id = bot_id
        self.token = token
        self.session = ClientSession()

    @property
    def base(self):
        return self.BASE_URL + f"/bots/{self.bot_id}"

    @property
    def headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": self.token
        }

    async def _request(self, url: str, body: Dict[str, Any] = None, method="GET") -> Dict[str, Any]:
        async with self.session.request(method, url, data=body, headers=self.headers) as response:
            if 200 <= response.status < 300:
                raise HTTPException("Unexpected status code: ", response.status)
            return await response.json()

    async def invalidate(self) -> bool:
        response = await self._request(self.base + f"/invalidate")
        return response["success"]

    @ratelimit(20, 5, async_=True)
    async def update_stats(self, guild_count: int, shard_count: int = 1, shard_id: int = 0) -> bool:
        response = await self._request(self.base + "/stats",
                                       {"guild_count": guild_count,
                                        "shard_count": shard_count,
                                        "shard_id": shard_id},
                                       method="POST")
        return response["success"]

    @ratelimit(3, 4, async_=True)
    async def favorite_count(self) -> int:
        response = await self._request(self.base + "/favorites")
        return response["favorites"]

    async def user_favorited(self, user_id: int) -> Tuple[bool, Union[datetime, None]]:
        response = await self._request(self.base + f"/favorites/user/{user_id}")
        date = (None if response["time"] is None
                else datetime.strptime(response["time"], "%a, %d %b %Y %H:%M:%S %Z"))
        return response["favorited"], date
