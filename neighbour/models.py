from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class NeighbourHood(models.Model):
    name = models.CharField(max_length = 30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    occupants = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.name

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neigborhood_id):
        neighborhood = cls.objects.get(id = neigborhood_id)
        return neighborhood

    def update_neighborhood(self):
        self.save()

    def update_occupants(self):
        self.occupants += 1
        self.save()

class UserProfile(models.Model):
    name = models.CharField(max_length = 30)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True)
    email = models.EmailField(max_length = 60, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)
    description = models.TextField(null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business = Business.objects.get(id = business_id)
        return business

    def update_business(self):
        self.save()

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-pub_date']

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name