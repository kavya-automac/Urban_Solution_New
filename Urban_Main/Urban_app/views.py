from rest_framework.decorators import api_view
from django.http import JsonResponse
from asgiref.sync import sync_to_async

# Create your views here.

@api_view(['GET'])
# @sync_to_async

def Dashboard(request):
    return JsonResponse({
        "Current": 20,"Power":27,"Temperature":30,"Humidity":20,
        "Start":"00:00:33","Cycle_Time":"00:00:00","Input_Load":41.8,"Actual_Weight":3.4,
         "Total_Power":19.843,"Alert_count":3,
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
