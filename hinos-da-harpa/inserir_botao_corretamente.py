import os
import re

# Caminho da pasta onde estão os arquivos HTML
caminho_dos_arquivos = '.'

# Botão que deve ser adicionado dentro da div de controls
novo_botao = '    <div id="muda-cor" class="control-button">mudar fundo</div>\n'

# Regex para encontrar div #controls
padrao_controls = re.compile(r'(<div id="controls">)(.*?)(</div>)', re.DOTALL)

# Botão exato a ser removido de onde não deveria estar
botao_livre = '<div id="muda-cor" class="control-button">mudar fundo</div>'

for nome_arquivo in os.listdir(caminho_dos_arquivos):
    if nome_arquivo.endswith('.html'):
        caminho_completo = os.path.join(caminho_dos_arquivos, nome_arquivo)

        with open(caminho_completo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        alterado = False

        # Remove botões soltos fora do controls
        if botao_livre in conteudo:
            conteudo = conteudo.replace(botao_livre, '')
            alterado = True

        # Encontrar e atualizar conteúdo dentro da div de controls
        match = padrao_controls.search(conteudo)
        if match:
            inicio, meio, fim = match.groups()
            if 'id="muda-cor"' not in meio:
                # Adiciona o botão no final do bloco controls
                meio += novo_botao
                novo_html = f'{inicio}{meio}{fim}'
                conteudo = padrao_controls.sub(novo_html, conteudo)
                alterado = True

        if alterado:
            with open(caminho_completo, 'w', encoding='utf-8') as f:
                f.write(conteudo)
            print(f"✅ Botão corrigido em: {nome_arquivo}")
        else:
            print(f"ℹ️ Sem mudanças: {nome_arquivo}")
