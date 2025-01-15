from lib.database_connection import get_db
from lib.movie_repository import MovieRepository
from lib.movie import Movie
from utils.create_matrix import create_matrix
from utils.movie_recommendations import find_similar_movies
from flask import Flask, request, jsonify, redirect
from lib.rating import Rating
from lib.rating_repository import RatingRepository
from lib.link_repository import LinkRepository
from utils.create_matrix import create_matrix
from utils.movie_recommendations import find_similar_movies
from lib.user_repository import *
import pandas as pd
import time



from app import app


@app.route("/movie_page/<id>", methods=["GET"])
def getMovie(id):
    id = int(id)
    db = get_db()
    movies_repo = MovieRepository(db)
    found_movie = movies_repo.find_movie_by_id(id, "tmdbMovies").__dict__
    ratings = RatingRepository(db).all_ratings()

    X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper = create_matrix(ratings)

    movie_id = id


    similar_ids = find_similar_movies(int(movie_id), db, movie_mapper, movie_inv_mapper, X, k=10)

    found_movie["similar"] = []

    for id in similar_ids:
        similar_movie = movies_repo.find_movie_by_id(int(id), "tmdbMovies").__dict__
        found_movie["similar"].append(similar_movie)

    return jsonify(found_movie)


@app.route('/movie_page/<movie_id>', methods=['POST'])
def rate_movie(movie_id):
    db = get_db()
    link = db['links']
    link_repo = LinkRepository(db)
    movie_id = link_repo.to_movieId(movie_id, link)
    data = request.json
    user_id = data.get('userId')
    rating = data.get('rating')
    ratings = db['ratings']
    user = UserRepository(db)
    user_id = user.get_user_id_from_object_id(user_id)
    rating_repo = RatingRepository(db)
    if ratings.find_one({"$and":[{"userId": user_id}, {"movieId": movie_id}]}) is not None:
        filter = {"$and":[{"userId": user_id}, {"movieId": movie_id}]}
        new_rating = {"$set": {"rating": rating}}
        rating_repo.update_rating(filter, new_rating)
    else:
        print("We are in except")
        rating_repo.add_rating(user_id, movie_id, rating)
    return jsonify({'message': 'Rating submitted successfully'})

