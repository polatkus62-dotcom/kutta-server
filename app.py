from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
  return "Kutta Server Aktif!"


@app.route("/api", methods=["GET", "POST"])
def api():
  return jsonify({"status": "success", "message": "Key aktif!"})


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=10000)
  
            
