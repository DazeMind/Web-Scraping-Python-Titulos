# Web-Scraping-Python-Titulos
Este código realiza web scraping en el sitio web "https://www.vulnhub.com" para extraer los títulos de las máquinas virtuales disponibles.  

Primero, se importan las librerías re y requests. 
La librería requests es utilizada para hacer una petición a la URL del sitio web y obtener su contenido HTML, que se almacena en la variable content. 

La librería re es utilizada para buscar patrones específicos en el HTML. 

A continuación, se define la variable patron que contiene una expresión regular para buscar los títulos de las máquinas virtuales. 

El patrón busca todo lo que sigue a "/entry/" en la URL, lo que incluye letras, números y guiones.  

Se utiliza re.findall() para encontrar todas las coincidencias de patron en el contenido HTML, lo que resulta en una lista de títulos de máquinas virtuales, que pueden contener duplicados. 

Para eliminar duplicados, se convierte la lista resultante en un conjunto mediante set(), y luego se convierte de nuevo en una lista. 

Finalmente, se utiliza un bucle for para limpiar los nombres de las máquinas virtuales, quitando "/entry/" de cada título, y se almacenan los nombres limpios en la lista maquinas_final. Además, en cada iteración del bucle, el nombre de la máquina se imprime en la consola.
