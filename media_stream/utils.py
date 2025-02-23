class Filters:
    FILTER_TYPES = [
        ('animals & pets', 'animals & pets'),
        ('anime', 'anime'),
        ('art & design', 'art & design'),
        ('auto & technique', 'auto & technique'),
        ('blogging', 'blogging'),
        ('cartoons', 'cartoons'),
        ('celebrity', 'celebrity'),
        ('dance', 'dance'),
        ('fashion & beauty', 'fashion & beauty'),
        ('food & kitchen', 'food & kitchen'),
        ('gaming', 'gaming'),
        ('live pictures', 'live pictures'),
        ('mashup', 'mashup'),
        ('memes', 'memes'),
        ('movies & TV', 'movies & TV'),
        ('music', 'music'),
        ('nature & travel', 'nature & travel'),
        ('science & technology', 'science & technology'),
        ('sports', 'sports'),
        ('stand-up & Jokes', 'stand-up & Jokes'),
    ]

    @classmethod
    def get_filter_types(cls):
        return cls.FILTER_TYPES
