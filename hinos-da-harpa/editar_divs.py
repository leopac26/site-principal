import os
import re

# Caminho da pasta
pasta = r'D:\meus projetos de github\site-principal\hinos-da-harpa'

# Bloco de controles correto
bloco_controls = '''
<div id="controls">
  <div id="scroll-up" class="control-button">-</div>
  <div id="scroll-down" class="control-button">+</div>
  <div id="scroll-toggle" class="control-button">Play</div>
  <div id="scroll-reset" class="control-button">Reset</div>
  <div id="transpose-up" class="control-button">Transpose +</div>
  <div id="transpose-down" class="control-button">Transpose -</div>
  <div id="font-size-up" class="control-button">A+</div>
  <div id="font-size-down" class="control-button">A-</div>
  <div id="muda-cor" class="control-button">mudar fundo</div>
</div>
'''.strip()

# Regex para remover todos os controles anteriores
controls_regex = re.compile(r'<div id="controls">.*?</div>', re.DOTALL | re.IGNORECASE)

# Também remove divs individuais duplicadas
botoes_regex = re.compile(r'\s*<div id="(scroll-up|scroll-down|scroll-toggle|scroll-reset|transpose-up|transpose-down|font-size-up|font-size-down|muda-cor)" class="control-button">.*?</div>', re.IGNORECASE)

for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.html'):
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        # Remove o bloco de controles antigo e qualquer botão duplicado fora do bloco
        conteudo = controls_regex.sub('', conteudo)
        conteudo = botoes_regex.sub('', conteudo)

        # Insere o bloco novo antes da tag </body>
        if '</body>' in conteudo:
            conteudo = conteudo.replace('</body>', bloco_controls + '\n</body>')
        else:
            # Se não tiver </body>, apenas adiciona no final
            conteudo += '\n' + bloco_controls

        # Salva de volta
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo)

        print(f'[✔] Corrigido e inserido bloco único em: {nome_arquivo}')
