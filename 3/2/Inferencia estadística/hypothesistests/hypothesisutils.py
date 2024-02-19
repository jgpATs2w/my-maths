def interpret_p(p_value):
    print(f'Valor p: {p_value}')
    if p_value < 0.01:
        print("Rechaza H0 con elevada significacion estadistica .")
    elif p_value < 0.049:
        print("Rechaza H0 con significacion estadistica")
    elif p_value < 0.051:
        print("Resultados con cierta significacion estadistica, acepta o rechaza H0")
    else:
        print("Acepta H0: resultados sin significacion estadistica.")