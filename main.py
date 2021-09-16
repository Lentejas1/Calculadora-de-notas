import streamlit as st

option = st.sidebar.selectbox("Asignatura", ("Front page", "Mecánica", "Ecuaciones Diferenciales", "TBC"))
Notas = {"Mec": 0.0, "Ele": 0.0}

if option == "Front page":
    st.write("""
    # Calculadora de notas de 2º Física UAB
    ## Despliega el side-bar para elegir la materia.
    """)
elif option == "Mecánica":
    st.write("""
    # Calculadora Mecánica Clásica
    """)
    ponderaciones = [0.225, 0.225, 0.225, 0.225, 0.1]
    notas = []
    st.write("### EXÁMENES")
    mec_exam_1 = st.slider("Nota primer parcial", 0.0, 10.0, step=0.01)
    notas.append(mec_exam_1)
    mec_exam_2 = st.slider("Nota segundo parcial", 0.0, 10.0, step=0.01)
    notas.append(mec_exam_2)
    mec_exam_3 = st.slider("Nota tercer parcial", 0.0, 10.0, step=0.01)
    notas.append(mec_exam_3)
    mec_exam_4 = st.slider("Nota cuarto parcial", 0.0, 10.0, step=0.01)
    notas.append(mec_exam_4)
    st.write("### PROBLEMAS")
    problems = st.slider("Nota problemas", 0.0, 10.0, step=0.01)
    notas.append(problems)
    mec_final_mark = 0.00

    for i in range(len(ponderaciones)):
        mec_final_mark += notas[i] * ponderaciones[i]

    Notas["Mec"] = mec_final_mark

    st.write("""
    ### Tu nota es de:\n
    ## {}
    """.format(mec_final_mark))

    if mec_final_mark >= 5:
        st.write(r"""
        APROBADO por
        """ + str(mec_final_mark - 5.0))
    else:
        st.write(r"""
        F
        """)
elif option == "Ecuaciones Diferenciales":
    st.write("""
        # Calculadora Ecuaciones Diferenciales
        """)
    st.write("### EXÁMENES")
    ed_exam_1 = st.slider("Nota primer parcial", 0.0, 10.0, step=0.01)
    ed_exam_2 = st.slider("Nota segundo parcial", 0.0, 10.0, step=0.01)
    st.write("### PROBLEMAS")
    problem_1 = st.slider("Nota problema 1", 0.0, 10.0, step=0.01)
    problem_2 = st.slider("Nota problema 2", 0.0, 10.0, step=0.01)

    ed_1_mark = problem_1 + (10-problem_1)*ed_exam_1/10
    ed_2_mark = problem_2 + (10-problem_2)*ed_exam_2/10
    ed_final_mark = (ed_1_mark + ed_2_mark)/2

    st.write("""
            #### Tu nota de la primera parte es de:\n
            ### {}
            """.format(ed_1_mark))
    st.write("""
                #### Tu nota de la segunda parte es de:\n
                ### {}
                """.format(ed_2_mark))
    st.write("""
        ### Tu nota es de:\n
        ## {}
        """.format(ed_final_mark))

    if ed_final_mark >= 5 and ed_1_mark >= 4 and ed_2_mark >= 4:
        st.write(r"""
            APROBADO por
            """ + str(ed_final_mark - 5.0))
    elif ed_1_mark < 4:
        st.write(r"""
            Necesitas más de un 4 en la primera parte para hacer media
            """)
        if ed_2_mark < 4:
            st.write(r"""
                    Necesitas más de un 4 en la primera parte para hacer media
                    """)
    elif ed_2_mark < 4:
        st.write(r"""
                Necesitas más de un 4 en la primera parte para hacer media
                """)
else:
    st.write("""
    ### Estate atento a futuras actualizaciones
    # Calculadora de notas de 2º Física UAB
    Despliega el side-bar para elegir la materia.
    ### Mecánica Clásica """
    + str(Notas["Mec"]))
