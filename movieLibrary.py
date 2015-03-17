# -*- coding: utf-8 -*-
import movieMedia
import fresh_tomatoes

#Create each of the movieMedia objects for display. This list can be extended to standard Integer limits without issue.
pirates = movieMedia.Movie("Pirates of the Caribbean", "Blacksmith Will Turner teams up with pirate Captain Jack Sparrow to save his love from Jack's former pirate allies, who are now undead.", "https://www.youtube.com/watch?v=naQr0uTrH_s")
lego = movieMedia.Movie("Lego Movie", "The LEGO® Movie, the first-ever, full-length theatrical LEGO® adventure, directed by Phil Lord & Christopher Miller, opens in theaters February 7, 2014.", "https://www.youtube.com/watch?v=fZ_JOBCLF-I")
robinHood = movieMedia.Movie("Robin Hood: Men in Tights", "Unlike some OTHER Robin Hoods, he can speak with an English accent. A great parody based on the orginal.", "https://www.youtube.com/watch?v=dX4Ik-cyp-I")
montyPython = movieMedia.Movie("Monty Python and the Holy Grail", "King Arthur and his knights embark on a low-budget search for the Grail, encountering many very silly obstacles.", "https://www.youtube.com/watch?v=urRkGvhXc8w")
predator = movieMedia.Movie("Predator", "Predator is a 1987 American science fiction horror/action film directed by John McTiernan, starring Arnold Schwarzenegger, Carl Weathers, Jesse Ventura, and Kevin Peter Hall.", "https://www.youtube.com/watch?v=Y1txEAywdiw")
homeAlone = movieMedia.Movie("Home Alone", "A child is left alone at home by accident, and gets into crazy situations when someone breaks in.", "https://www.youtube.com/watch?v=CK2Btk6Ybm0")

#We pack up the objects into one array for a clean method call signature
movies = [pirates, lego, robinHood, montyPython, predator, homeAlone]

#The data gets fed into the backend with just one method call.
#Using just one method call, as oppossed to setting the data in one call then running in a second, helps to prevent call errors.
fresh_tomatoes.open_movies_page(movies)
