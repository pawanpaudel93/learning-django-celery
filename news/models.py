from django.db import models


class News(models.Model):
    source = models.CharField("Source", max_length=255)
    author = models.CharField("Author", max_length=255, null=True)
    title = models.CharField("Title", max_length=255)
    description = models.CharField("Description", max_length=255)
    url = models.URLField("News URL", max_length=255, help_text="The URL to the news")
    image_url = models.URLField("Image URL", max_length=255, help_text="The URL to the news image")
    published_at = models.DateTimeField("Created on")
    content = models.TextField("Content")

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ['-published_at', 'title']

    def __str__(self):
        return self.title
