from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validation(self, email, password, conf_password, name, username, b_day):
        fields=[]
        if not EMAIL_REGEX.match(email):
            print ("Email NOT valid")
            fields.append("Email invalid")
        if len(name) < 3:
            print ('Name must be entered')
            fields.append('Name must be entered')
        if len(username) < 3:
            print ('username must be entered')
            fields.append('Username must be entered')
        if len(password) < 8:
            print ('password must be at least 8 characters')
            fields.append('Password must be at least 8 characters')
        if password != conf_password:
            print ('Make sure password confirmation matches')
            fields.append('Make sure password confirmation matches')
        if fields:
            return fields

    def login(self, email, entered_pw):
        l_fields=[]
        print "at login"
        try:
            user = Users.objects.get(email=email)#select * from users where #email = email
            print user
            if user.pw_hash == bcrypt.hashpw(entered_pw.encode(), user.pw_hash.encode()):
                l_fields.append("success!")
                print ('password match confirmed')
                return user
            else:
                l_fields.append("Incorrect password")
        except:
            l_fields.append("Email does not match our records")
        return l_fields

class Users(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    pw_hash=models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    b_day = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()

class Trips(models.Model):
    user = models.ForeignKey(Users)
    destination = models.CharField(max_length=255)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Groups(models.Model):
    trip = models.ForeignKey(Trips)
    guest = models.ForeignKey(Users)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __unicode__(self):
    return "id: " + str(self.id) + ", email: " + self.email