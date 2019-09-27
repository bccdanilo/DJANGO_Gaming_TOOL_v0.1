num1 = input('Entre com o 1º valor: ')
 
num2 = input('Entre com o 2º valor: ')
 
soma = int(num1) + int(num2)
 

def mult(num1, num2):
    if(num1 > num2):
        return int(num1) * int(num2)
    else:
        return int(num1) - int(num2)


print ("A soma é",soma)
print ("fn:", mult(num1,num2))


