# Buscador-leaks-commits-json
En este repositorio se encuentra el código de un buscador de leaks en commits que guarda los leaks encontrados en formato json.
Para ello, el repositorio consta de:
- Una carpeta "skale" que es la copia del repositorio de Git en el que se van a buscar los leaks
- Un fichero ".gitignore"
- Un fichero "requirements.txt" con las librerías necesarias para la ejecución del código
- Fichero "git_leaks_json.py" que buscará los leaks en commits. Para ello, se empleará una ETL que buscará unas palabras clave prefijadas en los commits del repositorio clonado.
- Fichero "leak.json" que contendrá los leaks encontrados y que será producido por el programa.

Para la ejecución de este repositorio primero se deberá hacer un pip install -r requirements.txt, el cual descargará las librerías necesarias para la ejecución del fichero y, posteriormente, ya se podrá ejecutar el fichero ".py".
