from django.db import models

class Stock(models.Model):
    quote = models.CharField(max_length = 10)


    def __str__(self):
        return self.quote

        
