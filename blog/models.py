from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400, blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    photo = models.ImageField(
        upload_to='post/pictures',
        blank=True,
        null=True
    )
    video = models.URLField(max_length=500,
    blank=True,
    null=True
    )
    
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Post, self).save(*args, **kwargs)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    
    
    
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Video(models.Model):
    name= models.CharField(max_length=500)
    file= models.FileField(upload_to='post/pictures', null=True, verbose_name="Trailer")
    
    
