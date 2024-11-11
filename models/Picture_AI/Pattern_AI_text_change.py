from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
import os
import requests

parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAVE_PATH = os.path.join(parent_directory, "download_pic", "text")


# 路径不存在时添加
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

Pattern_AI_text_change_BP = Blueprint("Pattern_AI_text_change", __name__)


# 后续AI
def text_func(description, rf, mask):
    pass


@Pattern_AI_text_change_BP.route("/api/pic_ai/text_change", methods=["POST"], endpoint="/Pattern_AI_text_change")
def Pattern_AI_text_change():
    if request.method == "POST":
        # 提示词描述
        description = request.form.get("description")

        # 参考/蒙版/模型不存在时返回error
        if "reference" not in request.files or "mask" not in request.files:
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

        text_func(description, rf, mask)

        return (
            jsonify(
                {"status": 0, "date": {"mutiply_pic": "", "gen_model": "", "msg": f"description is {description}"}}
            ),
            200,
        )
