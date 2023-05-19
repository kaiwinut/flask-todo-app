from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, static_folder='templates/', static_url_path='')

history = []
todos = []

class Todo:
    def __init__(self, title):
        self.id = len(history) 
        self.title = title

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return isinstance(other, Todo) and self.id == other.id

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add_item', methods=['POST'])
def add_item():
    global todos, history
    if request.method == 'POST':
        todos.append(Todo(request.form['title']))
        history.append(Todo(request.form['title']))
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    global todos 
    if request.method == 'POST':
        remove_ind = set([int(v) for k, v in request.form.items()])
        new_todos = []
        for todo in todos:
            if todo.id not in remove_ind:
                new_todos.append(todo) 
        todos = new_todos
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=8080, debug=True)
