from flask import Flask, jsonify, request 
import json
app = Flask(__name__)
answers = dict()

@app.route("/")
def hello():
	return "Welcome to 192overflow's API!"

@app.route("/api/answers", methods=['GET'])
def get_answer():
	question = request.args.get('question')

    with open('db.json', 'r') as db_read:
        answers = json.load(db_read)
	if question in answers:
		return jsonify({"answer": answers[question]})
	else:
		return jsonify({"message": "No answer."})

@app.route("/api/answers", methods=['POST'])
def post_answer():
	data = request.get_json()
	question = str(data["question"])
	answer = str(data["answer"])
	with open('db.json', 'r') as db_read:
        data = json.load(db_read)
    with open('db.json', 'w') as db_write:
        data[question] = answer
        json.dump(data, db_write)
    return jsonify({"question": question, "answer": answer})

@app.route("/answers", methods=['GET'])
def render_answer():
	question = request.args.get('question')
	with open('db.json', 'r') as db_read:
		answers = json.load(db_read)
	if question in answers:
		return render_template("answer.html", question=question, answer=answers[question])
	else:
		return jsonify({"status": 404, "message": "No answer."})
        
if __name__ == "__main__":
	app.run(port=5000, debug=True)