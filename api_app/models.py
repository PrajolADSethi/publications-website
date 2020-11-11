from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class College(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    clgID = models.BigIntegerField(blank=False,null=False) #doubt
    website = models.URLField(max_length=200,**options)

class Department(models.Model):

    collegeID = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    deptID = models.BigIntegerField(blank=False,null=False)

class Author(models.Model):

    deptartment = models.ForeignKey(Department, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # college = models.OneToOneField(College, on_delete=models.SET_NULL)
    name = model.CharField(max_length=100)
    userID = models.BigIntegerField(blank=False,null=False)
    ORCid = models.BigIntegerField()
    scopusID= models.BigIntegerField()
    bio = models.CharField(max_length=1000)
    affiliation = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    phoneno = models.BigIntegerField(blank=True,null=True)
    weblinks = models.URLField(max_length=200,**options)
    designation = models.CharField(max_length=100)
    # username = models.CharField(max_length=100)
    # password =



class Paper(models.Model):
    authorID = models.ForeignKey(Author, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    DOI = models.CharField(max_length=50, primary_key=True, unique=True)
    pri_author = models.CharField(max_length=100)
    citation = models.IntegerField()
    fields = models.CharField(max_length=100)
    publication_date = models.TimeField(auto_now=False, auto_now_add=False, **options)
    publish_name = models.CharField(max_length=100)
    abstract = models.CharField(max_length=1000)
    # tags =
