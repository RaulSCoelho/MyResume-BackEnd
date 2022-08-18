from asyncio.windows_events import NULL
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

    def getItem(model, key):
        try:
            return model.objects.filter(User_id=key)
        except model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    users = getItem(UserInfo, UserId)
    address = getItem(Address, UserId)
    socialMedias = getItem(SocialMedia, UserId)
    qualifications = getItem(Qualification, UserId)
    skills = getItem(Skill, UserId)
    experience = getItem(Experience, UserId)
    education = getItem(Education, UserId)

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

        response = {}

        def update(items, new, serializer, field):
            for item in items:
                try:
                    if item.id == new['id']:
                        customSerializer = serializer(item, data=new)

                        if customSerializer.is_valid():
                            customSerializer.save()
                            response[field] = customSerializer.data
                            break
                        else:
                            return Response(customSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
                except:
                    pass

        update(users, request.data['user'], UserInfoSerializer, 'user')
        update(address, request.data['address'], AddressSerializer, 'address')
        update(socialMedias, request.data['socialMedias'],
               SocialMediaSerializer, 'socialMedias')
        update(qualifications, request.data['qualifications'],
               QualificationSerializer, 'qualifications')
        update(skills, request.data['skills'], SkillSerializer, 'skills')
        update(experience, request.data['experience'],
               ExperienceSerializer, 'experience')
        update(education, request.data['education'],
               EducationSerializer, 'education')

        return Response(response)

    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# endregion
