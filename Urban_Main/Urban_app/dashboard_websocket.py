import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()


def dashboard_mqtt_data():
# def dashboard_mqtt_data(connected_machine_data):


    # machine_data = json.loads(connected_machine_data)

    dash_result={
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

                    ]
                        },


                        }
    }







    dash_result_json = json.dumps(dash_result)

    try:
        async_to_sync(channel_layer.group_send)('str(machine_id)'+'_io',
                                                {"type": "dashboard_socket_data", "text": dash_result_json})
    except Exception as e:
        print("io error - ", e)

