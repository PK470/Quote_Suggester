from django.db import models

# Create your models here.
class Quote(models.Model):
    MOOD_CHOICE = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('stressed','Stressed'),
        ('motivated','Motivated'),
    ]

    CATEGORY_CHOICES = [
        ('inspirational', 'Inspirational'),
        ('love', 'Love'),
        ('humor','Humor'),
        ('wisdom', 'Wisdom'),
    ]

    text = models.TextField()
    author = models.CharField(max_length = 100)
    mood = models.CharField(max_length = 20, choices = MOOD_CHOICE)
    category = models.CharField(max_length = 20, choices = CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.text} - {self.auther}"