import webbrowser
import urllib2
import simplejson

class TomatoMedia():

    def __init__(self, title, description, image_url, trailer_url):
        self.title = title
        self.description = description
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_url



class Movie():
    """ This class stores movie information, such as Title and story, as well as URL's for displaying the Poster image and Trailer video """

    def __init__(self, title, description, trailer_url):
        self.title = title
        self.description = description
        self.poster_image_url = self.get_image(title)
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def get_image(self, title):
        fetcher = urllib2.build_opener()
        #The title has all spaces replaced with "%20" so we can search google images for the title's movie poster
        searchTerm = self.title.replace(" ", "%20") + "%20Movie%20Poster"
        searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm
        f = fetcher.open(searchUrl)
        deserialized_output = simplejson.load(f)

        #We grab the url from the JSON response the API gives off
        imageUrl = deserialized_output['responseData']['results'][0]['unescapedUrl']
        return imageUrl
