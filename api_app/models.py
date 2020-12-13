from django.db import models
from django.contrib.auth.models import User
from . import scholarly_api, scopus_api, ieee_api



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

    def save(self, *args, **kwargs):

        titles = scholarly_api.get_pubs_titles(self.name)
        print(titles)

        scholarly_api.get_gs_data(self.name, titles)
        #
        scopus_api.get_scopus_data(titles)
        #
        ieee_api.get_ieee_data(titles)

        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.name


class Paper(models.Model):
    # authorID = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    # DOI = models.CharField(max_length=50, unique=True, null=True, blank=True)
    co_author = models.CharField(max_length=500)
    citations_google_scholar = models.IntegerField(default=0)
    citations_ieee = models.IntegerField(default=0)
    citations_scopus = models.IntegerField(default=0)
    citations_researchgate = models.IntegerField(default=0)
    citations_webofscience = models.IntegerField(default=0)
    fields = models.CharField(max_length=100, null=True, blank=True)
    publication_year = models.IntegerField()
    publisher_name = models.CharField(max_length=100, null=True, blank=True)
    abstract = models.CharField(max_length=2000, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)


    def update_citation(self):
        pass
        # TODO: add logic to update citation

    def get_authors(self):
        return str(self.co_author).split(', ')

    def __str__(self):
        return self.title
