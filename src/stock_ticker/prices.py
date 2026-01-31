def prices(payload: str, ndays: int):
    """
    Manipulate a given payload to return the
    1. The prices per day for the last ndays
    2. The average closing price over ndays
    """
    # Alpha Vantage does not support returning a specified amount of days. Need to get the whole response and then limit it
    prices = []
    for date in sorted(payload.keys(), reverse=True)[:ndays]:
        prices.append(
            {
                "date": date,
                "open": float(payload[date]["1. open"]),
                "high": float(payload[date]["2. high"]),
                "low": float(payload[date]["3. low"]),
                "close": float(payload[date]["4. close"]),
            }
        )

    # Determine the average closing price over NDAYS
    average = sum(price["close"] for price in prices) / len(prices)

    return {"prices": prices, "average": average}
