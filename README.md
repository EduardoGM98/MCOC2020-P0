# MCOC2020-P0
# Mi PC:
- Marca/Modelo: HP 240 G5 
- Tipo: Notebook
- Año de adquisición: 2017 
- Procesador: 
  - Marca/Modelo: Intel(R) Core(TM) i5-6200U 
  - Velocidad base: 2,40 GHz
  - Velocidad máxima: 2,80 GHz
  - Número de núcleos: 2
  - Número de hilos: 4
  - Arquitectura: x64
  - Set de instrucciones:Intel® SSE4.1, Intel® SSE4.2, Intel® AVX2
              
- Tamaños de las cachés del procesador: 
  - L1: 128 kB
  - L2: 512 kB
  - L3: 3,0 MB
                                        
- Memoria: 
  - Total: 4 GB
  - Tipo de memoria: DDR3
  - Velocidad: 2133 MHz
  - Numero de (SO)DIMM: 4
           
- Tarjeta gráfica: 
  - Marca/Modelo: Intel(R) HD Graphics 520
  - Memoria dedicada: 128 MB 
  - Resolución: 1366 x 768
                   
- Discos duros 1:
  - Marca/Modelo: WDC WD10JPVX-60JC3TO 
  - Tipo: HDD
  - Tamaño: 931,51 GB
  - Particiones: 5
  - Sistemas de archivos: NTFS
                  
- Dirección MAC de la tarjeta wifi:3C-A0-67-D3-5F-17
- Dirección IP (Interna, del router): 192.168.1.171
- Dirección IP (Externa, del ISP): 152.174.130.50
- Proveedor internet: Movistar fibra óptica

# Desempeño matmul
![alt text](https://github.com/EduardoGM98/MCOC2020-P0/blob/master/imagen%20graficos.jpeg)

- ¿Como difiere del gráfico del profesor/ayudante?
  - R. Difiere en que los tiempos de ejecución iniciales y finales son mas altos que los del profesor y por ende el grafico cambia en esas zonas. También cambia el grafico en que en el gráfico de uso de memoria tiene una mayor pendiente que el gráfico de el profesor.

- ¿A qué se pueden deber las diferencias?
  - R. Las diferencias se pueden deber principalmente a que los computadores son distintos, por ende mis timpos de ejecución y el uso de memoria en mi pc es más
  alto que en el computador de el profesor.

- El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  - R. Se debe a que la matriz es cuadrada y por ende el tiempo de ejecución es exponencial, a diferencia del uso de memoria que siempre aumenta lineal si es que la
  dificultad del problema aumenta.

- ¿Qué versión de python está usando?
  - R. 3.6

- ¿Qué versión de numpy está usando?
  - R. 1.14.0

- Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
  - R. ![alt text](https://github.com/EduardoGM98/MCOC2020-P0/blob/master/uso%20procesadores.jpeg)

# Desempeño MIMATMUL

![alt text](https://github.com/EduardoGM98/MCOC2020-P0/blob/master/graficos%20mimatmul.jpeg)

- ¿Como difiere del gráfico del profesor/ayudante?
  - R. En el caso del gráfico de tiempo de ejecución, difiere principalmente en el tiempo inicial de ejecución, siendo más alto en mi caso que en el caso del profesor/ayudante.

- ¿A qué se pueden deber las diferencias?
  - R. Esta diferencia se puede deber al uso de computadores distintos o también se puede deber a que como esta vez cada uno tenía que escribir un programa propio para calcular la multiplicación de matrices (y no se utiliza una función de python), entonces un codigo puede ser mas eficiente que otro y por ende los tiempos de ejecución pueden ser distintos.

- El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  - R. En este caso 
  
- ¿Qué versión de python está usando?
  - R. 3.6

- ¿Qué versión de numpy está usando?
  - R. 1.14.0 

- Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
  - R. 

