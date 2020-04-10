from flask import Flask
from flask_restplus import Api, Resource
from flask import request
from TextSumy import summary

flask_app = Flask(__name__)
app = Api(app=flask_app)

name_space = app.namespace('main', description='Main APIs')


@name_space.route("")
@name_space.doc(params={'url': {'description': 'URL of site for summary', 'in': 'query', 'type': 'string'}})
class MainClass(Resource):
    def get(self):
        res = summary(str(request.args.get('url')))
        return {
            "summary": str(res)
        }


if __name__ == '__main__':
    app.run()
