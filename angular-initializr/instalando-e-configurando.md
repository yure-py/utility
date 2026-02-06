# 🚀 Guia: Automação de Arquitetura Angular (ng-init)

Este guia ensina como hospedar e configurar o seu script Python de arquitetura para ser acessado globalmente no terminal Windows (Git Bash).

---

## 1. Hospedando no GitHub Gist

O Gist funciona como um repositório de arquivo único, ideal para scripts de utilidade.

1.  Acesse [gist.github.com](https://gist.github.com).
2.  No campo **Filename**, digite: `AngularInitializr.py`.
3.  No corpo do texto, cole o código Python finalizado.
4.  Clique em **Create public gist** (ou *secret*, se preferir).
5.  No canto superior direito do arquivo, clique no botão **Raw**.
6.  **Copie a URL da barra de endereços**. Ela deve ser parecida com esta:
    `https://gist.githubusercontent.com/seu-usuario/id-do-gist/raw/AngularInitializr.py`

---

## 2. Configurando o Alias (Atalho)

Para evitar erros de entrada de dados (`EOFError`), configuramos o terminal para baixar o script em um arquivo temporário antes de executá-lo.

1.  Abra o **Git Bash**.
2.  Abra seu arquivo de perfil:
    ```bash
    nano ~/.bashrc
    ```
3.  Adicione a seguinte linha ao final do arquivo (substitua a URL pela sua):
    ```bash
    alias ng-init='curl -s "SUA_URL_AQUI" > /tmp/ng_init.py && python /tmp/ng_init.py'
    ```
4.  Salve e saia (`Ctrl+O`, `Enter`, `Ctrl+X`).
5.  Atualize o terminal atual:
    ```bash
    source ~/.bashrc
    ```

---

## 3. Como Utilizar

Com o alias configurado, o processo de criação de um novo projeto fica muito mais rápido:

1.  Crie o projeto: `ng new nome-do-projeto`.
2.  Entre na pasta: `cd nome-do-projeto`.
3.  Rode o comando: `ng-init`.
4.  **No prompt do script**:
    * **Caminho**: Basta digitar `.` (ponto) e dar Enter, já que você está dentro da pasta.
    * **Feature**: Digite o nome da feature (ex: `catalog-manga`).

[Image of Angular feature-based modular architecture]

---

## 4. Possíveis Problemas e Soluções

### ❌ Erro: `EOFError: EOF when reading a line`
**Causa:** O Python tentou ler o comando `input()` diretamente do fluxo de dados do `curl` (stdin), o que não é permitido em scripts interativos.

**Passo a Passo da Solução:**
1. Verifique se o seu `alias` está salvando o arquivo em um local temporário antes de executar.
2. O comando no seu `~/.bashrc` deve obrigatoriamente seguir este formato:
   `curl -s "URL" > /tmp/script.py && python /tmp/script.py`
3. O símbolo `>` redireciona o código para o disco, liberando o terminal para sua digitação.

---

### ❌ Erro: `python: command not found`
**Causa:** O executável do Python não está configurado nas variáveis de ambiente (PATH) do seu Windows.

**Passo a Passo da Solução:**
1. No menu iniciar, digite "Variáveis de Ambiente" e abra "Editar as variáveis de ambiente do sistema".
2. Clique em **Variáveis de Ambiente** > Na lista "Variáveis do Sistema", selecione **Path** e clique em **Editar**.
3. Verifique se o caminho da instalação do Python (ex: `C:\Python312`) está lá.
4. Caso não esteja, reinstale o Python e lembre-se de marcar a caixa: **"Add Python to PATH"** na primeira tela do instalador.

---

## 5. Mantendo o Alias Persistente no Windows

Se o comando `ng-init` não funcionar ao abrir um novo terminal ou logo após a configuração, é porque o Git Bash não leu as atualizações. Siga este passo a passo para garantir a persistência e ativação imediata.

### Passo a Passo da Configuração:

1.  **Adicionar o Alias ao .bashrc**:
    Execute este comando para gravar o alias no final do seu arquivo de configuração (substitua a URL pela sua do Gist):
    
    ```bash
    echo "alias ng-init='curl -s \"SUA_URL_RAW_AQUI\" > /tmp/ng_init.py && python /tmp/ng_init.py'" >> ~/.bashrc
    ```

2.  **Vincular o .bashrc ao .bash_profile**:
    No Windows, o Git Bash inicia procurando o arquivo `.bash_profile`. Precisamos dizer a ele para ler também o seu `.bashrc`. Rode este comando:
    
    ```bash
    echo "[[ -f ~/.bashrc ]] && . ~/.bashrc" >> ~/.bash_profile
    ```

3.  **Conferir se tudo está certo**:
    Abra o arquivo para confirmar que a linha foi gravada corretamente:
    ```bash
    nano ~/.bashrc
    ```
    *Se estiver tudo certo, saia com `Ctrl+X`.*

4.  **Ativar as alterações (Passo Final)**:
    O Bash não recarrega as configurações automaticamente. Para que o comando funcione **agora mesmo**, nesta janela, execute:
    
    ```bash
    source ~/.bashrc
    ```

5.  **Testar**:
    Agora o comando deve funcionar perfeitamente:
    ```bash
    ng-init
    ```

### Por que isso é necessário?



O comando `source` força o terminal a reler o arquivo de configuração imediatamente. Sem ele, você teria que fechar todas as janelas do Git Bash e abrir novamente para que as mudanças fizessem efeito.

---
