from stock_ticker.prices import prices
from .fixtures import FAKE_PAYLOAD


def test_prices_for_2_days():
    """
    Test that prices() pulls the correct average for the previous two days
    """

    result = prices(FAKE_PAYLOAD, ndays=2)

    assert len(result["prices"]) == 2
    assert result["average"] == float(450)
