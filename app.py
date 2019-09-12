from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    #q=request.args.get('happy')
    #key = request.args.get('P7Z5S0UI3LE8')
    #limit = request.args.get(10)
    url = "https://api.tenor.com/v1/search?q=happy&key=P7Z5S0UI3LE8&limit=8"
    #url = "https://api.tenor.com/v1/search?q=q&key=key&limit=limit"
    # TODO: Make 'params' dict with query term and API key
    #mydict = {'q': 'happy'}
    # TODO: Make an API call to Tenor using the 'requests' library
    response = requests.get(url)
    gif = response.json()
    #print(response.content)
    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
