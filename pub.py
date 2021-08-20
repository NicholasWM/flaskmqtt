import paho.mqtt.client as mqtt     #import the client1
client = mqtt.Client() #create new instance
# broker_address="67.205.191.96" #use external broker
# broker_address="test.mosquitto.org" #use external broker
# broker_address="161.35.9.75" #use external broker
broker_address="localhost" #use external broker
# user = "marcosyaiama"
# password = "fabianopescariasnicholas1234"


# broker_address='broker.hivemq.com'
# user = ""
# password = ""

# client.username_pw_set(user, password=password) 

client.connect(broker_address, 1883, 60) #connect to broker
# client.publish('laksjd')
# client.publish("placa/3/carga/1", 'E-1')#publish
client.publish("placa/1/sensor/1", 'E-2')#publish
# client.publish("outTopic", 'E-1')#publish