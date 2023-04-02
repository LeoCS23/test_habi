
def ordenarCadena(string):

    return (''.join(sorted(string, key=lambda x: (x.isdigit(), x.isupper(), x))))


if __name__ == '__main__':

    valor = False

    while (valor == False):

        cadenaAlfanumerica =input("Ingrese cadena alfanumerica: ")
        tamanioCadena=len(cadenaAlfanumerica)

        if(tamanioCadena > 0 and tamanioCadena < 1000):
            print("cadena ordenada: " + ordenarCadena(cadenaAlfanumerica))
            valor = True
        else:
            print("Tamaño de la candena no aceptado")
