from rest_framework.response import Response
from rest_framework import status


class ApiResponser():
 def successResponse(data,respon = status.HTTP_200_OK,message='',event=''):
  return Response({"status":"success","data":data,"message":message,"event":event}, status=respon)

 def failedResponse(data,respon=status.HTTP_400_BAD_REQUEST,message='',event=''):
  return Response({"status":"error","data":data,"message":message,"event":event}, status=respon)