from django.db import models


class Game(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200, blank=True, default='')
	release_date = models.DateTimeField()
	game_category = models.CharField(max_length=200, blank=True, default='')
	played = models.BooleanField(default=False)

	class Meta:
		ordering = ('name',)


class MyModel(models.Model):
    index = models.IntegerField()
    symbol = models.CharField(max_length=20)
    Date = models.DateField()
    Open = models.IntegerField()
    High = models.IntegerField()
    Low = models.IntegerField()
    Close = models.IntegerField()
    Volume = models.IntegerField()
    AdjustmentFactor = models.IntegerField()
    AdjustmentType = models.IntegerField()
    avgvolume = models.IntegerField()    
    
    class Meta:
        ordering = ('avgvolume',)