from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class College(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Department(models.Model):

    collegeID = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # deptID = models.BigIntegerField(blank=False,null=False)

    def __str__(self):
        return f'{self.collegeID.name} => {self.name}'

class Author(models.Model):

    deptartment = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    ORCid = models.CharField(max_length=19,null=True,blank=True)
    scopusID= models.BigIntegerField(null=True, blank=True)
    bio = models.CharField(max_length=1000)
    affiliation = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    phoneno = models.BigIntegerField(blank=True,null=True)
    weblinks = models.CharField(max_length=200 ,null=True,blank=True)
    designation = models.CharField(max_length=100)
    # username = models.CharField(max_length=100)
    # password =
    def __str__(self):
        return self.name


class Paper(models.Model):
    # authorID = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    DOI = models.CharField(max_length=50, primary_key=True, unique=True)
    co_author = models.CharField(max_length=500)
    citation = models.IntegerField()
    fields = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    publisher_name = models.CharField(max_length=100)
    abstract = models.CharField(max_length=2000)


    def update_citation(self):
        pass
        # TODO: add logig to update citation
    def __str__(self):
        return self.title
        
