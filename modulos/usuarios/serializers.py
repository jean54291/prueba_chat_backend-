from rest_framework import serializers
from modulos.usuarios.models import Usuario

class PersonaSerializer (serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    en_linea= serializers.ReadOnlyField()
    fecha_ultima_sesion= serializers.ReadOnlyField()

    def create(self, validate_data):        
        self.validar_usuario(validate_data.get('username'))
        persona = Usuario()
        # persona.id = validate_data.get('id')
        persona.first_name = validate_data.get('first_name')
        persona.last_name = validate_data.get('last_name')
        persona.username = validate_data.get('username')
        persona.email = validate_data.get('email')
        persona.set_password(validate_data.get('password'))
        persona.save()
        return persona
        


    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validar_usuario(self, data):
        persona = Usuario.objects.filter(username = data)
        if len(persona) != 0:
            raise serializers.ValidationError("Ya existe la persona registrada")
        else:
            return data

    class Meta:
        model = Usuario
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email'
        )