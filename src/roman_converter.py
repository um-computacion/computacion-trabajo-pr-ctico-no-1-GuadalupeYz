
def decimal_to_roman(num: int) -> str: 
    dicc_romano = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C",  90: "XC",  50: "L",  40: "XL",
        10: "X",   9: "IX" ,  5: "V",   4: "IV",
        1: "I"
    }               
    resultado = []      
    for valor, simbolo in dicc_romano.items(): 
        cantidad = num // valor   
        resultado.append(simbolo * cantidad)
        num %= valor    
        
    return ''.join(resultado) 

if __name__ == "__main__":     
    numero = int(input("Ingrese un numero: "))
    if 1 <= numero <= 3999:
        romano = decimal_to_roman(numero) 
        print(f"El numero {numero} en numeros romanos es: {romano}")
    else:
        print("Error: El numero debe estar entre 1 y 3999")













