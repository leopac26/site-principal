import os

caminho_dos_arquivos = 'D:/meus projetos de github/site-principal/hinos-da-harpa'

# HTML do botão
novo_botao = '    <div id="muda-cor" class="control-button">mudar fundo</div>\n'

# Código JavaScript
codigo_js = """
<script>
document.getElementById('muda-cor').addEventListener('click', () => {
    document.body.style.backgroundColor =
      document.body.style.backgroundColor === 'black' ? 'white' : 'black';
});
</script>
"""

for nome_arquivo in os.listdir(caminho_dos_arquivos):
    if nome_arquivo.endswith('.html'):
        caminho_completo = os.path.join(caminho_dos_arquivos, nome_arquivo)

        with open(caminho_completo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        print(f'Alterando arquivo: {nome_arquivo}')

        if 'id="muda-cor"' in conteudo:
            print(f'Botão já existe no arquivo: {nome_arquivo}')
            continue  # já tem o botão e provavelmente o script

        # Insere o botão dentro da div de controls
        pos_controls = conteudo.find('<div id="controls">')
        if pos_controls != -1:
            fechamento_div = conteudo.find('</div>', pos_controls)
            if fechamento_div != -1:
                conteudo = (
                    conteudo[:fechamento_div] +
                    novo_botao +
                    conteudo[fechamento_div:]
                )

        # Insere o JS antes do </body>
        if '</body>' in conteudo:
            conteudo = conteudo.replace('</body>', codigo_js + '\n</body>')

        with open(caminho_completo, 'w', encoding='utf-8') as f:
            f.write(conteudo)

        print(f'Arquivo {nome_arquivo} modificado com sucesso!')

print("✅ Botão e JavaScript adicionados a todos os arquivos HTML.")
