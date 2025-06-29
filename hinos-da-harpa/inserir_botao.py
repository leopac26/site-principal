import os

# Caminho onde estão seus arquivos HTML
caminho_dos_arquivos = './'  # Pode ajustar esse caminho conforme necessário

# Botão que você quer adicionar
novo_botao = '    <div id="muda-cor" class="control-button">mudar fundo</div>\n'

for nome_arquivo in os.listdir(caminho_dos_arquivos):
    if nome_arquivo.endswith('.html'):
        caminho_completo = os.path.join(caminho_dos_arquivos, nome_arquivo)

        with open(caminho_completo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        # Verifica se o botão já existe
        if 'id="muda-cor"' in conteudo:
            continue  # já foi adicionado

        # Adiciona antes do fechamento da div de controles
        if '<div id="controls">' in conteudo:
            novo_conteudo = conteudo.replace(
                '</div>', novo_botao + '</div>', 1  # só na primeira ocorrência
            )

            with open(caminho_completo, 'w', encoding='utf-8') as f:
                f.write(novo_conteudo)

print("✅ Botão 'mudar fundo' adicionado a todos os arquivos HTML.")
