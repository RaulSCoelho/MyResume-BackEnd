from ..models import UserInfo, Address, SocialMedia, Qualification, Skill, Experience, Education
from .serializers import UserInfoSerializer, AddressSerializer, SocialMediaSerializer, QualificationSerializer, SkillSerializer, ExperienceSerializer, EducationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
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


# region ALL THE USERS LIST
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
# endregion


# region ONLY ONE USER
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def User(request, UserId):

    def getItemById(model, key):
        try:
            return model.objects.get(id=key)
        except model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def getItemByUserId(model, key):
        try:
            return model.objects.filter(User_id=key)
        except model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    users = getItemByUserId(UserInfo, UserId)
    address = getItemByUserId(Address, UserId)
    socialMedias = getItemByUserId(SocialMedia, UserId)
    qualifications = getItemByUserId(Qualification, UserId)
    skills = getItemByUserId(Skill, UserId)
    experience = getItemByUserId(Experience, UserId)
    education = getItemByUserId(Education, UserId)

    if request.method == 'GET':
        usersInfoSerializer = UserInfoSerializer(users, many=True)
        addressSerializer = AddressSerializer(address, many=True)
        socialMediaSerializer = SocialMediaSerializer(socialMedias, many=True)
        qualificationSerializer = QualificationSerializer(
            qualifications, many=True)
        skillSerializer = SkillSerializer(skills, many=True)
        experienceSerializer = ExperienceSerializer(experience, many=True)
        educationSerializer = EducationSerializer(education, many=True)

        return Response({
            'user': usersInfoSerializer.data,
            'address': addressSerializer.data,
            'socialMedias': socialMediaSerializer.data,
            'qualifications': qualificationSerializer.data,
            'skills': skillSerializer.data,
            'experience': experienceSerializer.data,
            'education': educationSerializer.data,
        })

    elif request.method == 'POST':

        def post(new, serializer):
            customSerializer = serializer(data=new)
            if customSerializer.is_valid():
                customSerializer.save()
                return customSerializer.data

        for [key, value] in request.data.items():
            if key == 'user':
                response = post(value, UserInfoSerializer)

            elif key == 'address':
                response = post(value, AddressSerializer)

            elif key == 'socialMedias':
                response = post(value, SocialMediaSerializer)

            elif key == 'qualifications':
                response = post(value, QualificationSerializer)

            elif key == 'skills':
                response = post(value, SkillSerializer)

            elif key == 'experience':
                response = post(value, ExperienceSerializer)

            elif key == 'education':
                response = post(value, EducationSerializer)
                
        return Response(response, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':

        def update(model, serializer, new, field):
            old = getItemById(model, new['id'])
            customSerializer = serializer(old, data=new)

            if customSerializer.is_valid():
                customSerializer.save()
                response[field] = customSerializer.data
            else:
                return Response(customSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        response = {}

        for [key, value] in request.data.items():
            if key == 'user':
                update(UserInfo, UserInfoSerializer, value, key)

            elif key == 'address':
                update(Address, AddressSerializer, value, key)

            elif key == 'socialMedias':
                update(SocialMedia, SocialMediaSerializer, value, key)

            elif key == 'qualifications':
                update(Qualification, QualificationSerializer, value, key)

            elif key == 'skills':
                update(Skill, SkillSerializer, value, key)

            elif key == 'experience':
                update(Experience, ExperienceSerializer, value, key)

            elif key == 'education':
                update(Education, EducationSerializer, value, key)

        return Response(response)

    elif request.method == 'DELETE':
        
        def delete(model, value):
            item = getItemById(model, value['id'])
            item.delete()

        for [key, value] in request.data.items():
            if key == 'user':
                users.delete()

            elif key == 'address':
                delete(Address, value)

            elif key == 'socialMedias':
                delete(SocialMedia, value)

            elif key == 'qualifications':
                delete(Qualification, value)

            elif key == 'skills':
                delete(Skill, value)

            elif key == 'experience':
                delete(Experience, value)

            elif key == 'education':
                delete(Education, value)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
# endregion
