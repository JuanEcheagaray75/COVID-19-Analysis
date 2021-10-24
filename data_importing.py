import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from zipfile import ZipFile
import io

# Dataset
url = 'https://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip'

response = requests.get(url, auth=HTTPBasicAuth('', ''),
                        stream=True, verify=False)
with ZipFile(io.BytesIO(response.content)) as zip:
    with zip.open(zip.namelist()[0]) as data:
        df = pd.read_csv(data)

df.drop(['PAIS_NACIONALIDAD', 'PAIS_ORIGEN'], axis=1, inplace=True)
print(df.head())

df.to_feather('data\\data.feather')
