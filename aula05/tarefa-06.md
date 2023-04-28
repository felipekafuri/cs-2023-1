1. O nome do branch padrão do Git é `master` (para versões mais antigas do Git) ou `main` (para versões mais recentes e serviços de hospedagem como o GitHub).

2. O comando `git branch nome` cria um novo branch chamado `nome`.

3. Para criar um branch a partir de um commit específico, use o comando `git checkout -b nome_do_novo_branch commit_hash`.

4. O comando `git checkout -b bugfix/234` cria e muda para um novo branch chamado `bugfix/234`.

5. Para alternar para o branch chamado `experimento2`, use o comando `git checkout experimento2`.

6. No repositório com dois branches, `b1` e `b2`, onde `b1` é o corrente, o comando `git branch` mostrará a lista de branches com um asterisco ao lado do branch corrente.

7. O comando `git checkout -b nome` cria um novo branch chamado `nome` e muda para ele.

8. A função do comando `git branch -d teste` é excluir o branch chamado `teste`.

9. Sequência de comandos para simular um caso simples de criação e uso seguido de merge:

   a. Criação de um ou mais branches:
      ```
      git checkout -b experimento
      ```
   b. Chaveamento para pelo menos dois branches:
      ```
      git checkout master
      git checkout experimento
      ```
   c. Merge:
      ```
      git checkout master
      git merge experimento
      ```
