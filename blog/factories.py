import factory
from factory import django 

class UserFactory(django.DjangoModelFactory):
    class Meta:
        model= "auth.User"
        django_get_or_create = ("username", )

    username= "ariel"


class PostFactory(django.DjangoModelFactory):
    class Meta:
        model= "blog.Post"
    
    text= factory.Faker("paragraph", nb_sentences=50)
    author= factory.SubFactory(UserFactory)
    title= factory.Faker("sentence")

