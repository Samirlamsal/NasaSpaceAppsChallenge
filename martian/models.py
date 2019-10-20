from django.db import models
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField



class entry(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Country = CountryField()
    Email = models.CharField(max_length=50)
    Destination = MultiSelectField(choices=[('Pluto','Pluto'), ('Charon','Charon'), ('Nix','Nix'), ('Hydra','Hydra'),('Kerberos','Kerberos'),('Styx','Styx'),('Ceres','Ceres'), ('MakeMake','MakeMake'),('Haumea','Haumea'),('Hiaka','Hiaka'),('Namaka','Namaka'),('Eris','Eris'),('Dysnomia','Dysnomia')])
    Purpose = MultiSelectField(choices=[('Adventure','Adventure'), ('Research','Research'), ('Recreation','Recreation'),('Others', 'Others')])

    def __str__(self):
        return self.Name
