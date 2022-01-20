import twitter
from decouple import config


class RONBWrapper:
    def __init__(self):
        self.api = twitter.Api(
            consumer_key=config("TWITTER_API_KEY"),
            consumer_secret=config("TWITTER_API_KEY_SECRET"),
            access_token_key=config("TWITTER_ACCESS_TOKEN"),
            access_token_secret=config("TWITTER_ACCESS_TOKEN_SECRET"),
            tweet_mode="extended",
        )

    def get_updates(self, screen_name: str = "RONBupdates", count: int = 10) -> list:
        """Given a twitter username returns `count` number of tweets

        Args:
            screen_name (str, optional): Twitter username. Defaults to "RONBupdates".
            count (int, optional): Number of tweets to fetch. Defaults to 10.

        Returns:
            list: List of tweets
        """
        return self.api.GetUserTimeline(screen_name=screen_name, count=count)
