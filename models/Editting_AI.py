from flask_restful import request, Resource
import os
from werkzeug.utils import secure_filename

SAVE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "download_pic", "editting")

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)


def edit_ai(image):
    # 具体实现编辑AI的功能
    pass


class Editting(Resource):
    def post(self):
        print(request.files)
        if "image" not in request.files:
            return {"status": 1, "data": {"msg": "error"}}

        image = request.files["image"]
        image_path = secure_filename(image.filename)
        image.save(os.path.join(SAVE_PATH, image_path))

        edit_ai(image)
        return {"status": 0, "date": {"raw_pic": "", "new_pic": "", "msg": "eding_ai sucessful!"}}
