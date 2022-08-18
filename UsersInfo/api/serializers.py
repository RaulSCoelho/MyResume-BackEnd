from importlib.metadata import requires
from rest_framework import serializers
from ..models import UserInfo, Address, SocialMedia, Qualification, Skill, Experience, Education


class UserInfoSerializer(serializers.ModelSerializer):
    User_id = serializers.IntegerField(required=False)

    class Meta:
        model = UserInfo
        fields = [
            'id',
            'User_id', 
            'Lang',
            'FirstName',
            'LastName',
            'BirthDate',
            'PhoneNumber',
            'Email',
            'CPF',
            'Citizenship',
            'MaritalStatus',
            'About',
        ]


class AddressSerializer(serializers.ModelSerializer):
    User_id = serializers.IntegerField(required=False)

    class Meta:
        model = Address
        fields = [
            'id',
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
    User_id = serializers.IntegerField(required=False)

    class Meta:
        model = SocialMedia
        fields = [
            'id',
            'User_id',
            'Name',
            'Link'
        ]


class QualificationSerializer(serializers.ModelSerializer):
    User_id = serializers.IntegerField(required=False)

    class Meta:
        model = Qualification
        fields = [
            'id',
            'User_id',
            'Lang',
            'Qualification'
        ]


class SkillSerializer(serializers.ModelSerializer):
    User_id = serializers.IntegerField(required=False)

    class Meta:
        model = Skill
        fields = [
            'id',
            'User_id',
            'Skill'
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    User_id = serializers.IntegerField(required=False)

    class Meta:
        model = Experience
        fields = [
            'id',
            'User_id',
            'Lang',
            'Company',
            'Location',
            'Occupation',
            'Description',
            'Period'
        ]


class EducationSerializer(serializers.ModelSerializer):
    User_id = serializers.IntegerField(required=False)

    class Meta:
        model = Education
        fields = [
            'id',
            'User_id',
            'Lang',
            'College',
            'Course',
            'Period',
            'Shift',
            'Description'
        ]
