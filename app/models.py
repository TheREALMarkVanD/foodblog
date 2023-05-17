from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class recipe(models.Model):
    
    region=models.CharField(max_length=100)
    title =models.CharField(max_length=100)
    image=models.ImageField(upload_to='images',default="")
    date=models.DateField()
    desc =models.TextField()
    ratings =models.FloatField()
    video =models.FileField(upload_to='videos')
    def __str__(self):
        return self.title

class recipe_card(models.Model):
    myfk=models.ForeignKey(recipe,on_delete=models.CASCADE,default="")
    preptime =models.CharField(max_length=100)
    cooktime =models.CharField(max_length=100)
    totaltime =models.CharField(max_length=100)
    servings =models.CharField(max_length=100)
    instructions =models.TextField()
    ingredients=models.TextField(default="")
    def __str__(self):
        return self.myfk.title
class Comment(models.Model):
    sno= models.AutoField(primary_key=True)
    comments=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(recipe, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
'''
class ingredients(models.Model):
    myfk2=models.ForeignKey(recipe,on_delete=models.CASCADE,default="")
    num =models.CharField(max_length=100)
    ingredient=models.CharField(max_length=100)
'''
#recipe_shortcut(title, image, rating){for dislplay on main page)
#recipe(region, title, desc, date, ratings, video, recipe_card)
#recipe_card(ratings, (prep_time, cook_time, total_time), servings, ingredients, instructions)
#ingredients(title, num, type_of_ingredient)
#comments(user, datetime, content, rating)