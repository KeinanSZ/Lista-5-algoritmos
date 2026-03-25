try:
    x = float(input('Digite o valor brow: '))
    y = float(input('Digite o valor brow: '))
    resultado = x / y
    print(f"Resultado: {resultado}")

except ZeroDivisionError:
    print("Não vai, não. Tente novamente (não divida por zero).")

except ValueError:
    print("Aí não, brow! Digite apenas números.")

except Exception as e:
   
    print('Ocorreu um erro inesperado o.O: {e}')

finally:
    print('Tenha um bom dia ou boa noite!!!')





#Capturando exceções múltiplas: Crie um programa que peça ao usuário o 
#nome de uma cor e mostre seu valor em RGB de acordo com um dicionário 
#pré-definido. O programa deve tratar exceções caso o nome da cor não exista 
#no dicionário. 
#cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': 
#(0, 0, 255)}



# Programa para buscar valor RGB de uma cor com tratamento de exceções


cores = {
    'vermelho': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul': (0, 0, 255)
}

try:
    cor = input("Digite o nome de uma cor (vermelho, verde, azul): ").strip().lower()
    if not cor:
        raise ValueError("O nome da cor não pode estar vazio")
    valor_rgb = cores[cor]
    print(f"O valor RGB da cor '{cor}' é: {valor_rgb}")
except KeyError:
    print("Erro: Cor não encontrada no dicionário")
except ValueError as ve:
    print(f"Erro de valor: {ve}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")




#Bloco else e finally: Escreva um programa que solicite um número ao 
#usuário. Se o número for maior que 10, exiba uma mensagem dizendo que o 
#número é válido. Utilize o bloco else para imprimir que o programa foi 
#executado com sucesso, e o bloco finally para imprimir "Programa encerrado".



try:
 
    numero = float(input("Digite um número: "))

   
    if numero > 10:
        print("O número eh válido (maior que 10).")
    else:
        print("O número não eh maior que 10.")


except ValueError:
    print("Entrada inválida! Por favor, digite um número.")


else:
    print("Programa executado com sucesso.")

finally:
    print("Programa encerrado.")




#Exceções personalizadas: Escreva uma função que verifica se uma senha 
#possui no mínimo 8 caracteres e pelo menos um número. Se a senha não 
#atender aos requisitos, levante uma exceção com uma mensagem 
#personalizada. Trate a exceção e mostre a mensagem ao usuário. 


class SenhaInvalidaError(Exception):
    pass
def validar_senha(senha):
    if len(senha) < 8:
        raise SenhaInvalidaError("A senha deve ter pelo menos 8 caracteres.")
    if not any(c.isdigit() for c in senha):
        raise SenhaInvalidaError("A senha deve conter pelo menos um número.")
    return True

try:
    senha = input("Digite sua senha: ")
    validar_senha(senha)
    print("Senha válidaaa")
except SenhaInvalidaError as e:
    print(f"Erro: {e}")


#---------------------


try:
    saldo = float(input("Saldo: R$ "))
    valor = float(input("Transferência: R$ "))
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    print(f"Transferência ok! Saldo: R$ {saldo - valor:.2f}")
except ValueError as e:
    print(f"Erro: {e}")














