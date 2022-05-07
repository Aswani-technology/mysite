from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['firstname'].isalpha()) == False:
            if len(postData['firstname']) < 2:
                errors['firstname'] = "First name can not be shorter than 2 characters"

        if (postData['lastname'].isalpha()) == False:
            if len(postData['lastname']) < 2:
                errors['lastname'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()