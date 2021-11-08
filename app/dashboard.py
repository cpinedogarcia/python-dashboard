from flask import redirect, render_template, request

from app import app, db
from app.models import Item


@app.route('/', methods=["GET"])
def home():
    items = Item.query.all()
    return render_template("index.html", items=items)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.form:
        try:
            item = Item(title=request.form.get("title"), desc=request.form.get(
                "desc"), icon="img/" + request.form.get("icon"), url=request.form.get("url"))
            db.session.add(item)
            db.session.commit()
        except Exception as e:
            print("Filed to save item")
            print(e)
        return redirect("/")
    return render_template("add.html")


@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.form:
        title = request.form.get("title")
        item = Item.query.filter_by(title=title).first()
        db.session.delete(item)
        db.session.commit()
        return redirect("/")
    else:
        items = Item.query.all()
    return render_template("remove.html", items=items)


@app.route("/init", methods=["GET"])
def init():
    for i in range(5):
        item = Item(title=i, desc=i, icon=i, url=i)
        db.session.add(item)
        db.session.commit()
    return redirect("/")
