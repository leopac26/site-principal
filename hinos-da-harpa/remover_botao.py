import os

# Caminho para os arquivos HTML
caminho_arquivo_html = "seu_arquivo.html"  # Altere para o caminho do seu arquivo HTML

# Função para corrigir o HTML removendo a div de fechamento extra
def corrigir_html():
    with open(caminho_arquivo_html, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    # Procurar a tag de fechamento </div> extra após o botão "muda-cor"
    pos_muda_cor = conteudo.find('<div id="muda-cor" class="control-button">mudar fundo</div>')
    if pos_muda_cor != -1:
        # Procurar onde começa a div de controle e onde ela termina
        pos_controls_inicio = conteudo.find('<div id="controls">')
        pos_controls_fim = conteudo.find('</div>', pos_controls_inicio)

        # Remover o fechamento extra da div após o botão
        conteudo = conteudo[:pos_controls_fim] + conteudo[pos_controls_fim + 6:]  # 6 é o comprimento de </div>

    # Salvar o conteúdo corrigido no arquivo
    with open(caminho_arquivo_html, 'w', encoding='utf-8') as file:
        file.write(conteudo)
    print(f"Arquivo '{caminho_arquivo_html}' corrigido com sucesso.")

# Executando a correção
corrigir_html()
