import streamlit as st
# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción

st.title("Tu calculadora de rebajas 🛍️🤑")
st.markdown('''**Bienvenido**, :rainbow[introduce] tus datos para calcular lo que tienes que pagar despues de las rebajas.''')
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Datos")
precio_original= st.sidebar.number_input("El precio (€)", min_value=0, max_value=100000, value=50000)
descuento= st.sidebar.slider( "rebaja (%)", 0.00, 100.00, 50.00)

# 3. Botón de Cálculo y Lógica
    # Fórmula Matemática: Precio por el descuento entre 100
if st.button("**Rabaja ahora**"):
   
    ahorro = precio_original * (descuento / 100)
    precio_final = precio_original - ahorro
   
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
     
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu precio final", value=f"{precio_final:.2f}")
       
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if descuento < 10:
            st.warning("Buen descuento👍👍")
            st.write("meh👍👍.")
            st.snow()
        elif descuento < 50 > 30 :
            st.success("muy buen descuento👌👌")
        elif descuento > 50 :
            st.warning("descuentazo🤑")
            st.write("te a tocado la loteria🎉🎉 .")
            st.balloons() # ¡Premio!
