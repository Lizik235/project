from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class Advertisement(models.Model):
    title = models.CharField(max_length=80, verbose_name="заголовок")
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=12, decimal_places=2)
    auction = models.BooleanField("возможность торга", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField("дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "advertisements"

    def __str__(self):
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})"
