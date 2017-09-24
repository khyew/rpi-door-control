# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# For Websocket connection
myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)

# For Websocket
myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)

# For Websocket, we only need to configure the root CA
myMQTTClient.configureCredentials("./VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem")

myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
