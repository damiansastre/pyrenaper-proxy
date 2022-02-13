from flask_restful import reqparse
import werkzeug

sid_parser = reqparse.RequestParser()
sid_parser.add_argument('front', type=werkzeug.datastructures.FileStorage, location='files', required=True)