from sqlalchemy.orm import Session
from app.models.post import Post
from datetime import datetime


def create_posts(
    db: Session,
    company_name: str,
    platform: str,
    calendar: list
):
    posts = []

    for item in calendar:
        existing_post = db.query(Post).filter_by(
            company_name=company_name,
            platform=platform,
            publish_date=datetime.strptime(item["publish_date"], "%Y-%m-%d").date(),
            topic=item["topic"]
        ).first()

        if existing_post:
            continue

        post = Post(
            company_name=company_name,
            platform=platform,
            publish_date=datetime.strptime(
                item["publish_date"], "%Y-%m-%d"
            ).date(),
            topic=item["topic"],
            ad_copy=item["ad_copy"],
            hashtags=", ".join(item["hashtags"]),
            image_prompt=item["image_prompt"],
            status="pending"
        )
        db.add(post)
        posts.append(post)

    db.commit()
    return posts
