from rest_framework import serializers

from .models import AccountsReceivable
def validate_personal_number(personal_number):

        try:
            personal_number = int(personal_number)
        except:
            raise serializers.ValidationError("Personal number must be integer")

class PersonalNumber(serializers.Serializer):
    personal_number = serializers.CharField(min_length = 1, max_length = 6, validators=[validate_personal_number])


class DebtSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountsReceivable
        fields = [
                "fio", 
                "personal_number",
                "contract_number",
                "accounts_receivable",
                "file_created_time"]
        
    

        
