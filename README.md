**Comando y archivo utilizado para debugging:**

> python3 Parser.py prueba1.txt

**Avances:**

**16 Abril 2023**

1. Durante y acabando semana santa pulí mis conocimientos de R para empezar a planear cómo sería el léxico, sintaxis y semántica.
2. Esta semana creé el documento en LATEX. En mi opinión, ya se ve muy bien; solo es de entrar a llenar y actualizar, ya así puedo enfocarme completamente en lo práctico y más difícil como los dibujos a mano y el código del compilador en sí, mis planes, errores y correcciones.
3. Apoyándome con el LittleDuck (en especial su Léxico, el cual era como un 60% de lo que usa el lenguaje R; su sintaxis es única y distinta, esa no me va a servir mucho mas que de recordatorio), creo haber terminado el Léxico por ahora, con la Sintaxis empecé a batallar un poco al ver que sería todo diferente. Me dio un dolor de cabeza nuevamente, intentaré avanzarle más tarde con lo que pueda, tengo clases de tópicos con tareas pesadas y de relleno que me están estresando sin razón, como el realizar un PowerPoint extenso para este lunes yo dar una clase de 40 minutos sobre películas y series de televisión y que el profesor no hable durante todo ese día, también un guión de género "romance y comedia" para un corto cuya creatividad no me está ayudando a exprimir; quisiera tener ya un léxico y sintaxis funcionales al 100% para empezar a preocuparme con lo demás.
4. La creación del Github no quisiera contarla en sí, sigue siendo la tarea de LittleDuck, el Léxico recibió complementaciones que mencioné en uno de los commits (exponencial, modulus, asignaciones...). Sigo trabajando en la sintaxis, solo que creo aún no sé cómo definir variables sin mencionar su tipo, lo preguntaré en clase si puedo, o tal vez cambie el diseño del compilador/lenguaje para que tenga que definir tipos, solo que rompería mi promesa de ser lo más similar a R posible, quisiera saber cómo hacerlo bien. Por ahora me llevaré los planes en la cabeza, me gusta planear y diseñar mucho primero antes de escribir.

**22 Abril 2023**

> Avance a Sintaxis (50%).

**23 Abril 2023 Parte 1**

> Avance a Sintaxis (95%), ya está construido, pero falta testear y romperlo; intentaré hacerlo durante esta semana, para enfocarme en la tablas de variables, direcciones, y el examen de mañana. En sí, donde siento me causará más ruido será el Loop y tal vez Statement/Expressions, lo demás siento ya está bien, o requerirá fixes pequeños. Las tablas de variables y direcciones las considero muy sencillas, así que aprovecharé esta semana para intentar ya ponerme al tan al tanto como pueda; siento que voy muy lento, pero no lo sé.

**23 Abril 2023 Parte 2**

> Tabla de variables terminada. Intentaré crear las matrices aquí en Python para el Type Matching y luego otra para las Direcciones; también codificar los nodos intermediarios al menos como placeholders para después conectarlos. Finalmente hacer pruebas a la sintaxis y dejarla al cien para el siguiente fin de semana, y lo que se pida a parte.

**1 Mayo 2023**

> Avances generales, especialmente al Léxico y Sintaxis; me empecé a perder en las posibilidades y el "¿cómo se haría?" en cuanto a definir parámetros, funcionalidades estrictas/especiales como la de "do while", "else if" / "elif", que se comportan distinto a cualquier if/else; también sobre los switches, declarar funciones, loops... Los más complicados, el endgame; me tengo que asegurar primero que se van a requerir o no, como por ejemplo: la recursión fue cancelada... Hasta ahora lo que más me preocupa es la modularidad del programa, sé que lo es, pero me sigue dando miedo que algún cambio pequeño requiera editar casi todo el programa entero de alguna manera, pero intentaré ignorarlo...

**2 Mayo 2023**

> Léxico y Sintaxis Terminado.
>
> Avance a creación de matrices, nodos y placeholders para lo que sigue. Investigaré cómo conectarlos y dejarlos ya funcionales: sé lo que hacen y para qué, pero aún no sé qué deben regresar de resultado, si un mensaje de error, detener el programa; y cómo de la forma más adecuada o mejor...

**7 Mayo 2023**

> Se me complicó el tiempo. Por ahora solo pude implementar el léxico y sintaxis del MODULE y FUNCTION_CALLING listos (Parser.py, linea 81 a 87); igualmente, perdí un buen de tiempo resolviendo un error con mis tokens de VOID y WHILE, se me hizo raro que el keyword de PROGRAM es el único que no debe ir adentro de la lista de tokens, tal vez por ser el primero en leerse, no lo sé... Arreglé dos errores de recursión infinita que encontré, y por ahora sigo reparando aquello mientras empiezo a meterme con lo de la memoria virtual, que es lo que más miedo me da. Sé que es un simple pedazito de código que interviene a mitad de una lectura, para meter o sacar elementos de una pila y ya, eso lo entiendo y todo, pero los errores siento me van a estresar mucho, me desanima, y he tenido una depresión muy pesada con la que he estado lidiando ya mucho tiempo, pero seguiré intentando.
>
> Terminé enfocando esta semana a mi proyecto final de Guionismo, el cual pienso acabar ya para este jueves a más tardar, espero menos; es para el 15 de Mayo, y es todo un guión cinemático de mínimo 25 páginas, con estructura y apariencia igual a los reales, sobre una historia o algo creativo y original que se nos ocurra. Me encanta escribir, pero hacerlo en muy poco tiempo y quererme lucir me ha quitado mucha energía, pero ya lo estoy terminando, ya para tener el mes entero libre para este proyecto y nada más.

**13 Mayo 2023 - Mockingjay Parte 1**

> Terminé de corregir unos errores relacionados a mi léxico y sintaxis. Los ciclos, funciones, operaciones con módulo, condicionales lógicas y también la declaración de arrays y/o matrices (por ahora hasta 2D, aunque sé cómo ciclarlo para que sean ilimitadas, aunque siento que más 3D ya empieza a ser un mal chiste). Acepta tanto el estilo de R (int x <- [1, ..., n] | int x[3] <- [1,2,3]) y C++ (int x[n] = [1, ..., n]) combinados de manera que aún tengan sentido. Por ahora dejaré el símbolo de exponencial en standby; acabo de recordar que me falta el return, pero lo elaboraré junto la memoria y máquina virtual cuales ya quiero taclear.
>
> Surgió un extraño error relacionado a mis floats; por alguna razón se quiebra, los lee siempre con valor de "0.0", no importa si es un int, float o ID de otra variable ya declarada o no... Llevo horas investigándolo, ni el ChatGPT pudo decirme bien qué sucede, pero creo lo iré resolviendo a lado de la memoria/MV, para ya no perder tiempo.

**14 Mayo 2023 - Mockingjay Parte 2**

> Pendiente: Léxico de Return, del Exponencial y de Corchetes al asignar matrices (int x[2][2] = [**{**1,2**}**, **{**1,2**}**]).
>
> Acabé las condicionales y otros problemas con el léxico, lo considero ya terminado aunque siga el error del CTEF allí, lo intentré resolver conforme vaya avanzando con la memoria, porque el error es una estupidez muy difícil, todo está bien escrito y diseñado, ha de ser algo bien pequeño y difícil de ver, no puedo perder mucho tiempo en ello.
>
> Inicié un mapa de memoria y de máquina virtual sencillos, no creo que estén bien o vayan a servir tal como están, pero siento son un inicio. Por ahora se inicializa con los stacks vacíos, puede verificar que la operación a realizar puede caber en la memoria de x bytes asignados, leer y escribir en el stack, lo que me falta es la lógica para los cuadruplos y las intervenciones/nodos durante la compilación, investigaré cómo hacerlos.
>
> (https://youtu.be/QKdFtnnj2lk?t=173 - Yo vs todas mis neuronas después de esta materia)

**16 Mayo 2023 - Memento**

> Me recomendaron utilizar los diccionarios de Python para la memoria, y tenían razón. Es una chulada de estructura de datos. Diseñé lo que creo sería uno de los primeros nodos neuronales de la semántica, uno en el que se guardaría los operandos, como prueba por ahora, en lo que veo cómo lee y escribe los valores del Ply y Yacc (es una variable llama "p" que según yo contiene el elemento leído más reciente...).

![1684256071125](image/README/1684256071125.png)

**17 Mayo 2023 - Irreversible**

> Tomé la decisión de abandonar la declaración de matrices al estilo R, con rangos o colon, es decir: "float listota**[3:3]** <- {1.5, 1.3...};". Perdí fácilmente más de 7 horas a lo largo de varios días intentando repararlo. Ni ChatGPT puede, ya intentamos de todo: procedencia en la lista de tokens, typos, el orden de las reglas, etc. Nada lo soluciona, y solamente parece ser esa regla de mi producción "p_vars", la cual dice así:
> "| type ID LEFTBRACKET CTEI COLON CTEI RIGHTBRACKET vars_equals SEMICOLON''' ". Por más que le he movido al lexer y a otras reglas, nada lo soluciona, está muy raro y solo sucede allí hasta ahora, así que creo que mejor lo cancelaré o dejaré al último.
>
> Fuera de eso, añadí los primeros intentos de extracción de IDs, types y después operandos y operadores para ir desarrollando la memoria. Sigo viendo cómo serían algunos casos, pero creo ya entendí cómo va a ser.

**20 Mayo 2023 - Joker**

> Había olvidado añadir a los bools, así que lo hice. Avancé a semántica, pero perdí tiempo con el debugging de la extracción de los tokens para crear cuádruplos. Terminé dándome cuenta que, Yacc y Ply guarda el nombre de los arrays o matrices con todo y dimensiones en brackets pegados (es decir, si tengo una declaración que dice "int matriz[4][5] = {1, 2, ...}" y quisiera que al llamar "p[2] me regresara el token ID "matriz", regresa en realidad "matriz[4][5]"), lo cual me obligó a cambiar mi diseño inicial para las reglas de semántica: quería que estuvieran en un archivo separado, adentro de una clase/objeto llamado "Rules" o "Semantics", pero eso implicaría varios códigos para lidiar con varios tokens pegados de distintas maneras en distintos statements, o el camino más fácil: que las reglas de semántica estén en el mismo archivo del Parser, y se manden a llamar en medio de las producciones de léxico y sintaxis. Veré si así, llamar a p[n] me regresa los tokens de forma individual y apropiada. Haría de la lectura del léxico y sintaxis más detallada, por incluir los nombres de los nodos neuronales ahora, pero no importa, creo que está hasta mejor para aprender.
>
> No funcionó, tendré que lidiar con strings de diferentes tipos. Soy un payaso. Al menos Semantics.py tendrá uso después de todo, y se verá más organizado y modular.

**22 Mayo 2023 - WTF**

> Bitácora espacial 23-05-23, estoy perdiendo la cabeza. Por cada cosa simple que hago, salen errores abstractos. Al momento de meter filas a mi diccionario de symbolTable, por alguna razón sobreescribe todos los índices con el mismo hasta el final, lo cual es imposible, el counter/index nunca lo repito, etc. Tampoco soy tan pelele con los loops y estas cosas; es Dios el quien no quiere que me gradúe.

**23 Mayo 2023**

> Después de 7 horas (no es broma) mirando la pantalla, descubrí que en Python necesito hacer un ".copy()" al momento de guardar una nueva fila en la symbol table, sino lo manda como pointer, como referencia, y eso estuvo rompiéndome la cabeza terrible todo este tiempo. Pensé que el problema era en el counter, en mis ifs, etc. Ya pude al fin extraer las variables y sus tipos, con esto ya puedo extraer lo que sea.

**24 Mayo 2023**

> Cambié la symbolTable de un diccionario, a pilas de Types, Names, etc. Puedo unirlos en una misma matriz o lista de tuplas, para evitar las keys de los hashmaps/diccionarios (no sabía que eran lo mismo). Igual, me empujó a estructurar el código de manera más limpia (separé el registro de IDs en una sola production rule para así evitar ciertas complicaciones con la memoria, declaración de variables cíclicas, etc.).

**26 Mayo 2023**

> Reescribí casi toda mi lógica de extracción de datos, para que en vez de utilizar un diccionario utilice una lista de tuplas, o lista de listas. De esta manera ya no se desperdicia espacio con las keys "type", "name", etc que se repetían mil veces cada una.
>
> Eso me llevó tiempo, sin embargo, de paso terminé de extraer y ordenar los valores también, lo cual se puso algo difícil porque esto se lee de derecha a izquierda, tuve que crear una pila que separe los elementos de cada variable declarada según las comas. Está feo, muy duct tape en mi opinión, pero funciona. Solo me falta separar las variables por sus funciones y separarlas de locales a globales, después de ello checar los tipos, que sean compatibles, finalmente meterme con los cuádruplos y completar lo que me falte. Siento me falta mucho, se siente muy pesado, pero seguiré a ver qué me sale.

**27 Mayo 2023**

> Planeé cómo diferenciar las variables de globales y locales y también insertar las dimensiones de las variables que lo tengan (variables de un solo valor la tienen vacía, pero mientras escribo esto, creo conviene hacerlas None, por si declaran una lista vacía, no se confunda con una variable de un valor tal vez. Pensé dejarlas adaptables, dinámicas, tipo python o R creo, donde casi todo es un array... O confirmar si tiene dimensiones primero, eso es mejor, me guarda tiempo y espacio), y lo logré esta mañana. Fue sencillo y corto.
>
> Más tarde arreglé la asignación de tipos y tuve que crear una regla "imaginaria", "general" del programa similar al LittleDuck donde primero se deben declarar las variables y desués ejecutar expresiones, igualmente dentro de una función. Sé que pone limitaciones en el lenguaje, pero ya me quiero enfocar en aprender a construirlo, me la compliqué demasiado al intentar diseñar un parser que fuera dinámico, casi como un lenguaje real y completo. Soy un imbécil, ya lo sé, quise lucirme, pero con esta regla, ya tengo todo lo que necesito para empezar los cuádruplos.

**28 Mayo 2023**

> Empecé el diseño y construcción de los métodos que construirán los cuádruplos. Medité la presentación en la mañana como un monje tibetiano. Intentaré hacer las expresiones primero, después funciones y returns, lo que falte. He tenido demasiadas complicaciones con PLY, creo que su manera de trabajo es toda una lógica distinta, porque me llega todo al revés, de derecha a izquierda, bottom-up parsing. Por ende me forza a vivir de pilas y contadores y de ponerme la trusa afuera, pero intentaré. Dios me bendiga.
>
> Bug fix que pudo haber cambiado mi vida desde el inicio: mi regex para números floats aceptaba integers tambien (r'[0-9]\.[0-9]+|[0-9]+'). Tuve que cambiarlo a que solo lea floats (r'[0-9]\.[0-9]+').
>
> Igualmente acabo descubrir cómo ejecutar acciones antes y durante la lectura del parser con PLY... Doy asco, me gustaría reescribir todo, pero ya no puedo.
>
> Terminé de construir/copiar la lógica de los cuádruplos de expresiones, solo me falta descifrar qué hacer con "AVAIL.next()" y "If any operand were a temporal space, return it to AVAIL" ... Igualmente, acabé el cubo semántico, ya checa los tipos y envía error que rompe el programa y te dice la expresión problemática; sin embargo, me falta hacer que los IDs entren con sus valores apropiados (ya los tengo declarados en la symbolTable) en vez como strings/chars. Tendré que asegurarme que sea local/global, índice de lista (después), etc.

**29 Mayo 2023**

> Saliendo de clase copié y adapté la lógica de las presentaciones para las expresiones, condicionales y ciclos while; me falta descifrar qué hacer con AVAIL y FILL.
>
> Estoy viendo que mi lógica de funciones se va a complicar demasiado, por no haber sabido cómo ejecutar acciones antes o durante, solo al final, todo lo hice como una especie de vector polaco masivo, leyendo de derecha a izquierda todo, sosteniéndome de las comas para saber dónde parar, dónde seguir, etcétera... No tengo ya la cabeza para reescribir algo así de grande otra vez, siento que me estoy arriesgando, así que primero me enfocaré en que la VM pueda ya leer y resolver operaciones, returns, prints, al menos para las expresiones primero, después subiré con las funciones y/o recursión.
>
> Después de jugar Tears of the Kingdom en el TEC un rato, desenredé mi cerebro, diseñé y construí el set de espacios temporales AVAIL. Con ayuda de ChatGPT recordé el uso de métodos estáticos y también el comando 'f' de Python 3.6, para crear strings, útil al momento de generar 't1, t2, t3 ...'.
>
> Durante la noche avancé a otro proyecto final, tengo dos: editar un script que escribí anteriormente en clase de Guinismo, y diseñar una caja para Diseño Gráfico. Me siento agobiado, tal vez terminaré sacrificando algo. No me quedó tiempo hoy para construir el FILL().

**30 Mayo 2023**

> Ya reentendí que FILL() lo usamos para asignar la línea a cuál saltar en un GOTOF ("ir a cierta línea si la variable es False") o GOTOV ("ir a cierta línea si la variable es True") ...
>
> Lo logré. Construí el método "FILL(líneaACuálSaltar, dóndeEnLosCuádruplos)", arreglé varios errores y finalmente los cuádruplos para expresiones lineales se construyen sin problema. Tuve que igual crear un método que busque el nombre del ID en la symbolTable para ver si existe, sacar su tipo y valor. Ese método sé que sufrirá muchos cambios, pues faltará checar si es global o local, si es una lista o matriz, en dónde, etc. Por ahora, ya funciona hacer expresiones lineales, al menos lo primero, aún faltan los returns y los prints. El órden de los cuádruplos se ve bien, regresa error si son de tipos incorrectos o si la variable aún no ha sido declarada...
>
> Por ahora necesito mirar mi techo una hora para reflexionar qué es mi vida.

**31 Mayo 2023**

> Pasé la mayor parte del día terminando mis otros dos proyectos finales (diría que están al 90%, ya no deberían molestarme para nada otra vez), y también desarrollé la lógica inicial de la Virtual Machine. Aún no la testeo porque me falta introducir los tokens de PRINTS, solo que no estoy seguro si así como es se mete (un string "PRINT") y ya solo se mete eso al switch enorme, imprimir el register apropiado... Quiero esperarme a mañana en la mañana porque tengo algo de miedo con volver a tener que editar la Semántica/Parser por ahora, se me hizo tarde.

**1 Junio 2023**

> Ya no me están naciendo las ganas de seguir esforzándome. Más del 70% de las mujeres en México (y hombres) abortan a gente como mi hermano, 100% en Europa. ¿Para qué hago esto? Solo me recuerda todo el tiempo y dinero que he perdido para nada, ya nada me hace feliz, ni el dinero ni nadie; saldré de aquí virgen de labios y sexo, nadie nunca se me acercó primero, nadie nunca me amó, nadie nunca me habló o me preguntó cómo estaba, y a la vez me echan toda la culpa de ello, como si de mi todo dependiera todo; me juzgaron por feo, me trataron literalmente como tratan a mi hermano con síndrome de down: me ignoran, me miran mal, con asco o disgusto, o me utilizan. Ya no me nace esforzarme por un mundo así, todos esos 4 de cada 5 equipos al semestre que me dejaron todo el peso de los proyectos encima ya me drenaron todo, ya no puedo seguir. Me duele la cabeza intentar.

**2 Junio 2023**

> Logré desarrollar la asignación y el print para expresiones lineales básicas (por lo tanto, debe funcionar para lo demás con facilidad, actualiza el valor de las variables sin problema). Al final me preocuparé por cambiarlo de una búsqueda O(n) a O(1) con las tablas de direcciones virtuales (3001, 3002...) si es que logro lo que me falta. Por ahora me importa más alcanzar las matrices, funciones, recursión y returns... Para ello ocupo volver a meterme a la semántica (Díos me bendiga) y meter la cantidad de parámetros o variables que cada función va utilizar. Por mi mal diseño inicial, esto va a doler.
>
> Para probar expresiones lineales básicas, probar con prueba2.txt
>
> Llevan ya desde las 11 hasta 3PM martillando la pared afuera de mi casa, toda esta semana. Parece como si los vecinos hubiesen escogido este tiempo con malicia para empezar una construcción inútil. Este tipo de cosas siempre me suceden.
>
> Logré insertar la cantidad de variables (incluyendo parámetros) que requiere el ERA para cargar la memoria de una function call. Tipo: [5i, 3f, 2b, 8s] ...
> Por legibilidad en la terminal vienen así, con el char pegado; ya después los separo o reemplazo. Pienso en modo que ahorita quiero sacar la carne del proyecto, la más que pueda, y la fase de mantenimiento (fuera del proyecto) sería donde pulo mi código. No digo que lo escribí mal, comento todo lo importante y pienso en hacerlo lo más cercano a O(1) posible, pero a veces me hago bolas, bolas que aprendo a desenredar después.
>
> Pasé la noche arreglando mi IF/ELSE. Ya funcionan, pero solo aritméticamente, por alguna razón no lee strings aún. Me saltaré eso por ahora, desde un principio del proyecto creo que mencioné la opción de ignorarlos al igual que los chars, no recuerdo, porque no los tengo añadidos en mi regla TYPE o var_cte, solamente en una personalizada que se me ocurrió a mí, pero no me sirvió para conectarlo, los strings me aparecen como "False". Fuera de eso, funcionan; pueden haber varios if/else seguidos (prueba4.txt).

~Óscar Antonio Hinojosa Salum A00821930
