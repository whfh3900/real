from rest_framework import serializers
from .models import UserInfo, Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        # fields = '__all__'
        fields = ['bas_ym', 'age_dc', 'gender', 'bas_dt', 'tran_md', 'ats_kdcd_dtl', 'dps_trn_am', 'text_1']


class UserinfoSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer(many=True)
    class Meta:
        model = UserInfo
        fields = ('uid', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'note', 'transaction')

    # def to_representation(self, instance):
    #     self.Meta.depth = 1
    #     return super().to_representation(instance)