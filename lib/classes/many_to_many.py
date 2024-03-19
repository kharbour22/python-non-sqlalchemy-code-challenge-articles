class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title_parameter):
        if(not hasattr(self, 'title')) and (isinstance(title_parameter, str)) and (5 <= len(title_parameter) <= 50):
            self._title = title_parameter

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author_parameter):
        if(isinstance(author_parameter, Author)):
            self._author = author_parameter

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine_parameter):
        if(isinstance(magazine_parameter, Magazine)):
            self._magazine = magazine_parameter


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_parameter):
        if(not hasattr(self, 'name')) and (isinstance(name_parameter, str)) and (len(name_parameter)>0):
            self._name = name_parameter

    def articles(self):
        return[ article for article in Article.all if article.author is self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if(len(self.articles()) == 0):
            return None
        else:
            return [magazine.category for magazine in self.magazines()]

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if(isinstance(name_parameter, str)) and (2 <= len(name_parameter) <= 16):
            self._name = name_parameter

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category_parameter):
        if(isinstance(category_parameter, str)) and (len(category_parameter)>0):
            self._category = category_parameter


    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        if(len(self.articles()) == 0):
            return None
        else:
            return [article.title for article in self.articles()]

    def contributing_authors(self):
        contributing_authors_list = [author for author in self.contributors() if len([article for article in author.articles() if article.magazine is self]) > 2]
        if(len(contributing_authors_list) == 0):
            return None
        else:
            return contributing_authors_list