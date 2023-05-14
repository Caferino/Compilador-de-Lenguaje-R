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

**13 Mayo 2023 - Mockingjay Parte 2**

> SDD.
>
> (https://youtu.be/QKdFtnnj2lk?t=173 - Yo vs todas mis neuronas después de esta materia)

~Óscar Antonio Hinojosa Salum A00821930
