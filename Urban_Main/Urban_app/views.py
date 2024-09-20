import datetime
import json

from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from asgiref.sync import sync_to_async

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
    "Actual_Weight": 3.4,
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
      "data": [
        {
          "x_axis_data": "2024-09-18T07:58:24Z",
          "y_axis_data": 20
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
        }
      ]
    },
    "Updated_timestamp": "2024-09-18T07:58:24Z"
  }




    return dash_res
    # return JsonResponse({"dash_res":dash_res})


@api_view(['POST'])

def Reports(request):
    start_datetime = request.data.get('start_datetime')
    end_datetime = request.data.get('end_datetime')
    try:
        start_datetime = datetime.datetime.strptime(start_datetime, '%Y-%m-%d')
        print('try  start_datetime',start_datetime)

        # end_datetime = datetime.datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')
        end_datetime_strp = datetime.datetime.strptime(end_datetime, '%Y-%m-%d')
        end_datetime = end_datetime_strp + datetime.timedelta(days=1)
        print('after increment end_datetime',end_datetime)
        reports_res ={
                "From_timestamp": "2024-09-18T07:58:24Z",
                "To_timestamp": "2024-09-20T07:58:24Z",
                "Report_data": [
                    {
                        "Timestamp": "2024-09-18T07:58:24Z",
                        "Cycle_time": 12,
                        "start_time": "12:00",
                        "Stop_time": "01:00",
                        "Input": 100,
                        "Output": 20,
                        "Power_consume": 20
                    },
                    {
                        "Timestamp": "2024-09-18T07:58:30Z",
                        "Cycle_time": 12,
                        "start_time": "12:00",
                        "Stop_time": "01:00",
                        "Input": 100,
                        "Output": 20,
                        "Power_consume": 20
                    },
                    {
                        "Timestamp": "2024-09-19T07:58:24Z",
                        "Cycle_time": 12,
                        "start_time": "12:00",
                        "Stop_time": "01:00",
                        "Input": 100,
                        "Output": 20,
                        "Power_consume": 20
                    },
                    {
                        "Timestamp": "2024-09-20T07:58:20Z",
                        "Cycle_time": 12,
                        "start_time": "12:00",
                        "Stop_time": "01:00",
                        "Input": 100,
                        "Output": 20,
                        "Power_consume": 20
                    }
                ]
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