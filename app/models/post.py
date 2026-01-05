from sqlalchemy import Column, Integer, String, Text, Date
from app.db.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    platform = Column(String, index=True)
    publish_date = Column(Date, index=True)
    topic = Column(String)
    ad_copy = Column(Text)
    hashtags = Column(Text)
    image_prompt = Column(Text)
    status = Column(String, default="pending")
