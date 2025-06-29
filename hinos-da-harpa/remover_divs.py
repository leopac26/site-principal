import os
import re

# Caminho da pasta
pasta = r'D:\meus projetos de github\site-principal\hinos-da-harpa'

# Lista dos IDs dos botões
ids_botoes = [
    "scroll-up", "scroll-down", "scroll-toggle", "scroll-reset",
    "transpose-up", "transpose-down", "font-size-up", "font-size-down", "muda-cor"
]

# Regex que captura todos os botões por ID
botoes_regex = re.compile(
    r'\s*<div id="(' + '|'.join(ids_botoes) + r')" class="control-button">.*?</div>',
    re.IGNORECASE
)

# Regex para capturar o bloco completo do #controls
controls_regex = re.compile(r'<div id="controls">.*?</div>', re.DOTALL | re.IGNORECASE)

for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.html'):
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

        # Encontra o bloco do #controls
        match = controls_regex.search(conteudo)
        if not match:
            print(f'[!] Bloco #controls não encontrado em: {nome_arquivo}')
            continue

        bloco_controls = match.group(0)
        pos_fim_controls = match.end()

        # Divide o conteúdo: antes e depois do bloco controls
        antes = conteudo[:pos_fim_controls]
        depois = conteudo[pos_fim_controls:]

        # Remove todos os botões duplicados que aparecem depois do #controls
        depois_sem_duplicados = botoes_regex.sub('', depois)

        # Junta tudo de volta
        conteudo_corrigido = antes + depois_sem_duplicados

        # Salva o arquivo
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo_corrigido)

        print(f'[✔] Duplicados removidos de: {nome_arquivo}')
