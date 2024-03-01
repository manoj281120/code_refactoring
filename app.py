from flask import Flask, render_template, request

app = Flask(__name__)
app.jinja_env.globals.update(enumerate=enumerate)
notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("home.html", notes=notes)

@app.route('/delete/<int:index>')
def delete(index):
    del notes[index]
    return render_template("home.html", notes=notes)

@app.route('/modify/<int:index>', methods=["GET", "POST"])
def modify(index):
    if request.method == "POST":
        new_note = request.form.get("new_note")
        notes[index] = new_note
        return render_template("home.html", notes=notes)
    else:
        return render_template("modify.html", index=index, note=notes[index])

if __name__ == '__main__':
    app.run(debug=True)
