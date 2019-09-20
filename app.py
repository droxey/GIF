from flask import Flask, render_template, request, url_for
import requests
import json


app = Flask(__name__)

@app.route('/')
def index():
    """Return trending gifs to the homepage."""
    # gets a response from the API
    trending_response = requests.get("https://api.tenor.com/v1/trending?key=P7Z5S0UI3LE8&limit=10")
    # returns a dictionary of gif data
    gifs_trending = json.loads(trending_response.content)
    # renders base html file and passes a dictionary of extracted trending gif results as a parameter
    return render_template("base.html", gif_url_list=gifs_trending['results'])

@app.route('/gifs')
def gifsearch():
    """Returns gifs based on the search query the user enters """
    # requests a query string from the user
    search_term = request.args.get("q")
    # gets a response from the API
    response = requests.get(f'https://api.tenor.com/v1/search?q={search_term}&key=P7Z5S0UI3LE8&limit=10')
    # returns a dictionary of gif data
    gifs = json.loads(response.content)
    # renders base html file and passes a dictionary of extracted gifs results as a parameter
    return render_template("base.html", gif_url_list=gifs['results'])



@app.route('/random')
def random():
   """Return random gifs when the user hit the randon button."""
   # requests a query string from the user
   search_term = request.args.get("q")
   # gets a response from the API
   random_response = requests.get(f'https://api.tenor.com/v1/random?q={search_term}&key=P7Z5S0UI3LE8&limit=10')
   # returns a dictionary of gif data
   gifs_random = json.loads(random_response.content)
   # renders base html file and passes a dictionary of extracted random gif results as a parameter)
   return render_template("base.html", gif_url_list=gifs_random['results'])

# a scope where the app is run
if __name__ == '__main__':
    app.run(debug=True)
