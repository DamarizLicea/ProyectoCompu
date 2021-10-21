# ProyectoDamarizLiceaA01369045_TC1028.1

PROYECTO PENSAMIENTO COMPUTACIONAL&KEIKIZ

Proyecto en base a crear una plataforma de ordenes/cotizaciones de pasteles de mi marca (Keikiz), y guardar además la cantidad de dinero que entra/sale.

Planeada para desplegar un menú inicial que presente las diferentes opciones con las que se puede trabajar (1. Comprar en el menú del día (mini menú), 2. Hacer una cotización de pastel (se despliega un mini menú interior de sabores), 3. Hacer un pedido (también se despliega mini menú),4. Opción de corte de caja/retiro del efectivo).
Los mini menús tendrán información de sabores, cremas, decoraciones, y la variable costos por rebanada o porción individual. 

El fin de cada una de las primeras 3 secciones del menú inicial, es que proporcionen un costo o cuenta final por el conjunto de productos que se llevan/ cotizan, o que, en el caso de hacer pedidos, arrojen un costo, reimprimiendo los datos que nos proporcionó primero el cliente (nombre del cliente, sabores, porciones, crema, decoración, fecha), y de ser posible, guardarlos en un registro.

SECCION 1

Como caso especial, la sección 1 del menú principal, tendrá que repetir el mismo proceso de compra hasta que el cliente le indique que desea dejar de comprar.

SECCION 2

La sección 2 será una calculadora de precios, con variables constantes como las cajas y los precios de cada decoración o porción de pastel, que al ser procesadas algebraicamente con los datos proporcionados por el usuario (sabor, número de porciones), arroje un precio exacto del producto que necesitan, si el cliente no estuviera contento, podría repetir el proceso desde 0.

SECCION 3

Similar a la segunda sección, solamente agregando que aquí ya se le pide al cliente pagar, el costo se altera si sus opciones de pago son con tarjeta.

SECCIÓN 4
Esta sección solo sería para uso del empleado.
La sección 4 es una función para realizar un cálculo del dinero que tenemos para retirarlo como corte, el dinero se calcula mediante la cantidad de monedas o billetes de cada importe multiplicadas por su valor, despliega las cantidades que se van a cada apartado de la repostería. También despliega la fecha y el tiempo en que se ejecuta la acción.

Además de eso, hice uso de Colorama, para que el proyecto tuviera una mejor estética.
