import rivian_api as rivian
import os
import json
import boto3
from datetime import datetime

rivian = rivian.Rivian()


response = rivian.login(
    dbutils.secrets.get(scope="deezwatts", key="username"),
    dbutils.secrets.get(scope="deezwatts", key="password")

)

# owner info, grab rivian vehicleid
owner = rivian.get_user_information()
rivianid = owner['data']['currentUser']['vehicles'][0]['id']
print(f'Rivian: {rivianid}')

# status info
whipstatus = rivian.get_vehicle_state(rivianid)

# whip info
whip = rivian.get_vehicle(rivianid)

# charging info
charge = rivian.get_live_session_data(rivianid)

# status is our main dictionary, add the other two keys
whipstatus['whip'] = whip
whipstatus['charge'] = charge

deezwatts = json.dumps(whipstatus)

timeitis = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")


# upload to a bucket
s3 = boto3.resource('s3')
s3object = s3.Object('deezwatts', 'in/json/deezwatts-json-' + timeitis + '.json')

response = s3object.put(
    Body=(bytes(deezwatts.encode('UTF-8')))
)


