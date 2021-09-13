import streamlit as st
import sys

option = st.sidebar.selectbox("Asignatura", ("Front page", "Mecánica", "TBC"))

if option == "Front page":
    st.write("""
    # Calculadora de notas de 2º Física UAB
    Despliega el side-bar para elegir la materia.
    """)
elif option == "Mecánica":
    st.write("""
    # Calculadora Mecánica Clásica
    """)
    ponderaciones = [0.225, 0.225, 0.225, 0.225, 0.1]
    notas = []
    st.write("### EXÁMENES")
    exam_1 = st.slider("Nota primer parcial", 0.0, 10.0, step=0.01)
    notas.append(exam_1)
    exam_2 = st.slider("Nota segundo parcial", 0.0, 10.0, step=0.01)
    notas.append(exam_2)
    exam_3 = st.slider("Nota tercer parcial", 0.0, 10.0, step=0.01)
    notas.append(exam_3)
    exam_4 = st.slider("Nota cuarto parcial", 0.0, 10.0, step=0.01)
    notas.append(exam_4)
    st.write("### PROBLEMAS")
    problems = st.slider("Nota problemas", 0.0, 10.0, step=0.01)
    notas.append(problems)
    final_mark = 0.00

    for i in range(len(ponderaciones)):
        final_mark += notas[i] * ponderaciones[i]

    st.write("""
    ### Tu nota es de:\n
    ## {}
    """.format(final_mark))

    if final_mark >= 5:
        st.write(r"""
        APROBADO por
        """ + str(final_mark - 5.0))
    else:
        st.write(r"""
        F
        """)
else:
    st.write("""
    ### Estate atento a futuras actualizaciones
    """)