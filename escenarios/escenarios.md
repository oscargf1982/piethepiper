# Pay the Piper · Índice de escenarios

Referencias y fondos de los escenarios del juego. Estilo general: tinta y acuarela oscura tipo grabado gótico; paleta negro, blanco hueso, carmesí, niebla verde enfermiza y luna rojo sangre. Venecia, peste de 1630. Público: alumnado de 14 años en adelante (cambio del 2026-11-21), así que se admite un tono oscuro de verdad.

## Escenario 1 · El puente del canal (combate contra Il Dottore del Ponte)

- **Referencia real:** [referencia-puente-venecia.png](referencia-puente-venecia.png) — foto de día de un canal estrecho con un puente de piedra de un solo arco, casas altas a ambos lados, plantas en los balcones y barcas a motor amarradas.
- **Versión del juego:** noche de peste de 1630. Se quitan barcas a motor, farolas modernas y antenas; góndolas cubiertas de paños negros; niebla verde sobre el agua; luna roja; faroles de aceite en las fachadas; ventanas cerradas o con una vela.
- **Uso:** fondo del prototipo [pay-the-piper-combate.html](../pay-the-piper-combate.html). Lienzo 960 × 540; el escenario visible ocupa la franja de arriba (0 a 370 px) y la de abajo queda tapada por el pentagrama.
- **Posiciones en el prototipo:** el Flautista está a x = 270 y el Dottore a x = 690. Miden unos 170 px de alto.
- **Prompt para pedírselo a Claude:** [prompt-fondo-puente.md](prompt-fondo-puente.md)
- **Fondo final:** [escenario-puente-combate.png](escenario-puente-combate.png) (1672 × 941). Noche roja, luna de sangre, cúpula de la Salute al fondo, niebla verde, estandarte y puerta con cruz de peste, góndola tapada.
- **Integrado en el prototipo (2026-11-21):** el fondo va dentro del HTML (reducido a 960 × 540 y subido 40 px). Los personajes y las ratas pisan los escalones reales del puente de la imagen. Si se cambia el fondo, hay que volver a medir los escalones (constante `STEPS` del prototipo).

## Escenario 2 · La cripta inundada de San Zaccaria (combate contra la Monaca, capítulo 1)

- **Fondo final:** [cripta-san-zaccaria.png](cripta-san-zaccaria.png) (1672 × 941), aportado por Oscar el 2026-11-23.
- **Descripción:** cripta románica con bóvedas de arista y columnas de capiteles tallados, medio inundada de agua negra que refleja las velas. Al fondo, en el centro, un altar de mármol con un sol grabado y una estatua de santa velada encima. A los lados, nichos con calaveras, relieves en la pared, sarcófagos, ataúdes apoyados en el muro y velas derretidas sobre las basas de las columnas. Niebla verde a ras del agua.
- **Composición para el combate:** vista frontal y simétrica. La línea del agua está más o menos a 2/3 de la altura (y ≈ 640 de 941). El altar central es el foco natural para la Monaca, y los huecos entre columnas a izquierda y derecha sirven para colocar a los combatientes. No hay suelo seco: los personajes estarían de pie en el agua o sobre las basas de las columnas.
- **Uso:** sustituye al escenario anterior del combate contra la Monaca. Lo integra en el juego el hilo del capítulo 1.
