from django.contrib import sessions
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status, permissions, generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from wshop import settings
from apps import utils
from .serializers import UserProfileSerializer, LogoutSerializer
from .models import UserProfile
import re
import time


# 我的首页
class Profile(APIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        my_coupons = UserProfile.objects.get(id=request.user.id).couponuserrelation_set.filter(
            user_id=request.user.id)
        user = UserProfile.objects.get(id=request.user.id)
        received = my_coupons.count()
        save = 0
        for item in my_coupons:
            coupon = item.coupon
            save += coupon.price
        return Response(
            {'message': '操作成功', 'status': status.HTTP_200_OK,
             'data': {'username': user.username, 'mobile': user.mobile,
                      'received': received,
                      'save': save}})


# 个人资料
class ProfileDetail(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, pk=None):
        try:
            self.update(request)
            return Response({'message': '操作成功', 'status': status.HTTP_200_OK})
        except Exception:
            return Response({'message': Exception, 'status': status.HTTP_400_BAD_REQUEST})


# 验证手机号，发送验证码
class ValidateAuth(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        mob_number = request.query_params['mobile']
        if mob_number == "":
            return Response({'message': '请输入手机号', 'status': status.HTTP_400_BAD_REQUEST})
        if re.match(r'^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}', mob_number):
            try:
                UserProfile.objects.get(mobile=mob_number)
                return Response({'message': '手机号已经被注册', 'status': status.HTTP_400_BAD_REQUEST})
            except UserProfile.DoesNotExist:
                # TODO 发送短信验证码
                validate_code = utils.create_validate_code(request)
                msg_result = utils.send_message(settings.LUOSIMAO_AUTH,
                                                {'mobile': mob_number,
                                                 'message': validate_code + "，您的验证码在十分钟内有效。"})
                return Response({'message': '验证通过，短信发送成功。',
                                 'status': status.HTTP_200_OK, 'validate_code': validate_code})
                # if msg_result["error"] == 0:
                #     return Response({'message': '验证通过，短信发送成功。',
                #                      'status': status.HTTP_200_OK, 'mobile': mob_number})
                # else:
                #     return Response({'message': '短信发送失败。',
                #                      'status': status.HTTP_400_BAD_REQUEST})
        else:
            return Response({'message': '手机号格式不正确', 'status': status.HTTP_400_BAD_REQUEST})


# 注册
class Register(generics.CreateAPIView, generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        validate_code = request.query_params['validate_code']
        # validate_code = request.data.get('validate_code')
        # return Response({'data': request.data})
        if not validate_code == request.session['validate_code']['code']:
            return Response({'message': '验证码错误', 'status': status.HTTP_400_BAD_REQUEST})
        elif time.localtime(time.time() - request.session['validate_code']['time']).tm_min > 10:
            return Response({'message': '您的验证码已经过期', 'status': status.HTTP_400_BAD_REQUEST})
        else:
            try:

                user = UserProfile(username=request.query_params['username'],
                                   password=make_password(request.query_params['password']),
                                   mobile=request.query_params['mobile'],
                                   is_customer=1 if request.query_params['type'] == 1 else 0)
                user.save()
                return Response({'message': '注册成功', 'status': status.HTTP_200_OK})
            except Exception:
                return Response({'message': Exception, 'status': status.HTTP_400_BAD_REQUEST})


# 登录
class Login(APIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request):
        try:
            username = request.query_params.get('username')
            password = request.query_params.get('password')
            if not username or not password:
                return Response({'message': '用户名和密码是必填的。', 'status': status.HTTP_400_BAD_REQUEST})
            user = UserProfile.objects.get(is_customer__gte=0, username=username)
            if user.check_password(raw_password=password):
                serializer = UserProfileSerializer(user)
                # request.user = user
                login(request, user)
                return Response({'message': '登录成功', 'csrf': request.session, 'status': status.HTTP_200_OK,
                                 'data': serializer.data})
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': '密码错误'})
        except UserProfile.DoesNotExist:
            return Response({'message': '当前账号不存在', 'status': status.HTTP_400_BAD_REQUEST})


# 注销
class Logout(APIView):
    queryset = UserProfile.objects.all()
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        logout(request)
        return Response(
            {'message': '注销成功', 'status': status.HTTP_200_OK, 'request_user': LogoutSerializer(request.user).data})


class GetService(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = UserProfile.objects.get(is_customer=-1)
        if user:
            return Response(
                {'data': {'username': user.username, 'mobile': user.mobile}, 'status': status.HTTP_200_OK}, )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
