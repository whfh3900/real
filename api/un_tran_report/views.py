from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserinfoSerializer, TransactionSerializer
from .models import UserInfo, Transaction
from UTD.utd import UniqueTransactionDetect
utd = UniqueTransactionDetect()

# Create your views here.
class UserInfoViewAPI(APIView):

    # 전체 가져오기(viewsets.ModelViewSet)
    # def list(self, request):
    #     queryset = UserInfo.objects.all()
    #     serializer = UserinfoSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # # 해당 pk만 가져오기
    # def retrieve(self, request, pk=None):
    #     queryset = UserInfo.objects.all()
    #     item = get_object_or_404(queryset, pk=pk)
    #     serializer = UserinfoSerializer(item)
    #     return Response(serializer.data)

    # APIView
    def get(self, request, pk=None):
        try:
            queryset = UserInfo.objects.all()
            item = get_object_or_404(queryset, pk=pk)
            serializer = UserinfoSerializer(item)

            # 정상 작동
            return Response({"result": serializer.data, "state": 200, "error": None}, status=status.HTTP_200_OK)

        except Exception as e:
            # url이 잘못 됬을때(user_info 에 없는 UID)
            return Response({"result": None, "state": 404, "error": "No UID matches the given query."}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request, pk=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()

            # 해당 User 데이터 가져오기
            try:
                tran_use = UserInfo.objects.filter(uid=pk).values()[0]
            except Exception as e:
                # serializer 형식 및 url이 잘못 됬을때(user_info 에 없는 UID)
                return Response({"result": None, "state": 404, "error": "No UID matches the given query."},


            # 거래유형
            result = utd.predict_result(serializer.data)
            if type(result) is dict:
                # 데이터 형식이 잘못 됬을때
                return Response({"result": None, "state": 400, "error": result},
                                status=status.HTTP_400_BAD_REQUEST)


            # 특이거래 여부
            if tran_use[result] != 0:
                detection_result = False
            else:
                detection_result = True

            # UserInfo 업데이트
            tran_use[result] = tran_use[result]+1
            get_uid = UserInfo.objects.get(uid=pk)

            get_uid.c1 = tran_use["c1"]
            get_uid.c2 = tran_use["c2"]
            get_uid.c3 = tran_use["c3"]
            get_uid.c4 = tran_use["c4"]
            get_uid.c5 = tran_use["c5"]
            get_uid.c6 = tran_use["c6"]
            get_uid.c7 = tran_use["c7"]
            get_uid.c8 = tran_use["c8"]
            get_uid.c9 = tran_use["c9"]
            get_uid.c10 = tran_use["c10"]
            get_uid.c11 = tran_use["c11"]
            get_uid.c12 = tran_use["c12"]
            get_uid.save()

            # Transaction 추가
            Transaction.objects.create(bas_ym=serializer.data['bas_ym'], \
                                       age_dc=serializer.data['age_dc'], \
                                       gender=serializer.data['gender'], \
                                       bas_dt=serializer.data['bas_dt'], \
                                       tran_md=serializer.data['tran_md'], \
                                       ats_kdcd_dtl=serializer.data['ats_kdcd_dtl'], \
                                       dps_trn_am=serializer.data['dps_trn_am'], \
                                       text_1=serializer.data['text_1'], \
                                       user_info_uid=get_uid, \
                                       result=result)

            # 정상 작동
            return Response({"result": detection_result, "state": 201, "error": None}, status=status.HTTP_201_CREATED)

        else:
            # key나 value가 잘못 됬을때(serializer)
            return Response({"result": None, "state": 400, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
