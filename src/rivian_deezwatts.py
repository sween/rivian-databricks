import rivian_api as rivian
import os
import json
import boto3
import time
from datetime import datetime


class RivianDataBricks(object):
    def __init__(self):
        self.rivian = rivian.Rivian()
        response = self.rivian.login(
            os.environ['RIVIAN_USERNAME'],
            os.environ['RIVIAN_PASSWORD']
        )
        # owner info, grab rivian vehicleid
        self.owner = self.rivian.get_user_information()
        self.rivianid = self.owner['data']['currentUser']['vehicles'][0]['id']
        print(f'Rivian: {self.rivianid}')

    def run(self):
        # status info
        whipstatus = self.rivian.get_vehicle_state(self.rivianid)
        # whip info
        whip = self.rivian.get_vehicle(self.rivianid)

        # charging info
        charge = self.rivian.get_live_session_data(self.rivianid)
        charge_schedule = self.rivian.get_charging_schedule(self.rivianid)

        charge['charge_schedule'] = charge_schedule

        # ota details
        ota = self.rivian.get_ota_details(self.rivianid)

        # last connection
        last_connection = self.rivian.get_vehicle_last_connection(self.rivianid)


        # status is our main dictionary, add the other two keys
        # and make a gigantic complex json object for databricks
        whipstatus['whip'] = whip
        whipstatus['charge'] = charge
        whipstatus['owner'] = self.owner
        whipstatus['last_connection'] = last_connection

        deezwatts = json.dumps(whipstatus)

        timeitis = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")


        # upload to a bucket
        s3 = boto3.resource('s3')
        s3object = s3.Object('deezwatts', 'in/json/deezwatts-json-' + timeitis + '.json')

        response = s3object.put(
            Body=(bytes(deezwatts.encode('UTF-8')))
        )       


if __name__ == '__main__':
    RivianDataBricks().run()