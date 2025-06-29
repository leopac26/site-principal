import os
import re

# Caminho da pasta onde estão os arquivos HTML
pasta_alvo = 'D:/meus projetos de github/site-principal/hinos-da-harpa'  # Ajuste conforme seu caminho

# Novo conteúdo da div #controls com os botões
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

# Expressão regular para localizar e substituir a div #controls com os botões corretos
regex_controls = re.compile(r'<div id="controls">.*?</div>', re.DOTALL)

# Percorre os arquivos da pasta
for nome_arquivo in os.listdir(pasta_alvo):
    if nome_arquivo.endswith('.html'):
        caminho_arquivo = os.path.join(pasta_alvo, nome_arquivo)

        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        # Substitui o conteúdo da div #controls pela nova versão com os botões
        novo_conteudo = re.sub(regex_controls, novo_controls, conteudo)

        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(novo_conteudo)

        print(f'✔ Corrigido: {nome_arquivo}')

print('✅ Todos os arquivos foram corrigidos.')
