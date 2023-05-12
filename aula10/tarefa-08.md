
# Revisão de Código - Classe Cliente
## Não Conformidades
1. Tratamento de Erros
Nos métodos setSexo, setEstadoCivil, setNacionalidade, setCpf e setPassaporte, se o argumento fornecido não passar na validação, a propriedade correspondente não é atualizada, mas nenhuma ação adicional é tomada. Pode ser mais útil lançar uma exceção ou retornar um erro, para que o chamador possa saber que a operação não foi bem-sucedida.

2. Tratamento de Datas
O método setDataNascimento aceita uma string como argumento, a qual é então convertida para um objeto Date. Isso pode levar a problemas se a string não estiver em um formato esperado. Além disso, não há validação da data de nascimento, portanto, pode ser definida como uma data futura, o que seria inválido.

3. Implementação de Construtor
O construtor personalizado da classe Cliente aceita todos os parâmetros de uma vez, e isso pode tornar difícil a criação de novas instâncias de Cliente, especialmente se apenas alguns atributos forem conhecidos. Uma abordagem alternativa poderia ser usar um padrão de construção, como o padrão Builder.

4. Falta de Documentação
Não há comentários ou documentação no código, o que pode dificultar a compreensão de outras pessoas (ou até mesmo você, no futuro) sobre como a classe deve ser usada ou como funciona internamente.

5. Tratamento de Dados Sensíveis
O CPF e o passaporte são dados sensíveis e não estão sendo tratados de forma adequada. É importante garantir que esses dados sejam armazenados e manipulados de forma segura.

# Revisão de Código - Classe PremioSeguro
## Não Conformidades

1. Tratamento de Erros
Na função obtemPercentualDesconto, as validações são realizadas, mas não há tratamento para cenários em que os dados não passam na validação. Da mesma forma que na classe Cliente, pode ser útil lançar uma exceção ou retornar um erro.

2. Design do Método
O método obtemPercentualDesconto não apenas obtém o percentual de desconto, mas também o define. Isso pode ser confuso, já que o nome do método sugere que ele apenas obtém um valor. Seria mais apropriado renomear este método para calculaPercentualDesconto ou algo similar, para refletir melhor o que ele realmente faz.

3. Validação de Dados
Embora haja validação dos dados do cliente, não há validação do valorSeguro. Como este valor é usado para calcular o valorSeguroComDesconto, pode ser útil garantir que ele seja válido antes de usá-lo.

4. Falta de Documentação
Novamente, falta documentação ou comentários no código. Isso pode dificultar a compreensão de sua funcionalidade e uso.

5. Tratamento de Dados Sensíveis
O CPF e o passaporte, que são dados sensíveis, são validados nesta classe, mas como mencionado na revisão da classe Cliente, é importante garantir que esses dados sejam armazenados e manipulados de forma segura.


# Revisão de Código - Classe CpfValidator
## Não Conformidades

1. Tratamento de Erros
Na função isCPF, é lançada uma CpfInvalidoException se o CPF for inválido. No entanto, o método retorna um valor booleano. Em geral, é melhor escolher uma estratégia de tratamento de erros e ser consistente. Nesse caso, é mais apropriado retornar false para CPFs inválidos em vez de lançar uma exceção, já que o chamador do método provavelmente verificará o valor de retorno de qualquer maneira.

2. Design do Método
A função isCPF poderia ser dividida em várias funções menores, cada uma responsável por uma parte da validação do CPF. Isso tornaria o código mais legível e fácil de manter. Por exemplo, poderia haver uma função validaDigitos, validaQuantidade e validaCalculo para lidar com as diferentes partes da validação.

3. Uso Eficiente de Recursos
A verificação de todos os números iguais no CPF poderia ser feita de forma mais eficiente. Atualmente, ela verifica explicitamente se cada número é igual ao anterior, o que é redundante e consome recursos desnecessários. Uma abordagem alternativa poderia ser usar um loop para verificar se todos os números são iguais.

4. Falta de Documentação
Novamente, não há comentários ou documentação no código. Isso pode dificultar a compreensão de como a classe e seus métodos devem ser usados.


# Revisão de Código - Classe CpfValidatorRefactored
## Não Conformidades
1. Métodos de validação
Os métodos de validação validaQuantidadeMaiorOnze e existeNaoDigito estão retornando o parâmetro result, que é passado como false e nunca alterado. Portanto, esses métodos sempre retornarão false, independentemente do CPF passado. Ao invés disso, você poderia retornar a condição que você está verificando diretamente. Por exemplo:

```java
private static boolean validaQuantidadeMaiorOnze(String cpf) {
    return cpf.length() <= 11;
}
```
2. Variáveis não utilizadas
Os métodos calculaPrimeiroDigito e calculaSegundoDigito retornam os dígitos calculados, mas esses valores não são atribuídos a nenhuma variável quando os métodos são chamados na função isCPF. Você precisa atribuir esses valores às variáveis primeiroDigito e segundoDigito respectivamente.

```java
primeiroDigito = calculaPrimeiroDigito(numerosCpf);
segundoDigito = calculaSegundoDigito(numerosCpf);
```

3. Método validaIgualdade
O método validaIgualdade ainda está verificando explicitamente se cada número é igual ao anterior. Uma abordagem alternativa poderia ser usar um loop para verificar se todos os números são iguais. Além disso, como mencionado anteriormente, você poderia retornar a condição que você está verificando diretamente.

```java
private static boolean validaIgualdade(int[] numerosCpf){
    for (int i = 1; i < numerosCpf.length; i++) {
        if (numerosCpf[i] != numerosCpf[0]) {
            return false;
        }
    }
    return true;
}```

## Conformidades
A refatoração para separar as diferentes partes da validação do CPF em métodos diferentes melhorou a legibilidade do código.
A documentação adicionada nos métodos auxilia no entendimento do propósito de cada um.


# Revisão de Código - Classe DataUtils
## Não Conformidades

1. Tratamento de exceções
O método StringToDate usa um bloco try-catch para lidar com uma possível ParseException, mas tudo o que faz quando captura a exceção é chamar pe.getMessage(), que não faz nada com a mensagem. Seria mais apropriado reagir de uma maneira significativa à exceção, por exemplo, lançando uma exceção personalizada ou pelo menos registrando a mensagem de erro.

```java
try {
    data = new SimpleDateFormat("dd/MM/yyyy").parse(dateString);
} catch (ParseException pe){
    throw new DataInvalidaException("Data em formato inválido!", pe);
}
```

2. Código comentado
O método validaIdade contém uma linha de código comentada que parece ter sido usada para fins de depuração (System.out.printf). Deve-se evitar deixar código comentado no código final, pois isso pode confundir outros desenvolvedores.

3. Validação de data
O método validaData valida a data de uma maneira muito manual e não considera anos bissextos corretamente. Java já possui bibliotecas muito boas para manipulação de datas, como java.time, que devem ser usadas em vez de tentar implementar essa lógica manualmente. Além disso, o método validaData também deve validar o formato da data.

```java
public static boolean validaData(String dateString) {
    try {
        LocalDate.parse(dateString, DateTimeFormatter.ofPattern("dd/MM/yyyy"));
        return true;
    } catch (DateTimeParseException e) {
        throw new DataInvalidaException("Data em formato inválido!", e);
    }
}
```

## Conformidades
A classe fornece um conjunto útil de métodos para manipulação e validação de datas.
O uso de exceções personalizadas para indicar erros de validação melhora a semântica do código e torna mais fácil para os usuários da classe entenderem o que deu errado.


# Revisão de Código - Classe EstadoCivilValidator
## Não Conformidades

Não foram encontradas não conformidades na classe EstadoCivilValidator. O código é conciso, claro e faz a validação de acordo com uma lista pré-definida de estados civis válidos. Além disso, ele lança uma exceção personalizada adequada quando um estado civil inválido é encontrado, o que é uma prática recomendada.

## Conformidades
O código está bem organizado e é fácil de entender. Ele executa sua função de validação de maneira eficiente e clara.

O método validaEstadoCivil é declarado como static, o que faz sentido, pois a validação do estado civil é uma operação que não depende do estado de qualquer objeto EstadoCivilValidator.

A lista de estados civis válidos é codificada como uma lista imutável, o que é uma boa prática para garantir a integridade dos dados.

A exceção personalizada EstadoCivilInvalidoException é usada para indicar um estado civil inválido. Isso é uma boa prática porque torna o código mais fácil de entender e usar corretamente, pois os usuários da classe sabem que tipo de exceção esperar.

O uso do método contains da interface List para verificar se o estado civil está na lista de estados civis válidos é uma abordagem eficiente e fácil de entender para a validação.



# Revisão de Código - Classe NacionalidadeValidator

## Não Conformidades
A variável NacionalidadesValidas deve começar com uma letra minúscula, de acordo com as convenções de nomenclatura do Java. Isso melhora a legibilidade e a compreensão do código.
Conformidades
O código está bem organizado e é fácil de entender. Ele executa sua função de validação de maneira eficiente e clara.

O método validaNacionalidade é declarado como static, o que faz sentido, pois a validação da nacionalidade é uma operação que não depende do estado de qualquer objeto NacionalidadeValidator.

A lista de nacionalidades válidas é codificada como uma lista imutável, o que é uma boa prática para garantir a integridade dos dados.

A exceção personalizada NacionalidadeInvalidaException é usada para indicar uma nacionalidade inválida. Isso é uma boa prática porque torna o código mais fácil de entender e usar corretamente, pois os usuários da classe sabem que tipo de exceção esperar.

O uso do método contains da interface List para verificar se a nacionalidade está na lista de nacionalidades válidas é uma abordagem eficiente e fácil de entender para a validação.

Recomendação
Aqui está a versão corrigida do código:

```java
package org.util;

import org.excecoes.NacionalidadeInvalidaException;

import java.util.Arrays;
import java.util.List;

public class NacionalidadeValidator {
    public static Boolean validaNacionalidade(String nacionalidade){
        boolean result = false;
        List<String> nacionalidadesValidas = Arrays.asList("Brasileira","Estrangeira");
        if(nacionalidadesValidas.contains(nacionalidade))
            result = true;
        else
            throw new NacionalidadeInvalidaException("Nacionalidade Inválida!");
        return result;
    }
}
```