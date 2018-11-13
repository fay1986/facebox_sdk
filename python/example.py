import paho.mqtt.client as mqtt
import time
import json
import requests

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("rt_message")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("-"*10)
    # print(msg.topic+" "+str(msg.payload))
    try:
        msg_dict = json.loads(msg.payload.decode())
        # print(msg_dict)
        # for k, v in msg_dict.items():
        #     print(k, v)
        status = msg_dict.get("status")
        persons = msg_dict.get("persons") 
        # person_id = msg_dict.get("person_id")
        # group_id = msg_dict.get("persons")[0].get("group_id") 
        # print(status, person_id, group_id)
        if status == "known person":
            for person in persons:
                person_id = person.get("id")
                group_id = person.get("group_id")

                url = "http://192.168.31.173:3000/restapi/get_name_by_faceid?group_id={}&face_id={}".format(group_id, person_id)
                response = requests.get(url)
                name = json.loads(response.text).get("name")
                person["name"] = name

        print(msg.topic+" "+json.dumps(msg_dict))
    except Exception as e:
        print(e)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.31.155", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
