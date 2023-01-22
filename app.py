from flask import Flask, render_template, request

app = Flask(__name__)

todo_list = []

@app.route("/")
def index():
    return render_template("index.html", todo_list=todo_list)

@app.route("/add_todo", methods=["POST"])
def add_todo():
    task = request.form["task"]
    todo_list.append(task)
    return render_template("index.html", todo_list=todo_list)

@app.route("/remove_todo/<int:index>")
def remove_todo(index):
    todo_list.pop(index)
    return render_template("index.html", todo_list=todo_list)

if __name__ == "__main__":
    app.run(debug=True)
