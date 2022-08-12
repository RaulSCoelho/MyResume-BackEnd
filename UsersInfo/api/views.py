from ..models import UserInfo, Address, SocialMedia, Qualification, Skill, Experience, Education
from .serializers import UserInfoSerializer, AddressSerializer, SocialMediaSerializer, QualificationSerializer, SkillSerializer, ExperienceSerializer, EducationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Users(request):
    if request.method == 'GET':
        users = UserInfo.objects.all()
        serializer = UserInfoSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getUser(request, UserId):   

    def getItem(model, key, type):
        if type == 'one':
            try:
                return model.objects.get(User_id=key)
            except model.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif type == 'many':
            try:
                return model.objects.filter(User_id=key)
            except model.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    user = getItem(UserInfo, UserId, 'one')
    address = getItem(Address, UserId, 'many')
    socialMedia = getItem(SocialMedia, UserId, 'many')
    qualification = getItem(Qualification, UserId, 'many')
    skill = getItem(Skill, UserId, 'many')
    experience = getItem(Experience, UserId, 'many')
    education = getItem(Education, UserId, 'many')

    if request.method == 'GET':
        userInfoSerializer = UserInfoSerializer(user)
        addressSerializer = AddressSerializer(address, many=True)
        socialMediaSerializer = SocialMediaSerializer(socialMedia, many=True)
        qualificationSerializer = QualificationSerializer(
            qualification, many=True)
        skillSerializer = SkillSerializer(skill, many=True)
        experienceSerializer = ExperienceSerializer(experience, many=True)
        educationSerializer = EducationSerializer(education, many=True)

        return Response({
            'user': userInfoSerializer.data,
            'address': addressSerializer.data,
            'socialMedias': socialMediaSerializer.data,
            'qualifications': qualificationSerializer.data,
            'skills': skillSerializer.data,
            'experience': experienceSerializer.data,
            'education': educationSerializer.data,
        })


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def editUser(request, UserId):

    def getItem(model, key, type):
        if type == 'one':
            try:
                return model.objects.get(User_id=key)
            except model.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif type == 'many':
            try:
                return model.objects.filter(User_id=key)
            except model.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    user = getItem(UserInfo, UserId, 'one')
    address = getItem(Address, UserId, 'many')
    socialMedia = getItem(SocialMedia, UserId, 'many')
    qualification = getItem(Qualification, UserId, 'many')
    skill = getItem(Skill, UserId, 'many')
    experience = getItem(Experience, UserId, 'many')
    education = getItem(Education, UserId, 'many')

    if request.method == 'PUT':
        def isValid(model):
            if model.is_valid():
                model.save()
            else:
                return Response(model.errors, status=status.HTTP_400_BAD_REQUEST)

        userInfoSerializer = UserInfoSerializer(user, data=request.data['user'])
        isValid(userInfoSerializer)
        addressSerializer = AddressSerializer(
            address, data=request.data['address'])
        isValid(addressSerializer)
        socialMediaSerializer = SocialMediaSerializer(
            socialMedia, data=request.data['socialMedias'])
        isValid(socialMediaSerializer)
        qualificationSerializer = QualificationSerializer(
            qualification, data=request.data['qualifications'])
        isValid(qualificationSerializer)
        skillSerializer = SkillSerializer(skill, data=request.data['skills'])
        isValid(skillSerializer)
        experienceSerializer = ExperienceSerializer(
            experience, data=request.data['experience'])
        isValid(experienceSerializer)
        educationSerializer = EducationSerializer(
            education, data=request.data['education'])
        isValid(educationSerializer)

        return Response({
            'user': userInfoSerializer.data,
            'address': addressSerializer.data,
            'socialMedias': socialMediaSerializer.data,
            'qualifications': qualificationSerializer.data,
            'skills': skillSerializer.data,
            'experience': experienceSerializer.data,
            'education': educationSerializer.data,
        })

    elif request.method == 'DELETE':
        user.delete()
        address.delete()
        socialMedia.delete()
        qualification.delete()
        skill.delete()
        experience.delete()
        education.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
