from django.db import models
from register.models import AppUser


class SavedStickman(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='saved_stickmen', null=True)
    payment_bool = models.BooleanField(default=False)
    stickman_name = models.CharField(max_length=20)
    stickman_clothes = models.JSONField()
    stickman_img_base64 = models.CharField(max_length=60000)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.stickman_name}"
