from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
import os
import requests

parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAVE_PATH = os.path.join(parent_directory, "download_pic", "reference")

# 路径不存在时添加
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

Pattern_AI_reference_change_BP = Blueprint("Pattern_AI_reference_change", __name__)


# 后续AI
def reference_func(rf, mask):
    pass


@Pattern_AI_reference_change_BP.route(
    "/api/pic_ai/reference_change", methods=["POST"], endpoint="/Pattern_AI_reference_change"
)
def Pattern_AI_reference_change():
    if request.method == "POST":
        # 参考/蒙版不存在时返回error
        if "reference" not in request.files or "mask" not in request.files:
            return jsonify({"error": "No file part"}), 400

        # 接收数据
        # 文件名保存为rf,mask
        rf = request.files["reference"]
        rf_name = secure_filename(rf.filename)
        _, rf_extension = os.path.splitext(rf_name)
        rf.save(os.path.join(SAVE_PATH, "rf" + rf_extension))

        mask = request.files["mask"]
        mask_name = secure_filename(mask.filename)
        _, mask_extension = os.path.splitext(mask_name)
        mask.save(os.path.join(SAVE_PATH, "mask" + mask_extension))

        reference_func(rf, mask)

        return (
            jsonify({"status": 0, "date": {"mutiply_pic": "", "gen_model": "", "msg": "reference_ai is sucessful!"}}),
            200,
        )
