from django.test import TestCase
from .models import UserProfile,NeighbourHood, Business, Post, Comment, Location, Category
from django.contrib.auth.models import User

class UserProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = UserProfile(id=1, name='John Doe',user = self.user,bio='test bio')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,UserProfile))

class PostTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post(id=1,title='Test',content='This is a test',user = self.user)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

class CommentTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post(id=1,title='Test',content='This is a test',user = self.user)
        self.comment = Comment(id=1,post=self.post,user=self.user, comment= 'This is a comment')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

class LocationTestClass(TestCase):
    #Setup method
    def setUp(self):
        self.location = Location(id=1,name='Test name')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

class CategoryTestClass(TestCase):
    #Setup method
    def setUp(self):
        self.category = Category(id=1,name='Test name')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

class NeighborhoodTestClass(TestCase):
    #Setup method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.location = Location(id=1,name='Test name')
        self.neighbourHood = NeighbourHood(id=1,name='Test name',location=self.location,occupants=1)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourHood,NeighbourHood))

    def test_create_neighborhood(self):
        self.location.save()
        self.neighbourHood.create_neighborhood()
        self.assertTrue(len(NeighbourHood.objects.all()) > 0)

    def test_delete_neighborhood(self):
        self.location.save()
        self.neighbourHood.create_neighborhood()
        self.neighbourHood = NeighbourHood.objects.get(id=1)
        self.neighbourHood.delete_neighborhood()
        self.assertTrue(len(NeighbourHood.objects.all()) == 0)

    def test_find_neighborhood(self):
        self.location.save()
        self.neighbourHood.create_neighborhood()
        self.searched_neighborhood = NeighbourHood.find_neighborhood(1)
        self.assertTrue(self.searched_neighborhood == self.neighbourHood)

    def test_update_neighborhood(self):
        self.location.save()
        self.neighbourHood.create_neighborhood()
        self.neighbourHood = NeighbourHood.objects.get(id=1)
        self.neighbourHood.name = 'Changed name'
        self.neighbourHood.update_neighborhood()
        self.updated_neighborhood = NeighbourHood.objects.get(id=1)
        self.assertEqual(self.updated_neighborhood.name,'Changed name')

    def test_update_occupants(self):
        self.location.save()
        self.neighbourHood.create_neighborhood()
        self.neighbourHood = NeighbourHood.objects.get(id=1)
        self.neighbourHood.update_occupants()
        self.updated_neighborhood = NeighbourHood.objects.get(id=1)
        self.assertTrue(self.updated_neighborhood.occupants == 2)

class BusinessTestClass(TestCase):
    #Setup method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = UserProfile(id=1, name='John Doe',user = self.user,bio='test bio')
        self.location = Location(id=1,name='Test name')
        self.neighbourhood = NeighbourHood(id=1,name='Test name',location=self.location,occupants=1)
        self.category = Category(id=1,name='Test name')
        self.business = Business(id=1,name='Test',user=self.profile,description='Test description',neighbourhood=self.neighbourhood,email='test@test.com')
        self.profile.save()
        self.location.save()
        self.neighbourhood.save()
        self.category.save()
        self.business.save()


    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def test_create_business(self):
        self.business.create_business()
        self.assertTrue(len(Business.objects.all()) > 0)

    def test_delete_business(self):
        self.business.delete_business()
        self.assertTrue(len(Business.objects.all()) == 0)

    def test_find_business(self):
        self.business = Business.find_business(1)
        self.assertEqual(self.business.id, 1)

    def test_update_business(self):
        self.business = Business.find_business(1)
        self.business.name = 'Changed name'
        self.business.update_business()
        self.updated_business = Business.find_business(1)
        self.assertEqual(self.updated_business.name, 'Changed name')