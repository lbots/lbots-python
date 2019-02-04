# LBots Python Wrapper

The official wrapper for the [LBots.org API](https://lbots.org/api/docs)

## Usage

```python
from lbots import LBotsClient

MY_BOT_ID = 1234567
MY_LBOTS_TOKEN = "abcdef"

my_client = LBotsClient(MY_BOT_ID, MY_LBOTS_TOKEN)

# For an Asynchronous (asyncio) version, use LBotsAsyncClient instead,
# and await all functions shown below.

# Update your stats all at once...
my_guild_count = 10
my_client.update_stats(my_guild_count)

# ...or per shard.
my_shard_count = 2
my_shard_id = 1
my_client.update_stats(my_guild_count, my_shard_count, my_shard_id)

# Get the amount of favorites your bot has
my_client.favorite_count()

# Check if a user favorited your bot
target_user_id = 123123123
favorited, favorited_at_time = my_client.user_favorited(target_user_id)

# Invalidate your API token, in case it leaked.
my_client.invalidate()
```
