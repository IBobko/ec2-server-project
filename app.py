from flask import Flask, send_file

import pandas as pd

app = Flask(__name__)


@app.route('/api')
def api():
    return "10$"


@app.route('/')
def hello_world():
    df = pd.read_csv('data/gdp.cvs')
    fig = df.iloc[265, 4:64].astype(float).plot(figsize=(50, 30)).get_figure()
    fig.savefig('test.png')

    return send_file('test.png')


@app.route('/russia')
def gdp_russia():
    df = pd.read_csv('data/gdp.cvs')
    fig = df[df['Country Name'] == 'Russian Federation'].iloc[0, 32:64].astype(float).plot(figsize=(50, 30),
                                                                                           fontsize=30).get_figure()
    fig.savefig('russia.png')

    return send_file('russia.png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
