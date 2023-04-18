# API REST

REST (Representational State Transfer) é um estilo de arquitetura de software que descreve como acessar e manipular funções da Web usando protocolos HTTP. Uma API RESTful é uma interface de programação de aplicativo que usa o estilo REST e permite que os desenvolvedores interajam com serviços da web.

# Conceitos

- Recurso: é a abstração de um objeto ou uma coleção de objetos que é armazenado no servidor. Cada recurso é identificado por um URI (Uniform Resource Identifier).
- Métodos HTTP: são as ações que podem ser realizadas sobre um recurso. Os principais métodos são: GET, POST, PUT e DELETE.
- Representação: é a forma como um recurso é apresentado na API. Geralmente, as representações são em formato JSON ou XML.
- URI: é a identificação única do recurso na API. É composto por um nome de domínio, um caminho e um identificador do recurso.
- Cliente-servidor: é o princípio da separação entre as responsabilidades do cliente e do servidor. O servidor fornece recursos e o cliente solicita e manipula esses recursos.

# Características

- Stateless: a API não mantém o estado entre as solicitações do cliente. Isso significa que cada solicitação do cliente deve conter todas as informações necessárias para atender à solicitação.
- Cacheável: as respostas da API podem ser armazenadas em cache pelo cliente ou corretor. Isso pode melhorar a eficiência e o desempenho da API.
- Interface uniforme: Uma API deve ter uma interface uniforme que defina como os recursos são acessados ​​e manipulados. Isso simplifica o desenvolvimento de clientes e servidores independentes.
- Sistema em camadas: A API pode ser composta por uma hierarquia de camadas intermediárias, como balanceadores de carga ou caches, que podem melhorar a escalabilidade e a segurança da API.
- Code on Demand: opcionalmente, a API pode fornecer código executável como JavaScript ou applets Java,
executado no cliente. Isso pode melhorar a funcionalidade e a interatividade da API.

As APIs RESTful são amplamente usadas na construção de aplicativos da Web e móveis. Eles fornecem uma maneira simples e eficiente de interagir com serviços da Web de maneira padronizada e escalável. Além disso, a abordagem RESTful é independente de linguagem, o que significa que pode ser implementada em qualquer linguagem de programação que suporte o protocolo HTTP.