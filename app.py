from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS

from models.Editting_AI import Editting
from models.Package_AI import Package_AI_BP
from models.Inspiration_AI import Inspiration_AI

from models.Package_AI import Package_AI_BP
from models.Picture_AI.Pattern_AI_color_change import Pattern_AI_color_change_BP
from models.Picture_AI.Pattern_AI_area_change import Pattern_AI_area_change_BP
from models.Picture_AI.Pattern_AI_text_change import Pattern_AI_text_change_BP
from models.Picture_AI.Pattern_AI_reference_change import Pattern_AI_reference_change_BP

app = Flask(__name__)
cors = CORS(app)
api = Api(app)


@app.route("/")
def index():
    return jsonify({"msg": "welcome to flask_base"}), 200


api.add_resource(Editting, "/api/edit_ai")
app.register_blueprint(Inspiration_AI)

app.register_blueprint(Package_AI_BP)
app.register_blueprint(Pattern_AI_color_change_BP)
app.register_blueprint(Pattern_AI_area_change_BP)
app.register_blueprint(Pattern_AI_text_change_BP)
app.register_blueprint(Pattern_AI_reference_change_BP)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
