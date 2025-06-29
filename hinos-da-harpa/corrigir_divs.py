import os
import re
import shutil

# Caminho da pasta com os arquivos HTML
pasta = './hinos-da-harpa'
backup_pasta = './backup-hinos'

# Cria a pasta de backup se não existir
os.makedirs(backup_pasta, exist_ok=True)

# Novo conteúdo da div #controls
novo_controls = '''<div id="controls">
  <div id="muda-cor" class="control-button">mudar fundo</div>
  <div id="scroll-down" class="control-button">+</div>
  <div id="scroll-toggle" class="control-button">Play</div>
  <div id="scroll-reset" class="control-button">Reset</div>
  <div id="transpose-up" class="control-button">Transpose +</div>
  <div id="transpose-down" class="control-button">Transpose -</div>
  <div id="font-size-up" class="control-button">A+</div>
  <div id="font-size-down" class="control-button">A-</div>
</div>'''

# Percorre todos os arquivos HTML
for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.html'):
        caminho_arquivo = os.path.join(pasta, nome_arquivo)
        caminho_backup = os.path.join(backup_pasta, nome_arquivo)

        # Faz backup do arquivo original
        shutil.copyfile(caminho_arquivo, caminho_backup)

        # Lê o conteúdo
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            html = f.read()

        # Remove a div vazia + os botões fora dela (até o próximo div ou tag)
        html_corrigido = re.sub(
            r'<div id="controls">\s*</div>\s*'
            r'(<div[^>]+class="control-button"[^>]*>.*?</div>\s*){1,}',
            novo_controls,
            html,
            flags=re.DOTALL
        )

        # Escreve de volta no arquivo original
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(html_corrigido)

        print(f'Corrigido e backup feito: {nome_arquivo}')

print("✅ Todos os arquivos foram corrigidos com sucesso.")
