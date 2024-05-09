# Proyecto_Ransomware

1-Encriptador:
Para usar el encriptador, debe seguir los siguientes pasos:
1. Ubicarse en la carpeta Encriptador 
2. uitlizar en terminal el comando "./encriptador.bat " seguido de la direccion de la carpeta a encriptar 
Ejemplo. este proyecto ya tiene unos archivos de prueba para encriptar, asi que usaremos:
"./encriptador.bat C:\Users\dluja\Documents\Proyecto_Ransomware\Encriptador\archivos_secretos"
3. listo los archivos se encriptaron fuera de la carpeta Encriptador

2-Desencriptador:
Para desencriptar nuestros archivos debemos hacer lo siguiente:
1. Ubicarnos en la carpeta de nuestro desencriptador
2. En la terminal escribir en la misma linea el comando: python desencriptar_archivos.py y entre comillas poner "Ruta de la carpeta con los archivos encriptados" y seguido de "Ruta donde queremos que este nuestra nueva carpeta con archivos" Ejemplo:  python desencriptar_archivos.py "C:\Users\dluja\Documents\ArchivosEncriptados.zip"  "C:\Users\dluja\Documents\ArchivosDesencriptados"
3. Se creara una nueva carpeta con los archivos desencriptados

3-Informacion del Sistema:
Para generar una carpeta con archivos txt con la informacion del sistema se hace lo siguiente:
1. Ubicarse dentro de la carpeta donde se encuentre el archivo systemInfoGenerator.py
2. Inserte en la terminal el comando: python systemInfoGenerator.py
3. Se va a crear la carpeta con un total de 10 archivos txt con diversa informacion del sistema. 