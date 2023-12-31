# petl-guia

## Ejemplo de comandos
### Ejemplo con la *dimensión ips* (proceso específico):

- Ejecutar solo las extracciones de una transformación:

      py main.py extract dim_ips

- Ejecutar las extracciones y transformaciones:

      py main.py transform dim_ips

- Ejecutar las extracciones, transformaciones y carga:
  
      py main.py load dim_ips
En general, para correr un comando con un proceso específico:
      
      py main.py extract nombre
      py main.py transform nombre
      py main.py load nombre

Donde `nombre` es alguna de las llaves de los diccionarios `dim_managers_dict`, 
`trans_managers_dict` y `fact_managers_dict` presentes en el archivo *etl_scripts/managers/managers.py*

---

### Ejemplo con todas las dimensiones

- Ejecutar solo las extracciones de todas las dimensiones:

      py main.py extract dimensions

- Ejecutar las extracciones y transformaciones de todas las dimensiones:

      py main.py transform dimensions

- Ejecutar las extracciones, transformaciones y carga de todas las dimensiones:
  
      py main.py load dimensions

---

### Ejemplo con todas las tablas trans

- Ejecutar solo las extracciones de todas las tablas trans:

      py main.py extract trans

- Ejecutar las extracciones y transformaciones de todas las tablas trans:

      py main.py transform trans

- Ejecutar las extracciones, transformaciones y carga de todas las tablas trans:
  
      py main.py load trans

---

### Ejemplo con todas las tablas de hechos

- Ejecutar solo las extracciones de todas las tablas de hechos:

      py main.py extract facts

- Ejecutar las extracciones y transformaciones de todas las tablas de hechos:

      py main.py transform facts

- Ejecutar las extracciones, transformaciones y carga de todas las tablas de hechos:
  
      py main.py load facts

---

### Ejemplo realizado con todas las transformaciones/procesos:

- Ejecutar todas las extracciones:

      py main.py extract all

- Ejecutar todas las extracciones y transformaciones:

      py main.py transform all

- Ejecutar todas las extracciones, transformaciones y cargas:

      py main.py load all
