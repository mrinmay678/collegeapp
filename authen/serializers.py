from rest_framework import serializers
from .models import Student,Teacher,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=(
            'id',
            'jis_ID',
            'password',
            'is_student',
            'is_teacher',
        )
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, user_data):
        user=User.objects.create_user(**user_data)
        return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=(
            'id',
            'name',
            'jis_ID',
            'email',
            'dept',
            'year_of_passout',
            'current_semester',
            'university_roll_no',
            'university_registration_no',
            'mentor',
            'profile_picture',
        )

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=(
            'id',
            'name',
            'jis_ID',
            'email',
            'dept',
            'profile_picture',
        )