class VideoGameRequest:
    def __init__(self, category=None, name=None, releaseDate=None, rating=None, reviewScore=None):
        self.category = category
        self.name = name
        self.releaseDate = releaseDate
        self.rating = rating
        self.reviewScore = reviewScore

    def to_dict(self):
        return {
            "category": self.category,
            "name": self.name,
            "releaseDate": self.releaseDate,
            "rating": self.rating,
            "reviewScore": self.reviewScore
        }

    @classmethod
    def Builder(cls):
        return cls.VideoGameRequestBuilder()
    

    class VideoGameRequestBuilder:
        def __init__(self):
            self._category=None
            self._name=None
            self._releaseDate=None
            self._rating=None
            self._reviewScore=None

        def category(self, category):
            self._category = category
            return self
        
        def name(self, name):
            self._name = name
            return self
        
        def releaseDate(self, releaseDate):
            self._releaseDate = releaseDate
            return self
        
        def rating(self, rating):
            self._rating = rating
            return self
        
        def reviewScore(self, reviewScore):
            self._reviewScore = reviewScore
            return self
        
        def build(self):
            return VideoGameRequest(
                category= self._category,
                rating= self._rating,
                releaseDate= self._releaseDate,
                reviewScore= self._reviewScore,
                name= self._name
            )
        
