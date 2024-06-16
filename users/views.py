import email
from tokenize import TokenError

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

from users.models import User


class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        # 自定义登录成功
        result = serializer.validated_data
        result['mobile'] = serializer.user.mobile
        result['email'] = serializer.user.email
        result['username'] = serializer.user.username
        result['token'] = result.pop('access')
        result['id'] = serializer.user.id
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RegisterView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not all([email, password]):
            return Response({'msg':'用户名和密码不能为空'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'msg':'用户已存在'}, status=status.HTTP_400_BAD_REQUEST)
        if 8 > len(password) | len(password) > 16:
            return Response({'msg': '密码长度不够'}, status=status.HTTP_400_BAD_REQUEST)
        user = User(email=email, username=email, password=password,is_superuser=False)
        user.save()
        res = {
            'username': user.username,
            'mobile': user.mobile,
            'email': user.email,
        }
        return Response(res, status=status.HTTP_200_OK)
