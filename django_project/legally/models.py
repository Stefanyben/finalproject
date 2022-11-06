from django.db import models

class Firms(models.Model):
    firm_name = models.CharField('Firm Name', max_length=120)
    region = models.CharField('Region', max_length=120)

    def __str__(self):
        return self.firm_name

class Speciality(models.Model):
    s_name = models.CharField('Speciality', max_length=120)

    def __str__(self):
        return self.s_name

class Attorneys(models.Model):
    name = models.CharField('Name', max_length=120)
    gender = models.CharField('Gender', max_length=10)
    speciality = models.ForeignKey(Speciality, blank=True, null=True, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firms, blank=True,null=True, on_delete=models.CASCADE)
    rate = models.CharField('Rate', max_length=10)
    years = models.CharField('Years of practice', max_length=10)
    state = models.CharField('State', max_length=120)
    country = models.CharField('Country located', max_length=120)

    def __str__(self):
        return self.name