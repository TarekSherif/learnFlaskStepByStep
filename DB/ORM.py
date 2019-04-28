from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///sales1.db')
Base = declarative_base()


class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    image_file = Column(String(20), nullable=False,
                        default='default.jpg')
    password = Column(String(60), nullable=False)
    posts = relationship('Post', bakref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username},{self.email},{self.image_file},{self.password}')"


class Post(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    date_posted = Column(DateTime, nullable=False,
                         default=datetime.utcnow)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title},{self.date_posted}')"


Base.metadata.create_all(engine)
