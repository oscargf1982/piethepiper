# Prompt · Fondo del combate en el puente

## A) Para Claude (adjunta la foto referencia-puente-venecia.png)

```
Te adjunto una foto real de un canal de Venecia con un puente de piedra. Úsala como referencia de composición y arquitectura para crear el FONDO DE COMBATE de mi videojuego educativo "Pay the Piper".

CONTEXTO DEL JUEGO
- Reinterpretación oscura del Flautista de Hamelín, ambientada en Venecia durante la peste de 1630. Es de noche.
- Combate por turnos: el Flautista (izquierda) se enfrenta a "Il Dottore del Ponte", un médico de la peste con máscara de pico (derecha). Los dos luchan DE PIE SOBRE EL PUENTE.
- Lo juega alumnado de 14 años en adelante: el tono puede ser oscuro e inquietante de verdad (peste, muerte, abandono).

QUÉ NECESITO
Un fondo dibujado en código (no puedes generar imágenes, así que hazlo como SVG o como función de HTML canvas), con aspecto de ilustración a mano: tinta y acuarela oscura, tipo grabado gótico. Usa trazos irregulares, sombreado de líneas cruzadas (hatching), manchas de acuarela con transparencia y bordes algo temblorosos. Nada de formas geométricas limpias ni degradados planos de videojuego.

TRANSFORMA LA FOTO ASÍ
- Pasa del día soleado a una noche de peste de 1630.
- Mantén: el canal estrecho que se pierde al fondo, las casas altas apretadas a ambos lados con contraventanas, el puente de piedra de un solo arco con escalones en los extremos, el reflejo del arco en el agua.
- Elimina todo lo moderno: barcas a motor, farolas eléctricas, antenas, tuberías, cables.
- Añade: góndolas amarradas cubiertas con paños negros, palos de amarre a rayas, faroles de aceite colgados en algunas fachadas, alguna ventana con luz de vela y la mayoría cerradas, una cruz o marca de peste pintada en una puerta, ropa tendida rota, gatos o ratas en sombra en un alféizar.
- Cielo negro rojizo con una gran LUNA ROJO SANGRE arriba a la derecha.
- NIEBLA VERDE enfermiza flotando sobre el agua y entre las casas.
- Las plantas de los balcones de la foto: conviértelas en macetas secas y enredaderas muertas.

PALETA (respétala)
Negro #0b0a09, negro tinta #17120f, blanco hueso #e8dcc0, piedra #5a4b3c, carmesí #8e1b16, rojo luna #b8281e, niebla verde rgba(130,165,110,0.15), luz de vela #e6963c.

COMPOSICIÓN Y MEDIDAS (importante, debe encajar en mi prototipo)
- Vista lateral, cámara frontal al puente, como un escenario de teatro.
- Tamaño 960 × 540 px. La parte visible del escenario es la franja de ARRIBA, de y = 0 a y = 370. La franja de abajo (370 a 540) la tapa la interfaz: rellénala solo con agua oscura.
- El tablero del puente es la línea donde pisan los personajes. Debe seguir esta curva: y = 250 + ((x − 480) / 360)² × 34, desde x = 90 hasta x = 870 (alto en el centro, y = 250; más bajo en los extremos, y ≈ 290). Dibuja el pretil bajo de piedra justo encima de esa línea.
- Bajo el puente, el arco va aproximadamente de x = 250 a x = 710, con el hueco oscuro y su reflejo en el agua (agua entre y = 285 y y = 370).
- Deja DESPEJADAS dos zonas donde irán los personajes (miden unos 170 px de alto): alrededor de x = 270 (Flautista) y de x = 690 (Dottore), desde y ≈ 90 hasta el tablero. Detrás de ellos, solo fondo lejano y oscuro para que sus siluetas se lean bien.
- Lo más detallado y oscuro, en los laterales (casas en primer plano a izquierda y derecha); el centro, más neblinoso y claro, con el canal que se aleja.

ENTREGA
1. Un único archivo HTML autocontenido que muestre el fondo a 960 × 540 (sin librerías externas), con un botón para descargarlo como PNG.
2. Si lo haces en canvas, pon todo el dibujo dentro de una función `bg(t)` que use un contexto llamado `ctx`, para poder pegarla en mi juego. Usa `t` (segundos) solo para animaciones suaves: llamas de velas que parpadean, ondas del agua y niebla que se desplaza despacio. Si lo haces en SVG, que las animaciones sean CSS.
3. Para ver cómo encaja, dibuja encima dos siluetas provisionales semitransparentes en x = 270 y x = 690 de pie sobre el puente, que pueda ocultar con una casilla "mostrar personajes".
```

## B) Variante para un generador de imágenes (ChatGPT, etc.)

Adjunta la misma foto y, si quieres, las hojas de personaje para que entienda el tono.

```
Using the attached photo of a small Venetian canal with a stone footbridge as composition reference, create a 2D side-view video game background, 16:9, 1920×1080. Same canal, same single-arch stone bridge centred, tall narrow houses on both sides, the canal receding into the distance.

Transform it into Venice at night during the plague of 1630: hand-drawn dark ink and watercolour illustration, gothic engraving style with cross-hatching, rough brush strokes and paper texture. Palette: black, bone white, weathered stone, crimson accents. A huge blood-red moon in the upper right of a black-red sky. Sickly green fog drifting over the water and between the houses. Remove all modern elements (motorboats, electric lamps, antennas, pipes). Add gondolas draped in black cloth, striped mooring poles, oil lanterns on the walls, a few windows lit by candles, shutters closed, dead potted plants on the balconies, a plague cross painted on one door.

The bridge deck is the stage: keep the bridge walkway clear and empty, with open space on the left half and right half of the bridge for two characters to be added later. No people, no characters, no text. Dark, oppressive and eerie, for a teenage audience (14+). The bottom third of the image is dark canal water with the reflection of the arch.
```

Nota: la imagen de ChatGPT saldrá a 1920 × 1080; para el prototipo habría que reducirla a 960 × 540 y ajustar la curva del puente a mano. Por eso para meterla directamente en el juego es más cómoda la versión A.
