from alpha_vantage.timeseries import TimeSeries


def get_daily(symbol: str, api_key: str):
    """
    Get the daily records for a specific stock
    """
    ts = TimeSeries(key=api_key, output_format="json")

    # TO-DO: Aplha Vantage free keys are rate limited to 25 requests per day. Need to handle this use case
    # TO-DO: If you pass in an invalid symbol, Alpha Vantage returns a 200 with all values except the dates being 0.0001. Need to validate that the symbol being passed in is actually valid
    payload = ts.get_daily(symbol=symbol, outputsize="compact")
    return payload
