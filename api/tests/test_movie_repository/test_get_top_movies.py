#from lib.movie_repository import MovieRepository
#import datetime
#from lib.database_connection import get_db
#
#"""
#test that shows the top 2 movies from the test database
#"""
#
#def test_find_top_movies_returns_top_movies():
#    db = get_db()
#    movie_repo =MovieRepository(db)
#    result = movie_repo.find_top_movies(3,"test_movie_database")
#    expected_result = [
#  {
#    "_id": "666af5493ea95c2d6684bd78",
#    "adult": False,
#    "backdrop_path": "/random",
#    "genre_ids": [
#      18,
#      80
#    ],
#    "id": 278,
#    "original_language": "en",
#    "original_title": "Title1",
#    "overview": "Overview1",
#    "popularity": 143.5,
#    "poster_path": "/path1",
#    "release_date": datetime.datetime(1994, 9, 23, 0, 0),
#    "title": "Title1",
#    "video": False,
#    "vote_average": 4.35,
#    "vote_count": 50
#  },
#  {
#    "_id": "666af5493ea95c2d6684bd79",
#    "adult": False,
#    "backdrop_path": "/random1",
#    "genre_ids": [
#      9,
#      75
#    ],
#    "id": 238,
#    "original_language": "en",
#    "original_title": "Title2",
#    "overview": "Overview2",
#    "popularity": 142.2,
#    "poster_path": "/path2",
#    "release_date": datetime.datetime(1972, 3, 14, 0, 0),
#    "title": "Title2",
#    "video": False,
#    "vote_average": 4.35,
#    "vote_count": 100
#  },
#  {
#    "_id": "666af5493ea95c2d6684bd7a",
#    "adult": False,
#    "backdrop_path": "/random2",
#    "genre_ids": [
#      18,
#      80
#    ],
#    "id": 299,
#    "original_language": "en",
#    "original_title": "Title3",
#    "overview": "Overview3",
#    "popularity": 142.2,
#    "poster_path": "/path3",
#    "release_date": datetime.datetime(1972, 3, 14, 0, 0),
#    "title": "Title3",
#    "video": False,
#    "vote_average": 3.5,
#    "vote_count": 150
#  }
#]
#
#
#    assert result == expected_result
