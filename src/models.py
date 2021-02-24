from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(120), unique=False, nullable=False)
    lastname = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    Comments = db.relationship('Comment', backref='User', lazy=True)
    Posts = db.relationship('Post', backref='User', lazy=True)
   # Followers = db.relationship("Followers", secondary="") Dudas sobre si lo hecho está correcto y este many to many como indicarlo.
   

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
        }

class Comment(db.Model):
    __tablename__ = 'Comment'
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(500), unique=True, nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('User.id'),
        nullable=False)  
    post_id = db.Column(db.Integer, db.ForeignKey('Post.id'),
        nullable=False)

    def __repr__(self):
        return '<Comment %r>' % self.id

    def serialize(self):
        return {
           "comment_text": self.comment_text,
            "autor_id": self.autor_id,
            "post_id": self.post_id,
            
        }

class Post(db.Model):
    __tablename__ = 'Post'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'),
        nullable=False)
    comments = db.relationship('Comment', backref='Post', lazy=True)
    medias = db.relationship('Media', backref='Post', lazy=True)
    users = db.relationship('User', backref='Post', lazy=True)

    def __repr__(self):
        return '<Post %r>' % self.Id

    def serialize(self):
        return {
            "user_from_id": self.Id,
            "user_to_id": self.user_id,                    
        }

class Media(db.Model):
    __tablename__ = 'Media'
    id  = db.Column(db.Integer, primary_key=True)
    type_ = db.Column(db.String(80), unique=False, nullable=False)
    url = db.Column(db.String(120), unique=False, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('Post.id'),
        nullable=False)

  

    def __repr__(self):
        return '<Media %r>' % self.id

    def serialize(self):
        return {
            "type": self.type_,    
            "url": self.url, 
            "post_id": self.post_id,                 
        }

class Follower(db.Model):
    __tablename__ = 'follower'
    user_from_id  = db.Column(db.Integer, db.ForeignKey('User.id'),
        nullable=False)
    user_to_id = db.Column(db.Integer, db.ForeignKey('User.id'),
        nullable=False)
  

    def __repr__(self):
        return '<Follower %r>' % self.user_from_id

    def serialize(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id,                    
        }
