from flask import Flask, send_file

import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():
    df = pd.read_csv('data/gdp.cvs')
    fig = df.iloc[265, 4:64].astype(float).plot(figsize=(50, 30)).get_figure()
    fig.savefig('test.png')

    return send_file('test.png')


if __name__ == '__main__':
    app.run()
