from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
from flask import request
import os
from datetime import datetime
import random

SAVE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "download_pic", "inspire")

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

Inspiration_AI = Blueprint("Inspiration", __name__)


def inspire_ai():
    pass


@Inspiration_AI.route("/api/inspire", methods=["POST"])
def Package_AI():
    if request.method == "POST":
        color = request.form.get("color")

        if "image" not in request.files or "mask" not in request.files:
            return jsonify({"error": "No file part"}), 400

        # 获取两个图片文件
        image = request.files["image"]
        mask = request.files["mask"]

        # 获取图片并保存
        image_path = secure_filename(image.filename)
        mask_path = secure_filename(mask.filename)

        image.save(os.path.join(SAVE_PATH, image_path))
        mask.save(os.path.join(SAVE_PATH, mask_path))

        # 后续补充
        inspire_ai()

        return jsonify({"status": 0, "date": {"mutiply_pic": "", "msg": f"inspiration_color is {color}"}}), 200
