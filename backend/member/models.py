from django.db import models
from django.urls import reverse_lazy


class Member(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse_lazy('member:member_detail', kwargs={'pk': self.pk})
