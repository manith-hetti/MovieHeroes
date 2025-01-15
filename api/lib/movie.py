class Movie():
    def __init__(self, id, title, overview, poster_path, backdrop_path, vote_average, release_date):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster_path = poster_path
        self.backdrop_path= backdrop_path
        self.vote_average = vote_average
        self.release_date = release_date


    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Movie({self.id}, {self.title}, {self.overview}, {self.poster_path}, {self.backdrop_path}, {self.vote_average}, {self.release_date})"
