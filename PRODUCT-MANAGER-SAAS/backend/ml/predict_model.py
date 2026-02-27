import pickle


MODEL_PATH = 'ml/saved_models/price_model.pkl'


def load_model(path=MODEL_PATH):
    with open(path, 'rb') as f:
        return pickle.load(f)


def predict(features, path=MODEL_PATH):
    _ = load_model(path)
    return round(float(features.get('base_price', 100)) * 1.03, 2)
