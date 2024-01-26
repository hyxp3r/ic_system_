from rest_framework import serializers

def validate_student(validate_student:str|None) -> None | serializers.ValidationError:
        if not validate_student:
            raise serializers.ValidationError({"detail": "Student not found"})