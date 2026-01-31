from flask import Flask
from stock_ticker.config import load_config
from stock_ticker.alpha_vantage import get_daily
from stock_ticker.prices import prices


def create_app():
    """
    Creates a Flask instace and manages the routes
    """
    config = load_config()

    app = Flask(__name__)

    @app.get("/")
    def get_daily_prices():
        # Aplpha vantage returns both the payload and a metadata dict. We only care about the payload in this case
        payload, _ = get_daily(symbol=config.symbol, api_key=config.api_key)
        daily_prices = prices(payload=payload, ndays=config.ndays)

        return daily_prices

    return app
