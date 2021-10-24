# Modelo predictivo para el COVID-19

Durante estas semanas estaré intentando analizar la base de datos de COVID-19 proporcionada por la Dirección General de Epidemiología Mexicana. Aclaro que este documento no es un README, sino que aquí haré un diario en el que exploraré todas las ideas que me surjan para el análisis.

## Día 1

Lograr cargar la base de datos desde un archivo zip descargado de la página de la dirección general de la epemidiología, que problemón es hacer ese tipo de cosas, ví que se podría hacer directamente con pandas, pero también he visto que es más seguro con el método alternativo que encontré. La experiencia me dirá si vale la pena.

De momento ya puedo leer el archivo, solamente me falta convertirlo a un formato con el que pueda trabajar de forma sencilla, que cargue relativamente rápido y que no consuma tanta memoria.

Creo que el archivo será en formato feather. Voy a ver como leer un feather desde un zip, tenerlo en ese formato en github podría ser una mejor idea.

Checar si por default todos los hombres tienen 0 en la variable de embarazo.

Definición de EPOC: una enfermedad que se produce cuando una persona tiene una infección que provoca una pérdida de la capacidad de respirar.

### Morbilidades y características a analizar

- Intubado (respuesta)
- Neumonía (Ver si se queda, la corrupción mexicana en los hospitales podría ser un problema)
- Edad
- Sexo
- Embarazo
- Diabetes
- Epoc
- Asma
- Inmusupr (inmunosupresión)
- Hipertensión
- Cardiovascular
- Renal_crónica
- Obesidad
- Tabaquismo
