
# importar librerías básicas
import pandas as pd
import streamlit as st
from datetime import datetime

# tantito backend
hoy = datetime.today()
meses = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre" }

# formatito
# region
st.markdown("""
<style>
@font-face {
    font-family: 'Gilroy';
    src: url('https://raw.githubusercontent.com/majoocharteKellanova/oc-to-transit/main/assets/gilroy-medium.ttf');
}
            
/* fuente global */
*, div, span, section, button, label, input, textarea, h1, h2, h3, p {
    font-family: 'Gilroy', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)
# endregion

st.image(
    "https://raw.githubusercontent.com/majoocharteKellanova/costco-scorecard/main/assets/costco-header.png",
    width=450
)

st.markdown(
"COSTCO SCORECARD",
unsafe_allow_html=True
)

# botón y variable para guardar el archivo
info = st.file_uploader("sube aquí la información de inventarios", type=["csv"], accept_multiple_files=False)

# ponemos la condicional del archivo para seguir el proceso
if info: # una lista vacía se considera False y una con elementos True (recorderis)
    df = pd.read_csv(info, skiprows=1)
    
    # detectar columnas de fechas
    cols_fecha = [c for c in df.columns if c.startswith("1 Semana terminando el")]

    # # reemplazar las columnas repetidas por una nueva variable
    # for c in cols_fecha:
    #     df['Semana'] = 
        
    # preview del dataframe
    st.markdown("inventarios semanal", unsafe_allow_html=True)
    st.dataframe(df.head())

else:
    st.info("carga un archivo para comenzar")
