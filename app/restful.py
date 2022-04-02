from flask_restful import Api, Resource
from sqlalchemy import func
from app.models import Thread, User
from app import app, db

api = Api(app)

class Thread_cls(Resource):

    def get(self, thread_id):
        thread = Thread.query.filter_by(id = thread_id).first()
        if thread:
            return {'text': thread.text, 'date': str(thread.date), 'images': thread.images, 'answers': [{'id': i.id, 'text': i.text, 'date': str(i.date), 'images': i.images} for i in thread.answers]}
        return {'message': 'Тред не найден'}, 404

class Threads_cls(Resource):

    def get(self, name, page):
        if name == 'new':
            threads = db.session.query(Thread).all()

            return {'Threads': [{'id': x.id, 'text': x.text, 'date': str(x.date), 'images': x.images, 'answers': [{'id': i.id, 'text': i.text, 'date': str(i.date), 'images': i.images} for i in x.answers]} for x in threads]}
        elif name == 'act':
            threads = db.session.query(Thread, func.count(User.id)).outerjoin(User).group_by(Thread.id).order_by(Thread.id.desc()).paginate(page, 10, False)

            threads_act = sorted(list(threads.items), key=lambda x: x[1])[::-1]
            return {'Threads': [{'id': x[0].id, 'text': x[0].text, 'date': str(x[0].date), 'images': x[0].images, 'answers': [{'id': i.id, 'text': i.text, 'date': str(i.date), 'images': i.images} for i in x[0].answers]} for x in threads_act]}
        return {'message': 'Ошибочка'}, 404

api.add_resource(Thread_cls, '/api/thread/<int:thread_id>/')
api.add_resource(Threads_cls, '/api/threads/<string:name>/<int:page>/')
