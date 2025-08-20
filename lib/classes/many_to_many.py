class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
        author._articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        self._magazine = new_magazine


class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = list(set(article.magazine.category for article in self._articles))
        return topics if topics else None


class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None


# The method finds authors who have written more than 2 articles for this magazine.
    def contributing_authors(self):
    # This line uses a list comprehension to filter authors. It counts how many articles each author has written for *this* magazine.
        authors = [author for author in self.contributors() if sum(1 for article in author.articles() if article.magazine == self) > 2]
            # This returns the list of authors if it's not empty, otherwise it returns None.
        return authors if authors else None