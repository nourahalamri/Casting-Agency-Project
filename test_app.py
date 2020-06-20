import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor, MovieActor

database_name = "database_test.db"
executive_producer_headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii0xMk56dzVBLXhnS3NmQnIxai1mbSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRuLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWVjYzY5NGEwN2RkYzAwMTkxNjNkMDgiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MjY1MjQ0MSwiZXhwIjoxNTkyNjU5NjQxLCJhenAiOiJXQ3ZOd0FXMEJrajFwTnJLOWFUczZFSHNPVHVMc1R3WCIsInNjb3BlIjoiIn0.MFDQi6DWupK8rVU7ec1OqMeAH7DZRSKYRv-pDIlUn0GU7QFc7foE5eoUvfMmu3QuORSuylzUOiGoy1hlVRstxKxlQ9Ukq2Z6x9JYvGrZVixsl-du0aXhsVmZtLxjUYoJiPknz132gT5XmGcHU-u6BMF0BGqOlrGTBfLFXkrYsfp5cWQSOpZnvluvddndSQ6Dx7NzKwM_KtHJHRS8KbJMcwheXiM6Sd27TOEFi1wGl2KdJVlV7DjnLh1mkAsTXaV8A5e0yOrWZz0YbGtd4wuX5PbuV-JCzWl1QFbMnrp8WGjgsSBxlTLy-iruzQyXzj7V9UxqwxeTjCZdFBxcZM1AYw'}
casting_director_headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii0xMk56dzVBLXhnS3NmQnIxai1mbSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRuLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWVjYzY2NWEwN2RkYzAwMTkxNjNjYTgiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MjY1MjM2MiwiZXhwIjoxNTkyNjU5NTYyLCJhenAiOiJXQ3ZOd0FXMEJrajFwTnJLOWFUczZFSHNPVHVMc1R3WCIsInNjb3BlIjoiIn0.R85KfelXHNXXXYlSYu1vEI5eg4Y68rkv2Yov_Ix54rxNp9UDAri1yqF7DM1lcqJa7a8EsZpjoYvn7lYc4mlXUWUi1YIINuweaCuM9DzOZxIn5RMj-dZuOUjvYHCsZv7228PTACwfA6UhtExkbMQZ5xGTFQGXPf02i4LoNjYCxEc_naX2NObxn0UOdFOTY7nhiHFLAotU8Gaz25Go876--LYshCp5bmCygfnw9fam6wvBhwwB-4p46piLTqjsxh2skUD3IUETgAykpMEVXm8NagO09yly6olnSo3dAMs_0_51_0hz2ab06FUxn74i6H3Pv1wxKlWRoCZ_Lfmh3m130w'}
casting_assistant_headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii0xMk56dzVBLXhnS3NmQnIxai1mbSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRuLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWVjYzYyMmEwN2RkYzAwMTkxNjNjMzUiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MjY1MjE5MywiZXhwIjoxNTkyNjU5MzkzLCJhenAiOiJXQ3ZOd0FXMEJrajFwTnJLOWFUczZFSHNPVHVMc1R3WCIsInNjb3BlIjoiIn0.jSanFDleI3beZA07tXfg3bSDkVbF46EWDkWIcHEptrfOOcnkc7r2AEPvQ24PSbcvmquNcwtJNuKHr2qwjZonTB9Znv97Be8VXVHiGvqI4zpnbj3yBQ0_Dmdw-7YYaeAGncY8dRi-xvfXiCUFv5tnCyccrHsw7Qp0O5Yz0qXSVwMr6I-e9IZap4O63xTDcbo8OxGlnQ-ALO2dN8DDZxotyzdROkFMXBD2u7m3MtJFyI9o52qeA1AnVoUeYXbFsk18qnPuj4cB7fmsjjtUsccLM7Fc-7oM-H96XQJFwS6c4Np1VZJg8yv1NFYe0D6Sj-46YgkuNaKakDAcQXgowhDIiw'}


class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(None, database_name)
        self.client = self.app.test_client
        setup_db(self.app, "database_test.db")

        self.new_movie = {
            'title': 'Nour sma',
            'release_date': '2017-01-22'
        }

        self.new_actor = {
            'name': 'Maha Alhart',
            'age': 23,
            'gender': 'Female'
        }

        self.new_movieActor = {
            'movie_id': 1,
            'actor_id': 1
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

    def tearDown(self):
        pass

    def test_get_movies(self):
        res = self.client().get('/movies', headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'], True)

    def test_get_movies_method_not_allowed(self):
        res = self.client().get('/movies/1',
                                headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)

    def test_get_movies_casting_director(self):
        res = self.client().get('/movies',
                                headers=casting_director_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'], True)

    def test_get_movies_casting_assistant(self):
        res = self.client().get('/movies', headers=casting_assistant_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'], True)

    def test_create_movie(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=executive_producer_headers)
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_if_movie_creation_not_allowed(self):
        res = self.client().post('/movies/1', json=self.new_movie,
                                 headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)

    def test_create_movie_casting_director(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=casting_director_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_movie_casting_assistant(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=casting_assistant_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_update_movie(self):
        movie = Movie.query.first()
        res = self.client().patch('/movies/'+str(movie.id),
                                  json=self.new_movie,
                                  headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movies_if_not_exist(self):
        res = self.client().patch('/movies/55', json=self.new_movie,
                                  headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_movies(self):
        movie = Movie.query.first()
        res = self.client().delete('/movies/'+str(movie.id),
                                   headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movies_if_not_exist(self):
        res = self.client().delete('/movies/55',
                                   headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_get_actors(self):
        res = self.client().get('/actors', headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'], True)

    def test_get_actors_method_not_allowed(self):
        res = self.client().get('/actors/1',
                                headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)

    def test_create_actor(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_if_actor_creation_not_allowed(self):
        res = self.client().post('/actors/1', json=self.new_actor,
                                 headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)

    def test_create_actor_casting_director(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers=casting_director_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_actor_casting_assistant(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers=casting_assistant_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_update_actor(self):
        actor = Actor.query.first()
        res = self.client().patch('/actors/'+str(actor.id), json=self.new_actor,
                                  headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_actors_if_not_exist(self):
        res = self.client().patch('/actors/55', json=self.new_actor,
                                  headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_actors(self):
        actor = Actor.query.first()
        res = self.client().delete('/actors/'+str(actor.id),
                                   headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actors_if_not_exist(self):
        res = self.client().delete('/actors/2000',
                                   headers=executive_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


if __name__ == "__main__":
    unittest.main()
