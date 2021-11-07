from app import db


class Item(db.Model):
    title = db.Column(db.String(80), unique=True,
                      nullable=False, primary_key=True)
    desc = db.Column(db.String(120))
    icon = db.Column(db.String(80))
    url = db.Column(db.String(80))

    def __repr__(self):
        return "<Title: {}>".format(self.title)
