from io import BytesIO
from flask import Flask, send_file, request

from ..post_factory.carousel_factory import CarouselFactory
from ..post_factory.single_post_factory import SinglePostFactory

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post_handler():
  request_data = request.get_json()
  post_type = request_data.get('type')
  
  post_factory = None

  if post_type == 'carousel':
    post_factory = CarouselFactory(request_data)
  elif post_type == 'single':
    post_factory = SinglePostFactory(request_data)

  image = post_factory.make()
  image_buffer = BytesIO()
  image.save(image_buffer, format='PNG')
  image_buffer.seek(0)

  return send_file(image_buffer, mimetype='image/png')
