from myapp.models import Article, Tag, ArticleTag


articles = [
    {
        'title': 'Démarrer avec les bases de données en python avec records',
        'tags': "python, database, records"
    },
    {
        'title': "Un espace d'entraide pour les futurs dev python",
        'tags': "openclassroom, discord"
    }
]


def main():
    for article in articles:
        new_article = Article.objects.create(title=article['title'])
        for tag in article['tags'].split(", "):
            new_tag = Tag.objects.create(tagname=tag)
            new_article.add_tag(new_tag)


if __name__ == "__main__":
    main()