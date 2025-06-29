import os

# Caminho onde estão seus arquivos HTML (ajuste se necessário)
caminho_dos_arquivos = './hinos-da-harpa'

# Botão que será adicionado
novo_botao = '    <div id="muda-cor" class="control-button">mudar fundo</div>\n'

for nome_arquivo in os.listdir(caminho_dos_arquivos):
    if nome_arquivo.endswith('.html'):
        caminho_completo = os.path.join(caminho_dos_arquivos, nome_arquivo)

        with open(caminho_completo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        # Verifica se o botão já existe
        if 'id="muda-cor"' in conteudo:
            continue

        # Procura a div #controls e adiciona o botão DENTRO dela (antes do </div>)
        if '<div id="controls">' in conteudo:
            inicio = conteudo.find('<div id="controls">')
            fechamento = conteudo.find('</div>', inicio)
            if fechamento != -1:
                novo_conteudo = (
                    conteudo[:fechamento]
                    + novo_botao
                    + conteudo[fechamento:]
                )
                with open(caminho_completo, 'w', encoding='utf-8') as f:
                    f.write(novo_conteudo)

print("✅ Botão 'mudar fundo' inserido dentro da div #controls.")
