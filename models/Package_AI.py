from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
import os
import requests


SAVE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "download_pic", "package_ai")

# 路径不存在时添加
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

Package_AI_BP = Blueprint("Package_AI", __name__)


# 后续AI
def Package_func(description, rf, mask, model):
    pass


@Package_AI_BP.route("/api/package_ai", methods=["POST"], endpoint="/Package_AI")
def Package_AI():
    if request.method == "POST":
        # 提示词描述
        description = request.form.get("description")

        # 参考/蒙版/模型不存在时返回error
        if "reference" not in request.files or "mask" not in request.files or "model" not in request.files:
            return jsonify({"error": "No file part"}), 400

        # 接收数据
        # 文件名保存为rf,mask,model
        rf = request.files["reference"]
        rf_name = secure_filename(rf.filename)
        _, rf_extension = os.path.splitext(rf_name)
        rf.save(os.path.join(SAVE_PATH, "rf" + rf_extension))

        mask = request.files["mask"]
        mask_name = secure_filename(mask.filename)
        _, mask_extension = os.path.splitext(mask_name)
        mask.save(os.path.join(SAVE_PATH, "mask" + mask_extension))

        model = request.files["model"]
        model_name = secure_filename(model.filename)
        _, model_extension = os.path.splitext(model_name)
        model.save(os.path.join(SAVE_PATH, "model" + model_extension))

        Package_func(description, rf, mask, model)

        # url = "http://127.0.0.1:5000//api/package_ai"
        # files = {
        #     "rf": os.path.join(SAVE_PATH, "rf" + rf_extension),
        #     "mask": os.path.join(SAVE_PATH, "mask" + mask_extension),
        #     "model": os.path.join(SAVE_PATH, "model" + model_extension)
        # }
        # data = {
        #     "description": description
        # }
        # response = requests.post(url, files=files, data=data)
        # # 输出响应
        # print(response.status_code)
        # print(response.json())

        # 返回接收成功
        return jsonify({"msg": "successful to finish download"}), 200
