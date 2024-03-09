from django.db import models






class InfoOtika(models.Model):
    name = models.CharField(max_length=100)
    hiz = models.DecimalField(max_digits=10, decimal_places=2)
    ivme = models.DecimalField(max_digits=10, decimal_places=2)
    rotasyon = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.TimeField()
    ilac = models.IntegerField()
    batarya = models.IntegerField()
    akim = models.DecimalField(max_digits=10, decimal_places=2)
    derece = models.DecimalField(max_digits=10, decimal_places=2)
    imha_bitkiler = models.IntegerField()
    asilan_engeller = models.IntegerField()
    durdur = models.BooleanField()
    bitki_resim = models.ImageField(upload_to='static/images')
    x_ekseni = models.DecimalField(max_digits=10, decimal_places=4)
    y_ekseni = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return self.name
