import teslapy
import json
from flask import jsonify

def tesla_state(request):
    with teslapy.Tesla('michaelkwasi@gmail.com') as tesla:
        vehicles = tesla.vehicle_list()
        vehicles[0].sync_wake_up()
        tesla_data = vehicles[0].api('VEHICLE_DATA')['response']
        return jsonify(tesla_data)
        #json_data = json.dumps(tesla_data)
    #return json_data