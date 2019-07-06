from . import models
from .database import db

class ArticleManager:
    
    def __init__(self):
        db.query("""
            CREATE TABLE IF NOT EXISTS article(
                id INT PRIMARY KEY AUTO_INCREMENT,
                title VARCHAR(255) NOT NULL
            )
        """)

    def create(self, title, id=None, *args, **kwargs):
        article = models.Article(title, id, *args, **kwargs)
        article.save()
        return article

    def save(self, article):
        with db.transaction() as conn:
            conn.query("""
                INSERT INTO article(id, title)
                VALUES (:id, :title)
                ON DUPLICATE KEY UPDATE title=VALUES(title), id=VALUES(id)
            """, **vars(article))
            
            for row in conn.query(
                "SELECT LAST_INSERT_ID() AS id WHERE LAST_INSERT_ID() != 0"
            ):
                article.id = row['id']

class ArticleTagManager:
    
    def __init__(self):
        db.query("""
            CREATE TABLE IF NOT EXISTS article(
                article_id INT REFERENCES article(id),
                tag_id INT REFERENCES tag(id),
                PRIMARY KEY (article_id, tag_id)
            );
        """)

    def add(self, article, tag):
        db.query("""
            INSERT IGNORE INTO article_tag(article_id, tag_id)
            VALUES (:article_id, :tag_id)
        """, article_id=article.id, tag_id=tag.id)


class TagManager:
    
    def __init__(self):
        db.query("""
            CREATE TABLE IF NOT EXISTS tag(
                id INT PRIMARY KEY AUTO_INCREMENT,
                tagname VARCHAR(255) NOT NULL,
                slug VARCHAR(255) NOT NULL UNIQUE
            );
        """)

    def create(self, tagname, id=None, *args, **kwargs):
        tag = models.Tag(tagname, id, *args, **kwargs)
        tag.save()
        return tag

    def save(self, tag):
        with db.transaction() as conn:
            conn.query("""
                INSERT INTO tag(id, tagname)
                VALUES (:id, :tagname)
                ON DUPLICATE KEY UPDATE id=id, tagname=VALUES(tagname)
            """, **vars(tag))
            
            for row in db.query(
                "SELECT LAST_INSERT_ID() AS id WHERE LAST_INSERT_ID() != 0"
            ):
                tag.id = row['id']