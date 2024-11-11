from flask_restful import request, Resource


def edit_ai(image):
    # 具体实现编辑AI的功能
    pass


class Editting(Resource):
    def post(self):
        print(request.files)
        if "image" not in request.files:
            return jsonify({"status": 1, "data": {"msg": "error"}}), 400
        image = request.files["image"]

        edit_ai(image)
        return {"status": 0, "date": {"raw_pic": "", "new_pic": "", "msg": "eding_ai sucessful!"}}
