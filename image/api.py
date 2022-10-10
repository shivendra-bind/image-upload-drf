from urllib import request
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.parsers import MultiPartParser, FormParser
from pathlib import Path

from .models import Image
class ImageUploadAPIVIew(GenericAPIView):
    parser_classes = (MultiPartParser, FormParser)

    class ImageSerializer(serializers.ModelSerializer):
        name = serializers.CharField(required=False)
        class Meta:
            model = Image
            fields = '__all__'
        # def validate(self, attrs):
        #     name = attrs.get('name', None)
        #     if name is None:
        #         path = Path(attrs.get('image'))
        #         attrs['name'] = path.stem
        #     return super().validate(attrs)
        

    def post(self, request, *args, **kwargs):
        serialiser =  self.ImageSerializer(data=request.data)
        serialiser.is_valid(raise_exception=True)
        img = serialiser.save()
        url = request.build_absolute_uri(img.image.url)
        ctx = serialiser.data
        ctx['url'] = url
        return Response(ctx,status=status.HTTP_200_OK)