from requests import Session
from requests.auth import HTTPBasicAuth  
from zeep import Client
from zeep.transports import Transport
import urllib3


urllib3.disable_warnings()
session = Session()
session.verify = False
session.auth = HTTPBasicAuth('User', 'Passwd')

client = Client('https://xyz.com/abc?wsdl',transport=Transport(session=session))
    
from zeep import helpers #To convert to python data structure
import pandas as pd  #for data frame

ClassList = client.service.getData()   # SOAP Operation 

pyl = helpers.serialize_object(ClassList)  #Convert to python data structure

df = pd.DataFrame(pyl)     
