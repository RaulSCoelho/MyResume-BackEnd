from rest_framework import serializers
from ..models import UserInfo, Address, SocialMedia, Qualification, Skill, Experience, Education


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = [
            'User_id',  
            'FirstName',
            'LastName',
            'BirthDate',
            'PhoneNumber',
            'Email',
            'CPF',
            'Citizenship',
            'MaritalStatus',
            'Profession',
            'Education',
            'About',
            'Experience'
        ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'User_id',
            'Street',
            'StreetNumber',
            'Complement',
            'ZipCode',
            'City',
            'State',
            'Country',
            'Neighborhood'
        ]


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = [
            'User_id',
            'Name',
            'Link'
        ]


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = [
            'User_id',
            'Qualification'
        ]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            'User_id',
            'Skill'
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'User_id',
            'Company',
            'Location',
            'Occupation',
            'Description',
            'Period'
        ]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'User_id',
            'College',
            'Course',
            'Period',
            'Shift',
            'Description'
        ]
