import os
from dataclasses import dataclass


@dataclass
class Config:
    api_key: str
    symbol: str
    ndays: int


def load_config():
    """
    Loads the required configuration from environment variables
    """

    # Validate that the correct env variables have been set. Fail otherwise
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Need to set an environment variable for ALPHA_VANTAGE_API_KEY"
        )

    symbol = os.getenv("SYMBOL")
    if not symbol:
        raise RuntimeError("Need to set an environment variable for SYMBOL")

    # TO_DO: validate that NDAYS is greater than 1 but less than 100 and NDAYS is an int
    ndays = int(os.getenv("NDAYS"))
    if not ndays:
        raise RuntimeError("Need to set an environment variable for NDAYS")

    return Config(api_key, symbol, ndays)
