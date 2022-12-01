from sqlalchemy import Column, Integer, String

from app.database import Base


class Users(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    email=Column(String(100), nullable=False,unique=True)
    password=Column(String(20),nullable=False,unique=True)
   

    def __repr__(self):
        return f"<User={self.id} email={self.email}>"