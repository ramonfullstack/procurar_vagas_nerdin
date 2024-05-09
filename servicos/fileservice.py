import os
import shutil


def mover_arquivo(origem, destino):
    print(f'Tentando mover o arquivo de {origem} para {destino}')
    
    try:
        # Move o arquivo da origem para o destino
        shutil.move(origem, destino)
        print(f'O arquivo foi movido de "{origem}" para "{destino}" com sucesso.')
    except FileNotFoundError:
        print(f'O arquivo "{origem}" não foi encontrado.')
    except PermissionError:
        print(f'Não foi possível mover o arquivo. Verifique as permissões.')

def limpar_arquivos_da_pasta(diretorioExcluir):
    arquivos = os.listdir(diretorioExcluir)
    print(arquivos)
    for arquivoExcluir in arquivos:
        caminho_completo = os.path.join(diretorioExcluir, arquivoExcluir)
        print(f'Arquivo excluir: {caminho_completo}')
        # Verifica se é um arquivo (não é um diretório)
        if os.path.isfile(caminho_completo):
            os.remove(caminho_completo)

def listar_arquivos_e_verificar_extensao(caminho_da_pasta, extensao_alvo):
    arquivos_encontrados = []
    caminho_alvo_arquivos = ''

    # Lista todos os arquivos no diretório
    arquivos = os.listdir(caminho_da_pasta)
    print(f'lista o caminho da pasta {caminho_da_pasta}')
    
     # Cria a pasta relacionada à extensão se ela não existir
    caminho_alvo_arquivos = os.path.join(caminho_da_pasta, extensao_alvo.lstrip('.') )
    if not os.path.exists(caminho_alvo_arquivos):
        os.makedirs(caminho_alvo_arquivos)

    # Itera sobre cada arquivo na lista
    for arquivo in arquivos:
        # Junta o caminho completo do arquivo
        caminho_completo = os.path.join(caminho_da_pasta, arquivo)

        # Verifica se é um arquivo (não é um diretório)
        if os.path.isfile(caminho_completo):
            # Obtém a extensão do arquivo
            _, extensao = os.path.splitext(arquivo)
            
            # Converte a extensão para minúsculas para tornar a comparação insensível a maiúsculas e minúsculas
            extensao = extensao.lower()

            # Verifica se a extensão corresponde à extensão alvo
            if extensao == extensao_alvo.lower():
                arquivos_encontrados.append(arquivo)
                
    print(f'Origem: {caminho_da_pasta} Destino: {caminho_alvo_arquivos}')        
    # Move cada arquivo encontrado para o diretório de destino
    for arquivo2 in arquivos_encontrados:
        print(f'Trying mover o arquivo de {caminho_da_pasta} para {caminho_alvo_arquivos}')
        origem = os.path.join(caminho_da_pasta, arquivo2)
        destino = os.path.join(caminho_alvo_arquivos, arquivo2)
        shutil.copyfile(origem, destino)
        
def obter_extensoes_da_pasta(caminho_da_pasta):
    extensoes = set()

    # Lista todos os arquivos no diretório
    arquivos = os.listdir(caminho_da_pasta)
    print(f'Arquivos: {arquivos}')
    
    # Itera sobre cada arquivo na lista
    for arquivo in arquivos:
        # Junta o caminho completo do arquivo
        caminho_completo = os.path.join(caminho_da_pasta, arquivo)

        # Verifica se é um arquivo (não é um diretório)
        if os.path.isfile(caminho_completo):
            # Obtém a extensão do arquivo
            _, extensao = os.path.splitext(arquivo)

            # Adiciona a extensão à lista
            extensoes.add(extensao.lower())  # Convertendo para minúsculas para evitar duplicatas

    return extensoes