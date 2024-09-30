# <YOUR_IMPORTS>
import os
import pandas as pd
import dill
from pydantic import BaseModel
import json


def get_model(path_to_models):
    pkl_files = [f for f in os.listdir(path_to_models) if f.endswith('.pkl')]
    model_file_path = os.path.join(path_to_models, pkl_files[0])
    # print (model_file_path)

    with open(model_file_path, 'rb') as file:
        model = dill.load(file)
        # print (model)
        return model

def predict_tests(path_to_test, model):
    class Form(BaseModel):
        id: int
        url: str
        region: str
        region_url: str
        price: int
        year: float
        manufacturer: str
        model: str
        fuel: str
        odometer: float
        title_status: str
        transmission: str
        image_url: str
        description: str
        state: str
        lat: float
        long: float
        posting_date: str

    dictionary = {}
    for each in os.listdir(path_to_test):
        file_path = os.path.join(path_to_test, each)

        with open(file_path, 'r') as f:
            data = json.load(f)
            form_data = Form(**data)
            df = pd.DataFrame.from_dict([form_data.dict()])
            prediction = model.predict(df)
            dictionary[each] = prediction[0]

    # print (dictionary)
    return dictionary


def predict():
    # <YOUR_CODE>
    path = os.environ.get('PROJECT_PATH', '.')

    path_to_models = f'{path}/data/models'
    path_to_test = f'{path}/data/test'

    path_to_predictions = f'{path}/data/predictions'
    pred_file = f'{path_to_predictions}/result.csv'

    # print (os.listdir(path_to_models))
    # print (os.listdir(path_to_test))

    model = get_model(path_to_models)
    predictions = predict_tests(path_to_test, model)

    # print (predictions)
    preds_to_table = pd.DataFrame(list(predictions.items()), columns=['file_name', 'prediction'])
    preds_to_table.to_csv(pred_file, index=False)

if __name__ == '__main__':
    predict()
