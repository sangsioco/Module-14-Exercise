from flask import flask
from flask_graphql import GraphQLView
import graphene
from schema import Query, Mutation
from models import db

app = flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:CIAjrj202709*!@localhost/movie_db'
db.init_app(app)

schemas = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view['graphql', schema=schema, graphiql=True]

)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
