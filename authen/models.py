from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.hashers import make_password
from collegeapp.settings import SECRET_KEY

class CustomUserManager(BaseUserManager):
    def _create_user(self, jis_ID, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not jis_ID:
            raise ValueError('The given username must be set')
        user = self.model(jis_ID = jis_ID, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_user(self, jis_ID, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(jis_ID, password, **extra_fields)

    def create_superuser(self, jis_ID, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(jis_ID, password, **extra_fields)


class User(AbstractBaseUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    jis_ID=models.CharField(default=None,max_length=20,blank=False,unique=True)
    email=models.EmailField(default=None,max_length=254,blank=True)
    dept=models.CharField(max_length=30,blank=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'jis_ID'

class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=200,blank=False)
    profile_picture = models.ImageField(default=None,upload_to='Images/Teachers', height_field=None, width_field=None,blank=True)    
    def __str__(self):
        return self.name

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    present_year=date.today().year
    year=(
        (present_year,present_year),
        (present_year+1,present_year+1),
        (present_year+2,present_year+2),
        (present_year+3,present_year+3),
        (present_year+4,present_year+4),
    )
    sem=(
        ("1st Semester","1st Semester"),
        ("2nd Semester","2nd Semester"),
        ("3rd Semester","3rd Semester"),
        ("4th Semester","4th Semester"),
        ("5th Semester","5th Semester"),
        ("6th Semester","6th Semester"),
        ("7th Semester","7th Semester"),
        ("8th Semester","8th Semester"),    
    )
    name=models.CharField(max_length=200,blank=False)
    year_of_passout=models.IntegerField(default=None,choices=year,blank=False)
    current_semester=models.CharField(default=None,max_length=15,choices=sem,blank=False)
    university_roll_no=models.IntegerField(default=None,blank=False)
    university_registration_no=models.IntegerField(default=None,blank=False)
    mentor=models.ForeignKey(Teacher,on_delete=models.DO_NOTHING)
    profile_picture = models.ImageField(default=None,upload_to='Images/Students', height_field=None, width_field=None,blank=True)

    def __str__(self):
        return self.name