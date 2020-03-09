from django.db import models

class User(models.Model):
    def __repr__(self):
        return f"<User object:{self.id} {self.first_name} {self.last_name} {self.email} {self.age}>"

    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)     
    email = models.CharField(max_length = 255)
    age = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 