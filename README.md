# [Movin' Out](https://www.youtube.com/watch?v=cJtL8vWNZ4o&ab_channel=billyjoelVEVO) 🏞:
<div align=center><img src ="https://trabajadorasocialdepueblocom.files.wordpress.com/2020/08/wp-1598249473318.gif?w=498&zoom=2" /></div>


Des de la aparición de la revolución industrial la población de zonas rurales en España he seguido una tendéncia de migración hacia las grandes ciudades. Esto ha llevado a la despoblación de ciertas zonas de España que siguen viendo como sus datos demográficos son cada vez menos esperanzadores.

Lo cierto es que en los últimos años ha aparecido el concepto de 'home office', trabajar des de casa o "tele-trabajar" es cada vez más frecuente en el mundo digital, ya sea parcialmente o totalmente. Esto ha hecho que aparezcan perfiles de gente que desea mudarse fuera de las ciudades, en busca de tranquilidad y salud. 

Con el fin de crear una herramienta para toda esa gente que quiera mudarse al campo pero no sepa por donde empezar hemos decidido crear una aplicación. Para ello, hemos tenido que crear el perfil de nuestro usuario medio y ver que es lo que busca en un pueblo. Este trabajo lo ha hecho mi compañera de UI/UX. Mi trabajo en el proyecto ha sido generar todas las herramientas necesarias para recopilar todos los datos que se necesitarían de cara a la creación de la aplicación. Además de crear la infrastructura para almacenar todos esos datos de forma que sean facilmente accesibles y faciles de usar. 

Finalmente, aunque no tenemos una compañera para crear la aplicación como tal he decidido crear una API con flask para poder ejemplificar los resultados obtenidos.

He subido en el repo toda la info que usado, tanto el código usado (con un 1 los archivos dedicados a la recopilación, con un 2 los dedicados a la creación de la base de datos y con un 3 los dedicados a la creación de la api), como los datos. Las fuentes de los datos estan citadas en la [Bibliografia](#bibliografia). 


# La recopilación de los datos 👷🏼‍♂️: 
Vimos que lo más importante para la mayoría de gente que quería mudarse un elemento importante era mantener una buena conexión a la red. Es por eso que decidí basar mi base de datos en un archivo csv sacado del Instituto Nacional de Estadística (INE) que indicaba la conectividad en cada Entidad poblacional de España (a internet, >= 30mb y >= 100mb y 3g y 4g). 

Por simplicidad decidí ceñirme a estudiar las entidades poblacionales en Castilla-León, por ser una comunidad autónoma con poca densidad de población, y la principal víctima de la despoblación de zonas rurales. 

Pues bien, tuve que buscar información de diferentes formas. Combine el uso de datos extraídos del INE en forma de csvs y el scrapeo de diferentes fuentes, tales como [Wikipedia](https://es.wikipedia.com) o [GoogleMaps](https://googlemaps.es). 

Hemos recogido datos de muchas naturalezas distintas para enriquecer la base de datos, tales como la población en cada población y del municipio al que pertenece, el partido politico que govierna en los municipios, datos climaticos o entidades cercanas (entidades como polideportivos, hospitales o centros comerciales). 

Un dato importante que no hemos recopilado pero sería interesante intentar incluir de cara a un futuro es el precio del suelo en cada población y la disponibilidad de viviendas.

# La base de datos 🗃:
Por la diversidad en los datos decidí usar el sistema de MongoDB. Es decir, la base de datos es no relacional. Aunque si que le he dado una estructura.

Todos los elementos incluidos en la base de datos tienen diferente información referente a cada entidad. Pero hay 2 elementos presentes en todas las entidades, un geopunto que identifica la localización de la entidad, y un elemento que describe el tipo de entidad. Es decir, que siempre podemos saber si hablamos de un pueblo, un hospital, una escuela o otra una entidad de otro tipo y sabemos donde se encuentra. 

La idea es que una futura aplicación pudiera hacer geoqueries para filtrar entre poblaciones. Si en un futuro enriquecieramos la base de datos con muchos más datos de toda España sería fácil filtrar pueblos por distancia a centros de salud, escuelas, etc. 

# La API 🗺:
La interfaz que he creado en el servidor de mi ordenador es muy senzilla y solo pretende ejemplificar la utilidad de la base de datos creada. La idea es que tenga dos funciones principales. 

Una de ellas esta ya terminada y operativa. Es posible buscar un pueblo de Castilla León y que nos muestre el pueblo, con información sobre el mismo. Información referente al clima, conectividad, etc. Además también aparecen en el mapa un grupo de entidades cercanas a la población.

La otra función que debería inculir esta api es un filtro. La idea sería poder llamar des de la api una geoquerie y que nos diera, por ejemplo, todos los pueblos que queden a menos de 20km de un hospital. De tal forma que aplicando un numero elevado de filtros pudieramos reducir mucho el numero de pueblos, y encontrar el mejor pueblo para nuestro usuario. Esta función no la he acabado, entre otras cosas por la falta de datos en la base de datos, que se encuentra en un estadio muy inicial. 

# Further Steps 🚀:
Este ha sido el proyecto final que he hecho en IRONHACK, he tenido apenas 10 días para desarroyarlo. Es por eso que el producto final es simplemente una pequeña muestra de lo que podría llegar a ser si un día decido crear, realmente, una base de datos que tenga una utilidad real y sea operativa. Hay muchisimas cosas que han quedado por hacer, así que voy a listar alguna de ellas por el orden que creo más adiente:
* Mejora del scrapeo, recopilación de datos sobre todos y cada uno de los pueblos de Castilla León,
* Extrapolar a todo el estado español. La creación de funciones que valen para los datos en Castilla León admite que se pueda extrapolar a todo el estado, o incluso con las debidas modificaciones es extrapolable a cualquier zona del planeta (¡dónde haya pueblos!😂).
* Creación de geoqueries que sirvan para filtrar de forma eficiente y adequada la base de datos. 
* Mejora de la interfaz, a nivel estetico pero sobretodo funcional, incluir mucha más información y estructurarla para que sea útil. 

# Bibliografia 📚: <a name="bibliografia"></a>
### Libraries:
* [Pandas](https://pandas.pydata.org/)
* [Numpy](https://numpy.org/doc/1.18/)
* [ReGex](https://docs.python.org/3/library/re.html)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Pymongo](https://pymongo.readthedocs.io/en/stable/)
* [Selenium](https://selenium-python.readthedocs.io/)
* [Beautiful Soup (bs4)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Fuentes de datos:
* [Instituto Nacional de Estadística (INE)](https://ine.es)
* [Wikipedia](https://es.wikipedia.com)
* [Weather Spark](https://es.weatherspark.com/)
* [GoogleMaps](https://googlemaps.es)

 
