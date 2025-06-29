import os
import re

# Caminho da pasta onde estão os arquivos HTML
pasta_alvo = './hinos-da-harpa'  # ajuste esse caminho conforme sua estrutura

# Novo conteúdo da div #controls
novo_controls = '''
<div id="controls">
  <div id="muda-cor" class="control-button">mudar fundo</div>
  <div id="scroll-down" class="control-button">+</div>
  <div id="scroll-toggle" class="control-button">Play</div>
  <div id="scroll-reset" class="control-button">Reset</div>
  <div id="transpose-up" class="control-button">Transpose +</div>
  <div id="transpose-down" class="control-button">Transpose -</div>
  <div id="font-size-up" class="control-button">A+</div>
  <div id="font-size-down" class="control-button">A-</div>
</div>
'''

# Expressão regular para encontrar a div controls e os botões fora dela
regex_controls = re.compile(
    r'<div id="controls">.*?</div>\s*'
    r'(?:\s*<div[^>]*class="control-button"[^>]*>.*?</div>\s*)*',
    re.DOTALL
)

# Processar todos os arquivos HTML na pasta
for nome_arquivo in os.listdir(pasta_alvo):
    if nome_arquivo.endswith('.html'):
        caminho_arquivo = os.path.join(pasta_alvo, nome_arquivo)

        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        # Substitui a div controls corrompida pelo novo conteúdo
        novo_conteudo = re.sub(regex_controls, novo_controls, conteudo)

        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(novo_conteudo)

        print(f'Corrigido: {nome_arquivo}')

print('Todos os arquivos foram atualizados com sucesso.')
