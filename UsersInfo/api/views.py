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

    elif request.method == 'POST':
        for [key, value] in request.data.items():
            print(f'{key}: {value}')

    elif request.method == 'PUT':

        serializer = UserInfoSerializer(user, data=request.data['user'])

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# endregion
