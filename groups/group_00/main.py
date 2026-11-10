"""
PhotoCensus - Group 00 (TEMPLATE)

Copy this folder to /groups/group_XX/ (XX = your group number)
and write your project here. Do not modify anything in /kit.
"""
import os
import sys

# Lets this file find black_box.py in /kit (do not remove these lines)
GROUP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(GROUP_DIR, "..", "..", "kit"))
from black_box import *  # noqa: E402,F401,F403


def main():
    nivel_confianca = 0.5
    print("PhotoCensus - Group 01")
    show_folders()
    # Your menu (while loop) starts here...
    while True:
        print("=== PHOTOS CENSUS ===")
        print(" 1 - Configurar confiança.")
        print(" 2 - Anasilar uma foto.")
        print(" 3 - Contar uma classe.")
        print(" 4 - Relatório da pasta.")
        print(" 5 - Foto mais cheia e mais vazia. ")
        print(" 6 - Procurar uma classe. ")
        print(" 7 - Gráfico de barras. ")
        print(" 0 - Sair. ")
        
        option = int(input("Escolha uma opção: "))
        
        if option == 0:
            print("Programa encerrado!")
            break

        elif option == 1:
            # O usuario define o nível de confiança para um valor entre 0 e 1.
            print("Você escolheu configurar confianca")
            confianca = float(input(" Digite o nível de confiança: "))
            while confianca < 0 or confianca > 1:
                print("Confiança inválida!")
                confianca = float(input("Digite novamente: "))
            nivel_confianca = confianca

        elif option == 2:
            print("Você escolheu analisar uma foto")
            pasta = input("Digite o nome da pasta: ")
            
            # Verificando se a pasta informada existe atraves do folder exists
            while not folder_exists(pasta):
                print("Pasta não encontrada!")
                pasta = input("Tente novamente: ")
            
             # Chamando a funçao total photos e guardando o resultado na variavel total   
            total = total_photos(pasta)
            numero = int(input("Digite o número da foto: "))

            # Validadando o número digitado
            while numero < 1 or numero > total:
                print("Número inválido!")
                numero = int(input("Digite novamente: "))

            # Chamando a função photo name 
            # Guardando resultado (Caminho) na variavel foto
            foto = photo_name(pasta, numero)

            # Chamando a funcao count objets 
            # Ela recebe foto e nivel de confianca
            # retorna a quantidade objetos identificados na foto
            quantidade = count_objects(foto, nivel_confianca)

            # Chamando a funcao main object
            # Ela recebe a foto e retorna o objeto considerado principal 
            # Armazenei na variavel principal
            principal = main_object(foto)

            # Chamando a funcao max confidence 
            # verifica os niveis de confianca dos objetos
            # retona o maior valor encontrado
            # Armazenei na variavel maior confianca
            maior_confianca = max_confidence(foto)

            # So calculei a porcentagem 
            porcentagem = maior_confianca * 100

            print(f"Caminho: {foto}")
            print(f"Quantidade de objetos: {quantidade}")
            print(f"Objeto principal: {principal}")
            print(f"Maior confiança: {porcentagem} %")
            

        elif option == 3:
            print("Você escolheu contar uma classe")

            folder = input("Digite o nome da pasta: ")
            
            # Validando se pasta digitada existe
            # utilizando o folder exists
            while not folder_exists(folder):
                print("Pasta inválida!")
                folder = input("Digite novamente: ")

            # Chamando a funcao total photos
            # Armazenei na variavel total
            total = total_photos(folder)

            number = int(input("Digite o número da foto: "))
            
            # Validando o número digitado 
            while number < 1 or number > total:
                print("Número inválido!")
                number = int(input("Digite novamente: "))
            
            # Chamando a funcao photo name
            # Retorna o caminho da foto
            photo = photo_name(folder, number)

            # Solicita o a classe do objeto que o usuário deseja achar na foto
            # ex: pessoa, cachorro
            # armazenei na variavel claas name
            class_name = input("Digite a classe que deseja procurar: ")

            # Chamando a funcao count class 
            # Ela conta quantos objetos da classe escolhida tem na foto
            # armazenei o resultado na variavel quantity
            quantity = count_class(photo, class_name, nivel_confianca)

            print("Quantidade encontrada:", quantity)
 
       elif option == 4:
            print("Você escolheu relatório da pasta")

       elif option == 5:
            print("Você escolheu foto mais cheia e mais vazia")

       elif option == 6:
            print("Você escolheu procurar uma classe")

       elif option == 7:
            print("Você escolheu gráfico de barras")

       else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
