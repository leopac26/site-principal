import os

# Caminho da pasta com os arquivos HTML
caminho_dos_arquivos = '.'

# Botão a ser removido (texto exato)
codigo_botao = '<div id="muda-cor" class="control-button">mudar fundo</div>'

# Percorre todos os arquivos da pasta
for nome_arquivo in os.listdir(caminho_dos_arquivos):
    if nome_arquivo.endswith('.html'):
        caminho_completo = os.path.join(caminho_dos_arquivos, nome_arquivo)

        with open(caminho_completo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        # Remove o botão, se existir
        if codigo_botao in conteudo:
            conteudo = conteudo.replace(codigo_botao, '')

            with open(caminho_completo, 'w', encoding='utf-8') as f:
                f.write(conteudo)

            print(f'✅ Botão removido de: {nome_arquivo}')
        else:
            print(f'ℹ️ Botão não encontrado em: {nome_arquivo}')
