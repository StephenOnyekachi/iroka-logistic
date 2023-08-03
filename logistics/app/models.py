from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver

# Create your models here.

# class Users(models.Model):
class Users(AbstractUser):
    #name = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # models.CharField(max_length=100, blank=True, null=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    number = models.IntegerField(default=0, null=True)
    block = models.BooleanField(default=False)
    address = models.TextField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.username


# @ receiver(post_save, sender=User)
# def save_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Users.objects.create(name=instance)
#         Users.save()

class Comment(models.Model):
    name = models.TextField()
    message = models.TextField()
    time = models.DateTimeField(verbose_name="last login", auto_now=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.TextField()
    message = models.TextField()
    email = models.TextField()
    time = models.DateTimeField(verbose_name="last login", auto_now=True)

    def __str__(self):
        return self.name

class Items(models.Model):
    # for sender
    sender_name = models.TextField()
    sender_address = models.TextField()
    sender_number = models.IntegerField()

    # for receiver
    receiver_name = models.TextField()
    receiver_address = models.TextField()
    receiver_number = models.IntegerField()

    # for company
    item = models.TextField()
    weight = models.IntegerField()
    pickup_time = models.TimeField()
    pickup_date = models.DateTimeField()
    destination = models.TextField()
    peparted_time = models.TimeField(verbose_name="last login", auto_now=True)
    freight = models.TextField()
    booking_mode = models.TextField()
    qnty = models.TextField()
    invoice_no = models.TextField()
    consignment = models.TextField()
    consignment_no = models.TextField()
    delivered = models.BooleanField(default=False)






