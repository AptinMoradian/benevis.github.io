from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit_text", methods=["POST"])
def submit_text():
    input_text = request.form["input_text"]
    if input_text:
        return jsonify({"success": True, "input_text": input_text})
    else:
        return jsonify({"success": False, "message": "متن نوشته خالی است."})

if __name__ == "__main__":
    app.run(debug=True)
