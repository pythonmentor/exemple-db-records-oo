from . import managers


class Article:

    objects = managers.ArticleManager()

    def __init__(self, title, id=None, *args, **kwargs):
        self.id = id
        self.title = title

    def save(self):
        self.objects.save(self)

    def add_tag(self, tag):
        ArticleTag.objects.add(self, tag)


class ArticleTag:

    objects = managers.ArticleTagManager()

    def __init__(self, article_id, tag_id, *args, **kwargs):
        self.article_id = article_id
        self.tag_id = tag_id

    def add(self, article, tag):
        self.objects.add(article, tag)


class Tag:

    objects = managers.TagManager()

    def __init__(self, tagname, id=None, *args, **kwargs):
        self.id = id
        self.tagname = tagname

    def save(self):
        self.objects.save(self)

    def add_article(self, article):
        ArticleTag.objects.add(self, tag)