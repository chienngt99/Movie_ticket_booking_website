from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.title

class ShowTime(models.Model):
    time = models.TimeField()

    def __str__(self):
        return str(self.time)

class MoviePost(models.Model):
    lang_choice = (
        ('Anh', 'English'),
        ('Việt', 'VietNam'),

    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    detail = models.TextField(default='')
    cast = models.CharField(max_length=100)
    director = models.CharField(max_length=20)
    language = models.CharField(max_length=10, choices=lang_choice)
    public_date = models.DateField()
    run_length = models.IntegerField(help_text="Enter run length in minutes")
    trailer = models.URLField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='media')





    class Meta:
        verbose_name_plural = 'MoviePost'

    def __str__(self):
        return self.name



class MovieShow(models.Model):

    time_show = models.TimeField()
    movie = models.ForeignKey(MoviePost, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.movie) + '  |  ' + str(self.time_show)

