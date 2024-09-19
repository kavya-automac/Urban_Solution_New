from rest_framework.decorators import api_view
from django.http import JsonResponse, request
from asgiref.sync import sync_to_async
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET'])
# @sync_to_async

def Dashboard(request):
    print('...')
    return JsonResponse({
        "Current": 20,"Power":27,"Temperature":30,"Humidity":20,"Cycle":"ON","Door":"CLOSED",
        "Start":"00:00:33","Cycle_Time":"00:00:00","Input_Load":41.8,"Actual_Weight":3.4,
         "Total_Power":19.843,"Alerts":[{"Timestamp":"2024-09-18T07:58:24Z","alert_status":"Overload"},
                                        {"Timestamp":"2024-09-18T07:58:24Z","alert_status":"Overload"},
                                        {"Timestamp": "2024-09-18T07:58:24Z", "alert_status": "Overload"},
                                        {"Timestamp": "2024-09-18T07:58:24Z", "alert_status": "Overload"},
                                        {"Timestamp": "2024-09-18T07:58:24Z", "alert_status": "Overload"}
                                        ],
        "graph_data":{
            "title":"Temperature",
            "labels": {
                       "x_label": "Timestamp",
                       "y_label": "°C",
                "data":[
                    {
                    "x_axis_data":"2024-09-18T07:58:24Z",
                    "y_axis_data":20
                    },
                    {
                        "x_axis_data": "2024-09-18T07:58:24Z",
                        "y_axis_data": 30
                    },
                    {
                        "x_axis_data": "2024-09-18T07:58:24Z",
                        "y_axis_data": 35
                    },
                    {
                        "x_axis_data": "2024-09-18T07:58:24Z",
                        "y_axis_data": 40
                    },

                    ]
                        },


                        }
    }
    )





class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

@api_view(('POST',))
def logout_view(request):
    """Blacklist the refresh token: extract token from the header
      during logout request user and refresh token is provided"""
    print("-------logout")
    Rtoken = request.data["refresh_token"]
    token = RefreshToken(Rtoken)
    token.blacklist()
    return JsonResponse({"status":"Successful Logout"} ,status=status.HTTP_200_OK)