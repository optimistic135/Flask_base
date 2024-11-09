from flask_restful import request, Resource


def edit_ai(image):
    # 具体实现编辑AI的功能
    pass


class Editting(Resource):
    def post(self):
        print(request.files)
        if "image" not in request.files:
            return "No file part"
        file = request.files["image"]

        edit_ai(file)
        return {"code": 200, "msg": "editting image sucessful!"}
