from flask import Flask, render_template, request, url_for
import requests
import json

app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    search_term = "sad"
    key = "P7Z5S0UI3LE8"
    lmt = 10

    # TODO : Learn about paramters in Flask
    # TODO: Make 'params' dict with query term and API key
    # params = [
    #      {
    #         "search_term": search_term,
    #         "key": key,
    #         "lmt" = lmt
    #      }
    #  ]
    # TODO: Make an API call to Tenor using the 'requests' library
    response = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, key, lmt))
    # TODO: Get the first 10 results from the search results
    gifs = response.json()
    gifs_results = gifs['results']
    # gif_media_dict = gifs_results[0]["media"][0]
    # gif_media_dict_url = gifs_results["media"][0]["gif"]["url"]
    #print(gif_media_dict)
    gif_url_array = [] # list to contain all urls only
    # return gif_media_dict_url
    for url in gifs_results:
        gif_url_array.append(url["media"][0]["gif"]["url"])

    # for gif in gif_url_array:
    #     print(gif)
    #return gif_url_array[3]
    #for gif_key,gif_value in gif_media_dict.items():
    #     #print(gif_media_dict[gif_key])
    #     gif_url_array.append(gif_value["url"])
    # print(gif_url_array)

    # TODO : SEND gif_url_array to index.html to populate the page

        #gif_url_array.append(gif[])
    # media_objects = []
    #
    # for media in gif_media_array:
    #     media_objects.append(media)
    #     print(media)

    # print(media_objects[0])


    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template("index.html", gif_url_array=gif_url_array)

if __name__ == '__main__':
    app.run(debug=True)
