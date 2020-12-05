from django.db import models


# Class to represent Genre model
class Genre(models.Model):
    name = models.CharField(max_length=100, default='Misc')

    def __str__(self):
        return self.name


# Class to represent Movie Model
class Movie(models.Model):
    name = models.CharField(max_length=200)
    popularity = models.FloatField('99 popularity', default=0.0)
    imdb_score = models.FloatField('Imdb Score', default=0.0)
    director = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)

    # Method to resolve viewing conflict in a ManyToMany Relation field.
    # Return - list of genre strings.
    def get_genres(self):
        return "\n".join([g.name for g in self.genres.all()])

    # For the column names in the tables(Admin/Users)
    get_genres.admin_order_field = 'genre'  # Allows column order sorting
    get_genres.short_description = 'Genres'  # Renames column head

    def __str__(self):
        return self.name
