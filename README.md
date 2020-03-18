# Desafio da Nasa

[Sobre o desafio](#DESCRIÇÃO-DO-DESAFIO)<br>
[Especificações técnicas](#ESPECIFICAÇÕES-TÉCNICAS)

## Descrição do desafio

Você é um membro da tripulação de uma nave espacial, que programou um encontro, junto com outra nave na superfície luminosa da Lua… entretanto dificuldades mecânicas obrigaram sua nave a uma descida forçada, num ponto distante a 100 Km do planejado encontro. A maior parte do equipamento, na descida forçada ficou avariada e já que sua sobrevivência depende de encontrar o ponto de encontro a 100 Km, é preciso escolher, dos itens abaixo, os mais essenciais, para este percurso.

Abaixo, há uma lista de 15 itens de coisas que não ficaram estragadas na descida. Seu trabalho será de numerar esses itens em termos de sua importância para alcançar o ponto de encontro. Coloque o número 1 para o item mais importante, o número 2 para o segundo, até o número 15 para o item menos importante.

Ao final, a sua ordenação será comparada a ordenação de um especialista. A diferença entre a sua ordenação, a ordenação de sua equipe e a do especialista irá definir a sua pontuação final.

. caixa de fósforo<br>
. alimento concentrado<br>
. corda de nylon<br>
. seda de para-quedas<br>
. um aquecedor portátil<br>
. duas pistolas de calibre 45<br>
. uma caixa de leite em pó<br>
. um mapa estelar( da constelação. lunar)<br>
. uma balsa salva-vidas<br>
. dois tanques de oxigênio 100 libras cada<br>
. uma bússola<br>
. cinco galões de água<br>
. sinais luminosos<br>
. um estojo de primeiro socorros c/ agulhas de injeção<br>
. um receptor e transmissor FM, movido a força solar<br>

## Fórmula da pontuação

A fórmula para o cálculo da pontuação é a seguinte:

<img src="http://latex.codecogs.com/svg.latex?%5Cfrac%7B%28%20%5CDelta%20individual%20-%20%5CDelta%20grupo%20*%20100%20%29%7D%7B112%7D" />

<img src="http://latex.codecogs.com/svg.latex?%5CDelta%20individual" />:  diferença entre as respostas individuais com a resposta do especialista.<br>
<img src="http://latex.codecogs.com/svg.latex?%5CDelta%20grupo" />:  diferença entre as respostas do grupo com a resposta do especialista.

## ESPECIFICAÇÕES TÉCNICAS

### Stack utilizada

**Python**
- Lóginas de interface para persistência de dados

**Python Flask**
- Conteúdo dinâmico nas páginas html da aplicação
- Configuração de rotas das páginas da aplicação e das APIs

**Html, Css, Javascript**
- Front-end da aplicação

**Postgres**
- Persistência dos dados 

### API

Para realizar o calculo da pontuação do desafio via API, é necessário realizar os seguintes passos:

1 - Gerar um id de sessão

2 - Inserir os dados de respostas individuais, passando o id de sessão no payload

3 - Inserir os dados de respostas do grupo, passando o id de sessão no payload

4 - Buscar a pontuação, a partir do id de sessão

A seguir estão descritos os métodos para as chamadas de API desses passos.

#### Get Session

Para gerar um ID de sessão, que será utilizado para junção dos dados individuais e de grupo para cálcular a pontuação do desafio.

Método: GET

Exemplo de uso:
```curl
curl localhost:5000/api/get-session
```

Exemplo de resposta:
```
c2689b54-cc76-493e-99ba-f96f800155d9
```
O exemplo acima é o id de sessão (formato uuid v4) que deve ser usado na requisições a seguir.


#### Post single

Para realizar a inserção dos dados da ordenação de itens do desafio individual.

Método: POST
Parâmetros necessários:
- Id de sessão: (string) id no formato uuid v4 gerado através da api [get-session](#GET-SESSION)
- id do item: (int) id do item a ser ordenado no teste invididual
- ordenação: (int) ordem de prioridade do item a ser lançado (de 1 a n, sendo n a quantidade total de itens cadastrados no banco de dados)

Exemplo de uso:
```curl
curl -X POST -d '{ 
        "session": "{{id da sessão}}", 
        "orders":{ 
          "{{id do item}}": "{{ordenacao do item}}", 
          "{{id do item2}}": "{{ordenacao do item2}}"
        }
      }' 
  -H 'Content-Type: application/json' localhost:5000/api/post-single
```
*Nota:*

*- substitua os valores entre {{ }} com os valores correspondentes*

*- no exemplo acima, foi demonstrada uma requisição de apenas dois itens, porém é possível inserir n itens dentro do atributo `orders` do payload*


Resposta:
- 200 em caso de sucesso.
- 4xx em caso de falha. A mensagem de erro é descrita do parâmetro `message` do json de resposta.


#### Post team

Para realizar a inserção dos dados da ordenação de itens do desafio de grupo.

Método: POST
Parâmetros necessários:
- Id de sessão: (string) id no formato uuid v4 gerado através da api [get-session](#GET-SESSION)
- id do item: (int) id do item a ser ordenado no teste invididual
- ordenação: (int) ordem de prioridade do item a ser lançado (de 1 a n, sendo n a quantidade total de itens cadastrados no banco de dados)

Exemplo de uso:
```curl
curl -X POST -d '{ 
        "session": "{{id da sessão}}", 
        "orders":{ 
          "{{id do item}}": "{{ordenacao do item}}", 
          "{{id do item2}}": "{{ordenacao do item2}}"
        }
      }' 
  -H 'Content-Type: application/json' localhost:5000/api/post-team
```
*Nota:*

*- substitua os valores entre {{ }} com os valores correspondentes*

*- no exemplo acima, foi demonstrada uma requisição de apenas dois itens, porém é possível inserir n itens dentro do atributo `orders` do payload*

Resposta:
- 200 em caso de sucesso.
- 4xx em caso de falha. A mensagem de erro é descrita do parâmetro `message` do json de resposta.


#### Score

Para realizar o cálculo da pontuação do desafio.

Método: GET
Parâmetros necessários:
- Id de sessão: (string) id no formato uuid v4 gerado através da api [get-session](#GET-SESSION)

Exemplo de uso:
```curl
curl -X GET -d '{ 
      "session": "{{id de sessão}}" 
      }' 
-H 'Content-Type: application/json' localhost:5000/api/score
```
*Nota:*

*- substitua os valores entre {{ }} com os valores correspondentes*

Exemplo de resposta:
```json
{
	"code": 200
	"message": "success"
	"response": {
		"score": -52.785714285714285 
	}
}

```
