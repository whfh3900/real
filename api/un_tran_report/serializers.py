# serializers.py
from rest_framework import serializers
from .models import UserInfo, Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        # fields = '__all__'
        fields = ['bas_ym', 'age_dc', 'gender', 'bas_dt', 'tran_md', 'ats_kdcd_dtl', 'dps_trn_am', 'text_1']


class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
