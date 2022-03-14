from index import db


class Querycollection(db.Document):
    question = db.StringField(max_length=255, unique=True)
    answer = db.StringField(max_length=255, required=True)

    def save(self, *args, **kwargs):
        super(Querycollection, self).save(*args, **kwargs)
