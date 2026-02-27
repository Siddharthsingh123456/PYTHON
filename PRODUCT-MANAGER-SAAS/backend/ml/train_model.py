import pickle
from pathlib import Path


def train_and_save_dummy_model(path='ml/saved_models/price_model.pkl'):
    model = {'name': 'dummy-linear-model', 'version': '1.0'}
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open('wb') as f:
        pickle.dump(model, f)
    return out_path


if __name__ == '__main__':
    print(f'Saved model to {train_and_save_dummy_model()}')
