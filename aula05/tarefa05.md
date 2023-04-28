1. `git --version`

2. Efeitos dos comandos:
   a. `git help`: Mostra uma lista de comandos Git mais comuns e suas descrições.
   b. `git help checkout`: Mostra informações detalhadas sobre o comando `git checkout`.
   c. `git help merge`: Mostra informações detalhadas sobre o comando `git merge`.
   d. `git init`: Inicializa um novo repositório Git local.
   e. `git add --all`: Adiciona todos os arquivos modificados e não rastreados ao próximo commit.
   f. `git add -u`: Adiciona apenas arquivos modificados e excluídos (não novos) ao próximo commit.
   g. `git config -l`: Lista todas as configurações do Git.
   h. `git mv a.txt b.txt`: Renomeia o arquivo a.txt para b.txt e registra a mudança para o próximo commit.
   i. `git reset --hard`: Descarta todas as mudanças feitas desde o último commit.
   j. `git log -27`: Mostra os últimos 27 commits no histórico do repositório.

3. `git add` e `git commit`

4. `git status`

5. `git ls-files --others`

6. `git commit -m "mensagem do commit"`

7. `git checkout -- teste.txt`

8. Crie um arquivo `.gitignore` no diretório raiz do repositório e adicione o nome do diretório (ou padrão) que deseja ignorar.

9. Se o repositório local for removido acidentalmente, você perderá todas as mudanças locais não sincronizadas com o repositório remoto. Se houver um repositório remoto, você pode cloná-lo novamente.

10. `git clone <url_do_repositório_remoto>`

11. `git log --oneline`

12. `~/.gitconfig` ou `.git/config` (configuração específica do repositório)

13. `git init`

14. `.git`

15. `git add -u`

16. SHA1 é um algoritmo criptográfico de hash que gera um valor de hash de 40 caracteres. No Git, é usado para identificar de forma única commits, objetos e referências.

17. `HEAD`

18. Não, o comando `git add -u` adiciona apenas arquivos modificados e excluídos (não novos) ao próximo commit.

19. O primeiro comando desfaz o último commit, mantendo as mudanças nos arquivos. O segundo comando descarta todas as mudanças feitas desde o último commit.

20. `git clean -f -d`

21. `.gitignore`

22. Adicione a seguinte linha ao arquivo `.gitignore`: `*.class`

23. `git clone https://github.com/jquery/jquery.git`

24. `git shortlog -sne` mostra uma lista de autores com o número de commits e informações de email.

25. `git remote -v` mostra uma lista de repositórios remotos e suas URLs.

26. `git tag`

27. `git tag -l "2.0*"`

28. Cria uma tag anotada chamada "3.4-gold" com a mensagem "minha versão ouro".

29. `git show 3.4-gold` mostra informações detal
