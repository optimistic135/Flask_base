from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
import os
import requests


parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAVE_PATH = os.path.join(parent_directory, "download_pic", "change")


# 路径不存在时添加
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

Pattern_AI_color_change_BP = Blueprint("Pattern_AI_color_change", __name__)


# 后续AI
def color_func(color, rf):
    pass


@Pattern_AI_color_change_BP.route("/api/pic_ai/color_change", methods=["POST"], endpoint="/Pattern_AI_color_change")
def Pattern_AI_color_change():
    if request.method == "POST":
        # 颜色
        color = request.form.get("color")

        # 参考不存在时返回error
        if "reference" not in request.files:
            return jsonify({"error": "No file part"}), 400

        # 接收数据
        # 文件名保存为rf
        rf = request.files["reference"]
        rf_name = secure_filename(rf.filename)
        _, rf_extension = os.path.splitext(rf_name)
        rf.save(os.path.join(SAVE_PATH, "rf" + rf_extension))

        color_func(color, rf)

        return (
            jsonify(
                {
                    "status": 0,
                    "date": {
                        "mutiply_pic": "",
                        "gen_model": "",
                        "color_setting": {"material": "", "col_pic": ""},
                        "msg": f"pic_color is {color}",
                    },
                }
            ),
            200,
        )
