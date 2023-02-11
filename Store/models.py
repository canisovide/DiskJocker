from django.db import models


class Artiste(models.Model):
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)


class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # un contact peut laisser un message sur la plateforme
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)


class Genre(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Type(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Disque(models.Model):
    titre = models.CharField(max_length=255)
    reference = models.IntegerField(blank=True, null=True)
    quantite = models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='file/images/disque')
    appreciation = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    parition = models.DateField(null=True, blank=True)
    continent = models.CharField(max_length = 255, blank=True, null = True)
    pays = models.CharField(max_length = 255, blank=True, null = True)
    # relation entre un disque et les artistes
    artistes = models.ManyToManyField(Artiste, related_name='disques', blank=True)
    played = models.IntegerField(default=0)
    # relation entre un disque et un genre musical
    genre = models.ManyToManyField(Genre,related_name = "genres", blank = True)
    # relation entre un disque et un type (album, mixtape, compilation, EP, etc.
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.titre


class Chanson(models.Model):
    titre = models.CharField(max_length=255)
    path = models.FileField(upload_to='file/audios/chanson')
    # une chanson est chanté par un ou plusieurs artiste(s)
    artistes = models.ManyToManyField(Artiste, related_name='chansons', blank=True)
    # une chanson est necessairement présent sur un disque
    disque = models.ForeignKey(Disque, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.titre
    


class Booking(models.Model):
    contacted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    disque = models.ForeignKey(Disque, on_delete=models.CASCADE, null=True)
    quantite = models.IntegerField(default=1)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)


class DiskJocker(models.Model):
    nom = models.CharField(max_length=255)
    logo = models.ImageField(blank=True, null=True, upload_to="file/images/diskjocker")
    banniere_Img = models.ImageField(blank=True, null=True, upload_to="file/images/diskjocker")
    banniere_Vid = models.FileField(blank=True, null=True, upload_to="file/videos/diskjocker")
    def __str__(self):
        return self.nom
    
class Banniere(models.Model):
    nom = models.CharField(max_length = 255)
    image = models.ImageField(upload_to="file/frontend/images/diskjocker")
    def __str__(self):
        return self.nom
    
