from flask import Flask, request, jsonify, Blueprint
import ollama

desiredModel = "qwen2.5:1.5b"

app = Flask(__name__)
ai_chat_bp = Blueprint("ai", __name__, url_prefix="/api/ai")


@ai_chat_bp.route("/chat")
def chat():
    try:
        print(request.args.get("question"))
        question = request.args.get("question")
        response = ollama.chat(
            model=desiredModel, messages=[{"role": "user", "content": question}]
        )
        return response["message"]["content"]
    except Exception as e:
        return jsonify({"error": f"Error {e}"}), 503


app.register_blueprint(ai_chat_bp)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2222)
