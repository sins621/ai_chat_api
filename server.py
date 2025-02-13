from flask import Flask, request, jsonify
import ollama

desiredModel = "qwen2.5:1.5b"

app = Flask(__name__)


@app.route("/")
def chat():
    print(request.args.get("question"))
    question = request.args.get("question")
    response = ollama.chat(
        model=desiredModel, messages=[{"role": "user", "content": question}]
    )

    return response["message"]["content"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2222)
