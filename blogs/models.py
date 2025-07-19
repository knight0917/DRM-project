from django.db import models



# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField()

    def __str__(self):
        return self.blog_title 
    

class Comment(models.Model):
    #on delete using because if blog post gets deleted comment must be deleted
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')  
    commnet = models.TextField()

    def __str__(self):
        return self.comment