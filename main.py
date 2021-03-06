  
from flask import Flask
from flask import jsonify
import pandas as pd
import logging
#import wikipedia

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World! I like making AI apps!!'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is my glorious Hello World page</title>
    <p>Hello<?/>
    <p><b>World</b></p>
    """

@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

@app.route('/bob')
def bob():
    val = {"Bob" : "You're not Bob, I AAM BOB!!"}
    return jsonify(val)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


#@app.route('/wikipedia/<company>')
#def wikipedia_route(company):
#
#    from google.cloud import language
#    from google.cloud.language import enums
#    from google.cloud.language import types  
#    result = wikipedia.summary(company, sentences=10)
#    
#    client = language.LanguageServiceClient()
#    document = language.types.Document(
#        content = result,
#        type = enums.Document.Type.PLAIN_TEXT
#    )
#    entities = client.analyze_entities(document).entities
#    return str(entities)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
