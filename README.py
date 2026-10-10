Actúa como un desarrollador experto en Python y Streamlit, así como un diseñador UI/UX de alta gama. Escribe el código completo en un solo archivo Python (.py) listo para ejecutarse con "streamlit run app.py", para una pastelería de diseño exclusivo llamada "Starry Ocean Pâtisserie".

La pastelería fusiona la estética artística de Vincent van Gogh (pinceladas, cielo estrellado) con la majestuosidad del océano, usando una paleta de colores azules profundos y acentos dorados.

El código DEBE incluir estrictamente lo siguiente:

1. **Diseño y Estilos (CSS Inyectado con st.markdown):**
   - Layout ancho (`layout="wide"`).
   - Fondo general oscuro/azul medianoche (`#0a0f1d`), tarjetas de productos con bordes sutiles dorados (`#d4af37`), detalles en azul eléctrico/turquesa (`#1e3a8a` o `#0284c7`) y tipografía elegante con títulos dorados.

2. **Navegación con `st.sidebar`:**
   - Menú de opciones: "🌌 Catálogo Artístico", "🛒 Mi Reserva de Dulces", "✨ Encargos Personalizados".
   - Filtros en la barra lateral para clasificar los pasteles por temática ("Van Gogh", "Océano y Oro", "Clásicos").

3. **Catálogo de Productos (Mínimo 6 creaciones creativas con imágenes de Unsplash):**
   - 1. "La Noche Estrellada" (Torta de vainilla con cacao azul y hoja de oro).
   - 2. "Abismo Marino" (Cheesecake de frutos azules con textura de olas y perlas doradas).
   - 3. "Girasoles de Arles" (Cupcakes de limón con textura estilo pintura al óleo).
   - 4. "Tesoros del Océano" (Macarons con ganache de chocolate blanco y sal marina dorada).
   - 5. "Olas de Medianoche" (Torta de chocolate con degradado azul y acentos dorados abstractos).
   - 6. "Cielo de Provenza" (Tartaleta de lavanda y arándanos con caramelo dorado).
   - Cada producto debe tener su tarjeta visual con imagen, nombre, precio, descripción poética y su botón funcional "Reservar Creación".

4. **Gestión del Carrito (`st.session_state`):**
   - Almacena las creaciones agregadas.
   - En la sección del carrito, muestra la lista de postres seleccionados, el total y un formulario de reserva (Nombre, Fecha de recogida, Comentarios) con un botón de "Confirmar Reserva" que active `st.balloons()`.

5. **Requisitos técnicos:**
   - Código limpio, optimizado, sin errores de sintaxis y comentado de forma clara. 
   - Utiliza exclusivamente componentes nativos de Streamlit y Markdown/CSS.
