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

![alt text](https://github.com/EduardoGM98/MCOC2020-P0/blob/master/mimatmul_gr%C3%A1ficos.png)

- ¿Como difiere del gráfico del profesor/ayudante?
  - R. En el caso del gráfico de tiempo de ejecución, difiere principalmente en el tiempo inicial de ejecución, siendo más alto en mi caso que en el caso del profesor/ayudante.

- ¿A qué se pueden deber las diferencias?
  - R. Esta diferencia se puede deber al uso de computadores distintos o también se puede deber a que como esta vez cada uno tenía que escribir un programa propio para calcular la multiplicación de matrices (y no se utiliza una función de python), entonces un codigo puede ser mas eficiente que otro y por ende los tiempos de ejecución pueden ser distintos.

- El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  - R. Se debe a que la matriz es cuadrada y por ende el tiempo de ejecución aumenta exponencialmente cuando aumenta el tamaños de la matriz, a diferencia del uso de memoria que siempre aumenta lineal si es que la dificultad del problema aumenta.
 
- ¿Qué versión de python está usando?
  - R. 3.6

- ¿Qué versión de numpy está usando?
  - R. 1.14.0 

- Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
  - R. Si, se utilzan los 4 procesadores.
  ![alt text](https://github.com/EduardoGM98/MCOC2020-P0/blob/master/uso%20procesadores%20mimatmul.png)
  
# Desempeño de INV

- Desempeño de los 3 casos:
  - caso 1: 
  ![alt text](https://github.com/EduardoGM98/MCOC2020-P0/blob/master/graficos%20inv%20matrices%20caso%201.png)
  - caso 2:
  ![alt text](https://github.com/EduardoGM98/MCOC2020-P0/blob/master/graficos%20inv%20matrices%20caso%202.png)
  - caso 3: 
  ![alt text](https://github.com/EduardoGM98/MCOC2020-P0/blob/master/graficos%20inv%20matrices%20caso%203.png)
 
 Se puede apreciar que para el caso 1 numpy no soportaba los tamaños de half y longdouble por lo que no aparecen en el gráfico. También se puede ver que al usar la opción del caso 3 si mejora el desempeño. Por último, se ve que el uso de memoria para double y longdouble en el caso 2 y 3 son iguales ya que los dos son float64.
  
- Tamaños en memoria de los distintos tipos de datos:
  - half: 16 bytes
  - single: 32 bytes
  - double: 64 bytes
  - long double: 64 bytes

- Uso de memoria para cada caso:
  - caso 1: ![alt text](https://github.com/EduardoGM98/MCOC2020-P0/blob/master/uso%20procesadores%20inv%20matrices%20caso%201.png)
  - caso 2: ![alt text](https://github.com/EduardoGM98/MCOC2020-P0/blob/master/uso%20procesadores%20inv%20matrices%20caso%202.png)
  - caso 3: ![alt text](https://github.com/EduardoGM98/MCOC2020-P0/blob/master/uso%20procesadores%20inv%20matrices%20caso%203.png)
  Se puede ver en las tres imagenes que el caso 1 es el que mas porcentaje de memoria utiliza para invertir las matrices, seguido del caso 3 y por último el que menos memoria utiliza es el caso 2. También se puede apreciar que practicamente todos los procesadores son utilizados para resolver los porblemas.
  
- ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)?
  - R. Para el caso de numpy creo que se utiliza el método de Gaussian ya que es el proceso que más utilizo memoria de los 3 casos que analizamos y esto se puede deber a que para Gauss se tienen que generar las matrices triangular superior y triangular inferior que, creo yo, puede hacer que se utilize más memoria del procesador.
  Para Scipy creo que utilizó el método Eigendecomposition, ya que este método es mas facil para calcular la inversa de una matriz cuadrada y por ende puede producir un menos uso de memoria de los procesadores ya que no era muy compleja la operación.
  
- ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso?
  - R. Para el caso 1, se puede ver que para el dtype=double si influyó la estructura de caché y el paralelismo ya que la curva va creciendo desde que se demora menos con menos memoria hasta que cuando se requiere mas memoria el tiempo también crece y se debe a que comienza en los primeros niveles del caché y luego a medida de que la memoria de los caché se vaya llenando entonces sube a los otros niveles de caché y luego a ram y que a medido que sube, el tiempo de resolución aumenta ya que los niveles superiores de caché y luego la memoria ram son más lentos que los de abajo. Pero para dtype=single no ocurre esto ya que la curva tiene saltos que en ciertos puntos se demora bastante tiempo en comparación al punto siguiente que se demora muy poco.
  Para el caso 2, se aprecia lo mismo que en el caso 1, ya que para dtype=double y longdouble la curva va creciendo en tiempo a medida que aumenta la memoria, pero para los dtype=half y single esto no ocurre debido a los saltos que ocurren entre un punto a otro.
  Finalmente, para el caso 3, la estructura de caché y el paralelismo se ven reflejados en todos los dtypes, ya que cuando el uso de memoria es muy pequeño, L1 comienza a trabajar y es el más rápido de todos y por ende el tiempo de ejecución es muy chico, pero a medida que la memoria aumenta, L1 va a tener que trabajar en paralelo con L2, luego con L3 y asi sucesivamente hasta resolver todo el problema, y cuando esto ocurre los tiempos de ejecución son más altos, viendose esto reflejado en los gráficos mostrados anteriormente.
  

# Desempeño Ax = B

![alt text](https://github.com/EduardoGM98/MCOC2020-P0/blob/master/Entrega%206/gr%C3%A1fico%20A_invB%20parte%202.png)

Se puede apreciar en el gráfico que la función que mas tiempo demoró cuando N=10000 es la función de numpy que invierte la matríz para resolver el sistema de ecuaciones, en cambio la que menos se demoró fue la función que utiliza el solve de scipy utilziando los parámetros "pos" y "overwrite_b". Pero se puede apreciar que esto no es así en un principio, ya que el solver de numpy fue el que menos demoro para N=2, mientras el que más se demoró para este mismo N fue el solver de scipy con el argumento "symmetric", que luego estos 2 últimos solvers se demorarán prácticamente los mismo que las otras funciones. 
Los distintos tiempos de ejecución de cada solver se deben a que cada solver realiza la operación de distinta manera, afectando al desempeño de un solver en comparacióon con los otros. En el caso del desempeño de la función de numpy que invierte la matriz, ya se podría haber previsto que iba a ser la que más tiempo iba a demorar ya que no es muy óptimo tener que invertir una matriz de 10000 x 10000 y se comprobó que es así ya que fue la función que más demoró. En el caso del solver que menos se demoró, se puede deber a los parámetros "pos" y "overwrite_b" que se utilizaron para este caso, ya que el primero de estos hace que la matriz se defina como definida positiva y el segundo de estos sobreescribe los datos de la matriz B, mejorando el rendimiento de esta solución y por ende ser la función que menos se demora. 
Se puede notar que para N muy grandes, los distintos solver se demoran prácticamente lo mismo, siendo la diferencia muy chica, a diferencia de la función de numpy que invierte las matrices ya que su tiempo final de ejecución es mucho más alto que el de los otros, ya que como se puede ver en el gráfico todos los otros solvers se demoran alrededor de 10 segundos, o un poco más en algunos casos, en la ejecución para N=10000 pero la función numpy que invierte las matrices se demora alrededor de 1 minuto, una diferencia considerable en el caso de que se quieran resolver problemas de este tipo o con matrices que tengan un N más grande. 

# Matrices dispersas y complejidad computaciona
```
def matriz_laplaceana(N, d=double):
    L=-(np.eye(N, k=-1, dtype=d))+2*\
      (np.eye(N, dtype=d)) + -(np.eye(N, k=+1, dtype=d))
    return L
```
- Matriz llena matmul.
![alt text]()

- Matriz dispersa matmul.
![alt text]()

- Matriz llena inv
![alt text]()

- Matriz dispersa inv
![alt text]()

- Matriz llena Ax=b
![alt text]()

- Matriz inversa Ax=b
![alt text]()


- Comente las diferencias que ve en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas.
  - R. Principalmente se puede ver que en el caso de las matrices dispersas los puntos son más estables que en el caso de matrices llenas, es decir, que en el gráfico no se ven tantos saltos de tiempo, entre un punto y otro, a diferencia de los gráficos de matrices llenas.
  
- ¿Cual parece la complejidad asintótica (para LaTeX: N\rightarrow\inftyN → ∞)  para el ensamblado y solución en ambos casos y porqué?
  - R. Caso matmul llena: para el ensamblado de la matriz la complejidad asintotática parece ser O(N**2) ya que los puntos finales tienden a establecerse en esa asíntota, en cambio para la solución parece ser O(N**3) ya que el algoritmo sigue en gran parte a esa asíntota.
  Caso matmul dispersa: para el ensamblado nuemvamente parece ser O(N**2), debido a que el algoritmo se mantiene pegado a esa asíntota durante gran parte de su largo, mientras que para la solución se parece más a O(N**4) en su último tramo.
  Caso inv llena: para el ensamblado de este caso, el algoritmo tiende a parecerse, cuando tiende a infinito, a O(N**4) ya que parece ser que tiende a esa asíntota en su último tramo, en cambio, para la solución, la complejidad asintitatica parece ser O(N**3) dada la misma razón anterior.
  Caso inv dispersa: Para el ensamblado, parece ser que la complejidad asintotática tiende a O(N**4) dado que el algoritmo se mantiene, en los puntos finales, asintotático a eso. Para el caso de la solución, y debido a la forma que toma el algoritmo en los últimos puntos, la complejidad asintotática se parece a O(N**4)
  Caso Ax=b llena: Para este caso, en el ensamble de la matriz cuando tiende a infinito, la complejidad asintotática parece ser O(N) ya que no es muy grande la pendiente en el tramo final del algoritmo y por ende tiende a eso. Para la solución, tiende a la asíntota de O(N**2) debido a lo mismo que para el ensamble.
  Caso Ax=b dispersa: En este caso para el ensamble, al igual que para el caso anterior, cuando tiende a infinto, la complejidad asintotática tiende a O(N) dado que la curva del algoritmo tiende a esa asíntota en sus últimos puntos. Para el caso de la solución, en los últimos puntos se puede ver que la curva tiende a O(N**4).
  
- ¿Como afecta el tamaño de las matrices al comportamiento aparente?
  - R. Que a medida que aumenta el tamaño de la matriz, el tiempo de ejecución del algoritmo va a ir en aumento, por ende el gráfico del algoritmo va a ser creciente, al punto de hacerse asintotático en cualquiera de los casos de complejidad asintotática vistos anteriormente.
  
- ¿Qué tan estables son las corridas (se parecen todas entre si siempre, nunca, en un rango)?
  - R. Por lo general, las distintas corridas son muy estables, la mayoría se parece mucho entre si, sobretodo cuando los tamaños de las matrices son muy grandes. En algunos casos en los puntos iniciales, hay una corrida que es muy distinta a las otras, puede deberse a que cuando se corrión el programa esa vez, el uso de memoria era más elevado debido a que podría estar abiertas otras aplicaciones, pero igual, por lo general, es muy estable.





