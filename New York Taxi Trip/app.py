import numpy as np
import pickle
from flask import Flask, render_template, request, jsonify, url_for, redirect
from forms import trip_form
import pandas as pd
import numpy as np
#import folium

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e0b352bf843cc4d91df1453babbc2741'


model = pickle.load(open('rf_model_1.pkl', 'rb'))
#pca = pickle.load(open('pca_model.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def home():
    form = trip_form()
    return render_template('Home.html', form=form)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = trip_form()
    dict_data = request.form.to_dict()
    # df_test = pd.DataFrame(data=dict_data.values(), columns=['vendor_id', 'pickup_longitude', 'passenger_count'])
    test = pd.Series(data=dict_data)
    test.drop(labels='csrf_token', inplace=True)
    test['dt'] = pd.to_datetime(test['dt'])
    test['pickup_hour'] = test['dt'].hour
    test['pickup_day'] = test['dt'].dayofweek
    test['month'] = test['dt'].month
    test.drop(labels=['dt', 'submit'], inplace=True)
    X = pd.DataFrame(data=np.reshape(test.values,(1,10)),columns = test.index)
    X = X[['cab_vendor','no_of_passengers','pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude','store_and_fwd_flag', 'pickup_hour', 'pickup_day', 'month']]
    #X = pca.transform(df_test)
    y_pred = model.predict(X)
    y_pred = (int)(np.exp(y_pred[0]))
    return render_template('Home.html', form=form, predicted_result=f'Predicted trip duration is {y_pred} mins')


if __name__ == '__main__':
    app.run(debug=True)
