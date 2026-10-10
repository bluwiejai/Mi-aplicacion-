Actúa como un desarrollador experto en Python y Streamlit, especializado en e-commerce y diseño de interfaces de usuario (UI/UX). 

Por favor, escribe el código completo en un solo archivo Python (.py) para una página web interactiva de Streamlit para una marca de ropa deportiva llamada "FitVibe Athletics".

El código debe incluir los siguientes elementos:

1. **Configuración de la Página y Estilos:**
   - Usa un layout ancho (`layout="wide"`).
   - Aplica un estilo visual moderno y enérgico (puedes usar CSS personalizado inyectado con `st.markdown` para darle colores deportivos, por ejemplo, tonos oscuros con acentos en verde neón o naranja).

2. **Barra Lateral (Sidebar) de Navegación y Filtros:**
   - Menú de navegación con las siguientes secciones: 
     * 🏠 Inicio / Tienda
     * 🔥 Productos Destacados
     * 🛒 Mi Carrito de Compras
     * 📞 Contacto
   - Filtros en la barra lateral para la sección de tienda:
     * Categoría (Hombre, Mujer, Accesorios).
     * Rango de precios.

3. **Sección de Productos (Catálogo):**
   - Muestra al menos 6 productos deportivos diferentes (ej. Leggings de compresión, Camiseta dry-fit, Zapatillas de running, Sudadera térmica, Short de entrenamiento, Botella deportiva).
   - Cada producto debe mostrar: Nombre, Categoría, Precio, una imagen representativa (puedes usar URLs de imágenes de prueba de Unsplash) y un botón de "Agregar al carrito".

4. **Funcionalidad del Carrito de Compras:**
   - Utiliza `st.session_state` para almacenar los productos que el usuario va agregando.
   - En la sección del Carrito, muestra la lista de productos seleccionados, el cálculo del total a pagar y un botón de "Simular Pago / Finalizar Compra" que muestre un mensaje de éxito con confeti (`st.balloons()`).

5. **Buenas prácticas:**
   - Código limpio, comentado y listo para ejecutarse usando `streamlit run app.py`.
   - Manejo correcto del estado de la sesión (`st.session_state`) para que los datos no se pierdan al interactuar con la página.
