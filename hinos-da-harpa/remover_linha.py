import os

# Caminho da pasta onde estão os arquivos HTML
pasta = r'D:/meus projetos de github/site-principal/hinos-da-harpa'

# Frase ou trecho exato que você quer remover
trecho_para_remover = '<td><a href="../videos-youtube/videosyoutube.html"> videos</a></td>'

# Loop por todos os arquivos da pasta
for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.html'):
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.readlines()

        # Remover linhas que contêm exatamente o trecho
        novo_conteudo = [linha for linha in conteudo if trecho_para_remover not in linha]

        # Salvar o arquivo modificado
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.writelines(novo_conteudo)

        print(f'Removido do arquivo: {nome_arquivo}')
