from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import get_data
import re
class Index(APIView):
    def get(self,request):
        url=request.GET.get('url')
        sheet_id=re.findall('spreadsheets/d/([\w\-\.]+)',url)[0]
        data=get_data(sheet_id)
        return Response(data)

        
