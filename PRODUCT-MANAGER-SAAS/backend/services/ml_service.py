from services.price_service import estimate_price


def predict_price(payload):
    features = payload.get('features', {})
    predicted = estimate_price(features)
    return {'predicted_price': predicted}, 200
