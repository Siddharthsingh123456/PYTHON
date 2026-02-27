def estimate_price(features):
    base_price = float(features.get('base_price', 100))
    demand_index = float(features.get('demand_index', 1.0))
    competitor_delta = float(features.get('competitor_delta', 0.0))
    return round(base_price * demand_index + competitor_delta, 2)
