import datetime
import json

from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from asgiref.sync import sync_to_async
from .models import *
from .serializers import *
# Create your views here.

# @api_view(['GET'])
@sync_to_async

def Dashboard():
    print('...')

    dash_res={
    "Current": 20,
    "Power": 27,
    "Temperature": 30,
    "Humidity": 20,
    "Cycle": "ON",
    "Door": "CLOSED",
    "Start": "00:00:33",
    "Cycle_Time": "00:00:00",
    "Input_Load": 41.8,
    "Output_load": 3.4,
    "Total_Power": 19.843,
    "Alerts": {
        "Timestamp": "2024-09-18T07:58:24Z",
        "alert_status": "Overload"
      },

    "graph_data": {
      "title": "Temperature",
      "labels": {
        "x_label": "Timestamp",
        "y_label": "°C"
      },
      "data": {
          "x_axis_data": "2024-09-18T07:58:24Z",
          "y_axis_data": 20
        },

    },
    "Updated_timestamp": "2024-09-18T07:58:24Z"
  }




    return dash_res
    # return JsonResponse({"dash_res":dash_res})


@api_view(['POST'])

def Reports(request):
    start_datetime = request.data.get('start_datetime')
    end_datetime = request.data.get('end_datetime')
    report_type_f = request.data.get("Report_type")
    try:
        start_datetime = datetime.datetime.strptime(start_datetime, '%Y-%m-%d')
        # print('try  start_datetime',start_datetime)

        # end_datetime = datetime.datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')
        end_datetime_strp = datetime.datetime.strptime(end_datetime, '%Y-%m-%d')
        end_datetime = end_datetime_strp + datetime.timedelta(days=1)
        # print('after increment end_datetime',end_datetime)
        if report_type_f == "Compost_Report":
            query_data = Reports_data.objects.filter(Timestamp__range=[start_datetime, end_datetime])
            # print("query_data",query_data)
            query_serializer =ReportsSerializer(query_data,many=True)
            # print("query_serializer", query_serializer.data)
        elif  report_type_f == "Cummulative_Report":
            query_data = Cummulative_report_data.objects.filter(date_data__range=[start_datetime, end_datetime])
            # print("query_data", query_data)
            query_serializer = CummulativeSerializer(query_data, many=True)
            # print("query_serializer", query_serializer.data)
        else:
            return JsonResponse({"error":"enter valid report type "})

        reports_res ={
                "From_timestamp": start_datetime,
                "To_timestamp": end_datetime_strp,
                "Report_data": query_serializer.data
            }


    except:
        return JsonResponse({"error": "Invalid date format. Use 'YYYY-MM-DD HH:MM:SS' format."},
                            status=status.HTTP_400_BAD_REQUEST)


    return JsonResponse({"reports_result":reports_res})









# {
#     "From_timestamp": "2024-09-18T07:58:24Z",
#     "To_timestamp": "2024-09-20T07:58:24Z",
#     "Report_data": [
#         {
#             "Timestamp": "2024-09-18T07:58:24Z",
#             "Cycle_time": 12,
#             "start_time": "12:00",
#             "Stop_time": "01:00",
#             "Input": 100,
#             "Output": 20,
#             "Power_consume": 20
#         },
#         {
#             "Timestamp": "2024-09-18T07:58:30Z",
#             "Cycle_time": 12,
#             "start_time": "12:00",
#             "Stop_time": "01:00",
#             "Input": 100,
#             "Output": 20,
#             "Power_consume": 20
#         },
#         {
#             "Timestamp": "2024-09-19T07:58:24Z",
#             "Cycle_time": 12,
#             "start_time": "12:00",
#             "Stop_time": "01:00",
#             "Input": 100,
#             "Output": 20,
#             "Power_consume": 20
#         },
#         {
#             "Timestamp": "2024-09-20T07:58:20Z",
#             "Cycle_time": 12,
#             "start_time": "12:00",
#             "Stop_time": "01:00",
#             "Input": 100,
#             "Output": 20,
#             "Power_consume": 20
#         }
#     ]
# }







# {
#     "Current": 20,
#     "Power": 27,
#     "Temperature": 30,
#     "Humidity": 20,
#     "Cycle": "ON",
#     "Door": "CLOSED",
#     "Start": "00:00:33",
#     "Cycle_Time": "00:00:00",
#     "Input_Load": 41.8,
#     "Output_load": 3.4,
#     "Total_Power": 19.843,
#     "Alerts": {
#         "Timestamp": "2024-09-18T07:58:24Z",
#         "alert_status": "Overload"
#       },
#
#     "graph_data": {
#       "title": "Temperature",
#       "labels": {
#         "x_label": "Timestamp",
#         "y_label": "°C"
#       },
#       "data": [
#         {
#           "x_axis_data": "2024-09-18T07:58:24Z",
#           "y_axis_data": 20
#         },
#         {
#           "x_axis_data": "2024-09-18T07:58:24Z",
#           "y_axis_data": 30
#         },
#         {
#           "x_axis_data": "2024-09-18T07:58:24Z",
#           "y_axis_data": 35
#         },
#         {
#           "x_axis_data": "2024-09-18T07:58:24Z",
#           "y_axis_data": 40
#         }
#       ]
#     },
#     "Updated_timestamp": "2024-09-18T07:58:24Z"
#   }
#
