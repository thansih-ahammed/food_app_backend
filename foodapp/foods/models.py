from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=200)
    publisher_name = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to="foods/images")
    ingredients = models.TextField()
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'foods_food'

    def __str__(self):
        return self.name
        