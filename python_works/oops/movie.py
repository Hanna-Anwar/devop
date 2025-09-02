class Movie:

    def __init__(self,title,director,language,year):

        self.title = title

        self.director = director

        self.language = language

        self.year = year


    def display_movie(self):

        print(f"\n movie-title =  {self.title} \n movie-director = {self.director} \n language = {self.language} \n year = {self.year}\n")

    def __str__(self):

         return self.year
    
movie_instance = Movie("ABCD","vrinda","hindi","2012")

movie_instance.display_movie()

print(movie_instance)