from django.db import models
from ..common.models import BaseModel
from ckeditor.fields import RichTextField
from apps.user.models import CustomUser


class Contact(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_contact')
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    web_site = models.URLField(max_length=255)
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    message = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Biz bilan aloqa"
        verbose_name_plural = "Biz bilan aloqa"