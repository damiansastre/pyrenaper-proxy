from flask_restful import reqparse
import werkzeug

sid_parser = reqparse.RequestParser()
sid_parser.add_argument('number', type=str, required=True, help='Doc Number')
sid_parser.add_argument('gender', required=True, type=str, help='Gender either M or F')
sid_parser.add_argument('order', required=True, type=str, help='Order ID from document creation')


barcode_parser = reqparse.RequestParser()
barcode_parser.add_argument('front', type=werkzeug.datastructures.FileStorage, location='files', required=True)
