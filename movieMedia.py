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
        #We use the default webbrowser, for added convenience of familiarity for the user.
        #Opening in a non-default browser is a very quick way to discourage users from utilizing our program.
        webbrowser.open(self.trailer_youtube_url)

    def get_image(self, title):
        fetcher = urllib2.build_opener()
        #The title has all spaces replaced with "%20" so we can search google images for the title's movie poster
        #This allows the user to input a common string, such as "Pirates of the Carribean", without having to worry about formatting in a way Google's API would understand
        #Dynamically grabbing the Movie poster helps to ease use of program, and allows the latest movie poster to be grabbed each time.
        searchTerm = self.title.replace(" ", "%20") + "%20Movie%20Poster"
        searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm
        f = fetcher.open(searchUrl)

        #The output of the Google API search needs to be deserialized into an object, so we can access it in the backend without having to parse strings
        deserialized_output = simplejson.load(f)

        #We grab the image url from the now-converted JSON object, and use it for displaying the poster image
        imageUrl = deserialized_output['responseData']['results'][0]['unescapedUrl']
        return imageUrl
