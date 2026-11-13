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
            
            def folder_report(min_confidence):
                print('\n--- Relatório da pasta ---')

                # choose folder  
                # Escolhendo a pasta validada com um while
                show_folders()
                folder = input('Digite o nome da pasta:').strip()
                while not folder_exists(folder):
                    print('Pasta inválida! Tente novamente.')
                    folder = input('Digite o nome da pasta:').strip()

                # total folder photos
                # total de fotos na pasta
                total = total_photos(folder)

                # accumulators
                # acumuladores manuais
                total_objects = 0
                empty_photos = 0

                print(f'\nPasta: {folder} | Confiança mínima: {min_confidence}')
                print('------------------------------------')

                # examination of the photos in the folders
                # examinação das fotos nas pastas ( iniciando em 1)
                for number in range(1, total + 1):
                    photo = photo_name(folder, number)
                    amount = count_objects(photo, min_confidence)
   
                    # one line per photo
                    # uma linha por foto
                    print(f'Foto {number}: {amount} objeto(s)')

                    # accumulate the total of objects
                    # acumulador do total de objetos
                    total_objects = total_objects + amount

                    # count photos with no objects
                    # contar as fotos sem objetos
                    if amount == 0:
                        empty_photos = empty_photos + 1

                # average of objects per photo
                # média de objetos por foto fora do loop "for"
                average = total_objects / total

                # Folder report result
                # resultado do relatório
                print('------------------------------------')
                print('Total geral de objetos:', total_objects)
                print(f'Média de objetos por foto: {average:.2f}')
                print('Fotos sem nenhum objeto:', empty_photos)
                print('------------------------------------')

        elif option == 5:
            print("Você escolheu foto mais cheia e mais vazia")
             
            def fullest_and_emptiest_photo(min_confidence):
                print('\n--- Foto mais cheia e mais vazia ---')

                # choose folder
                # escolher a pasta (sendo validada pelo while)
                show_folders()
                folder = input('Digite o nome da pasta:').strip()
                while not folder_exists(folder):
                    print('Pasta inválida! Tente novamente.')
                    folder = input('Digite o nome da pasta:').strip()

                # total photos in the folder
                # total de fotos na pasta
                total = total_photos(folder)

                # starting with the data of photo one
                # começando com os dados da foto 1 (para não inventar valor)
                first_photo = photo_name(folder, 1)
                highest_amount = count_objects(first_photo, min_confidence)
                highest_number = 1
                lowest_amount = highest_amount
                lowest_number = 1

                # analyze the remaining photos (from 2 to total)
                # analisar o restante das fotos (da segunda ao total)
                for number in range(2, total + 1):
                    photo = photo_name(folder, number)
                    amount = count_objects(photo, min_confidence)

                    # new highest? (strict > keeps the first photo in case of a tie)
                    # novo recorde? (estrito > mantém a primeira foto em caso de empate)
                    if amount > highest_amount:
                        highest_amount = amount
                        highest_number = number

                    # new lowest? (strict < keeps the first photo in case of a tie)
                    # novo menor valor? (estrito < mantém a primeira foto em caso de empate)
                    if amount < lowest_amount:
                        lowest_amount = amount
                        lowest_number = number

                # final result 
                # resultado final fora do laço
                print(f'\nPasta: {folder} | Confiança mínima: {min_confidence}')
                print('------------------------------------')
                print(f'Foto mais cheia: nº {highest_number} com {highest_amount} objeto(s)')
                print('Caminho:', photo_name(folder, highest_number))
                print(f'Foto mais vazia: nº {lowest_number} com {lowest_amount} objeto(s)')
                print('Caminho:', photo_name(folder, lowest_number))
                print('------------------------------------')

        elif option == 6:
            print("Você escolheu procurar uma classe")
        #Receber as informaçoes
            folder = input("Digite o nome da pasta: ")  
            while not folder_exists(folder):
                print("Pasta inválida")
                folder = input("Digite o nome da pasta novamente: ")
            class_name = input("Digite a classe desejada: ")
        
            total_fotos = total_photos(folder)
        #inicia os cont
            fotos_com_classe = 0
            total_encontrado = 0
        # perrcorrer as fotos
            for numero in range(1, total_fotos +1):
                photo = photo_name(folder,numero)
                quantidade = count_class(photo,class_name)
                total_encontrado += quantidade
        #verificar se a classe apareceu
                if quantidade >0:
                    fotos_com_classe += 1
        #calcular a porcetagem
                porcentagem = (fotos_com_classe/total_fotos) * 100
        #resultados
            print(f"Total de fotos: {total_fotos}")
            print(f"Fotos com {class_name}: {fotos_com_classe}")
            print(f"Total de objetos encontrados: {total_encontrado}")
            print(f"Porcentagem: {porcentagem} %")

        elif option == 7:
            print("Você escolheu gráfico de barras")

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
