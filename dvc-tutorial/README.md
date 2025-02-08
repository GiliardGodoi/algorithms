# DVC Tutorial

[Data Version Control](https://dvc.org/doc) (DVC) é uma ferramenta inicialmente criada para gerenciar versões dos *datasets* em um projeto de Machine Learning.

## passo 0: instalar o `dvc`

A [página](https://dvc.org/doc/install) de instalação do dvc traz diversas formas que esse programa pode ser instalado.
Eu prefiro fazer da forma mais simples:
```bash
$ pip install dvc
```

Se você procurar, existe também uma extensão do `dvc` para o `VS Code`.

## 1º passo: iniciar o projeto

Digamos que desejamos criar um projeto em um diretório chamado `dvc-tutorial`.
Após criar a pasta, a primeira coisa a se fazer é iniciar um repositório `git`. 

O `dvc` e o `git` são duas ferramentas que andam juntas, e a primeira não sobrevive sem a segunda.

```bash
$ mkdir dvc-tutorial
$ cd dvc-tutorial
$ git init
$ dvc init
```

Alguns arquivos de configuração já são criados logo de cara, na estrutura de diretório. Eles são uma pasta `.dvc` e um arquivo `.dvcignore`.

Observe que esses arquivos e diretórios já estão adicionados à área de *stage* do `git`. Para verificar isso, execute o comando:
```bash
$ git status

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .dvc/.gitignore
        new file:   .dvc/config
        new file:   .dvcignore
```

Portanto, já podemos dar um *commit* nessas mudanças:
```
$ git commit -m 'Inicializando projeto DVC'
```

## 2º passo: rastrear o dataset

Na documentação oficial, é sugerido obter um *dataset* de exemplo através do comando `dvc get`. 

No nosso caso vamos apenas gerar um *dataset fake* com o seguinte comando:
```bash
$ python fake.py
```

Se executarmos o comando `dvc status` temos a seguinte mensagem:
```bash
$ dvc status
There are no data or pipelines tracked in this project yet.
See <https://dvc.org/doc/start> to get started!
```

Obviamente porque não começamos a rastrear o nosso *dataset*. 
Para tanto, basta executar o comando `dvc add <caminho-para-dataset>`, como no exemplo a seguir:

```bash
$ dvc add data/dirty_data.csv

To track the changes with git, run:
    git add 'data\dirty_data.csv.dvc' 'data\.gitignore'

To enable auto staging, run:
    dvc config core.autostage true
```

O `dvc` gera um arquivo com extensão `.dvc` no padrão `nome-do-arquivo.csv.dvc`. 
O exemplo a seguir mostra o conteúdo desse arquivo:
```yaml
outs:
- md5: 416545c6a16b623635d3b35d8a65711b
  size: 9757
  hash: md5
  path: dirty_data.csv
```

Se gerarmos outro '*dataset fake*' e adiciona-lo com o `dvc add <caminho-para-o-dataset>`, será gerado outro arquivo como o anterior.
```bash
$ python fake.py # one more time
$ dvc add data/dirty_dirty_data.csv
```

Aqui está um ponto importante! 
É através desses arquivos, que contém um hash do *dataset* e outras informações, é que o `dvc` irá fazer o versionamento dos dados.

Então, toda vez que alterarmos o *dataset*, mas manter o mesmo nome do arquivo, o `dvc` vai saber que não se trata do mesmo *dataset* através da informação do *hash*.

Uma recomendação é sempre após gerar uma nova versão do *dataset*, realizar um *commit* do arquivo de controle do `dvc`. 
Assim, estaremos também `versionando` os nossos *datasets*.

## 3º passo: definir um repositório remoto

Podemos também querer compartilhar os nossos dados de alguma forma.
O `dvc` possibilita a configuração de um repositório remoto de dados de forma semelhante ao que se propõe o `git`.

A [documentação](https://dvc.org/doc/start#storing-and-sharing) fornece maiores detalhes sobre as possibilidades dessa funcionalidade.
É possível configurar um repositório de dados remotos utilizando diversos provedores disponíveis no mercado.

Nesse exemplo, o repositório remoto vai ser apenas um outro diretório no mesmo nível que a pasta do nosso projeto.

```bash
$ cd ..
$ mkdir dvc-repo
$ ls dvc-repo # empty
```

Vamos vamos apontar ao repositório remoto com o comando:
```bash
$ cd ..
$ cd dvc-tutorial
$ dvc remote add -d myremote ..\dvc-repo
```

Agora estamos prontos para enviar o nosso *dataset* para esse repositório de dados remoto:
```bash
$ dvc push
```

Ou obter um *dataset* com o comando `dvc pull`.
```bash
$ dvc pull
```

Lembre-se, o `dvc` sempre vai utilizar aqueles arquivos `.dvc` gerenciar os *datasets*. 
Quando damos o comando `dvc pull` ele vai olhar para esses arquivos para determinar qual a versão do dataset que ele irá resgatar.

É bom lembrar que o GitHub não lida muito bem com [arquivos grandes](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

## 4º passo: Alterar e voltar ao que era antes

Nesse passo, vamos supor que realizamos alguma alteração no nosso *dataset* original:
```bash
$ python change.py
$ dvc status

data\dirty_data.csv.dvc:
    changed outs:
        modified:           data\dirty_data.csv
```

Caso tenhamos comitados no `git`, podemos nos certificar que o arquivo `data/dirty_data.csv.dvc` não foi alterado. 
Isto é, o `dvc` ainda está apontando a versão anterior do *dataset*.

Nós podemos realizar um `dvc commit` para dizer ao `dvc` que o *dataset* foi alterado.
```bash
$ dvc commit
```

Novamente, com o comando `git status` podemos ver que o conteúdo do nosso arquivo `data/dirty_data.csv.dvc` foi alterado:
```bash
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   data/dirty_data.csv.dvc
```

Agora, por um momento, imagine que essa alteração não era exatamente o que queríamos.
Podemos voltar o arquivo `data/dirty_data.csv.dvc` à sua versão anterior.
Nesse exemplo, vamos fazer isso com o comando:
```bash
$ git restore .\data\dirty_data.csv.dvc
```

Agora, se executarmos o seguinte comando, o nosso arquivo de dataset volta ao que era antes.
```bash
$ dvc checkout
Building workspace index                                                                            |2.00 [00:00,  128entry/s]
Comparing indexes                                                                                   |3.00 [00:00,    ?entry/s]
Applying changes                                                                                    |1.00 [00:00,  64.0file/s]
M       data\dirty_data.csv
```

O `dvc` mantém um cache das nossas versões do *dataset* na pasta `.dvc\cache\files\md5\..`.  
E sim, se não tomarmos cuidado, várias versões do *dataset* pode consumir muito espaço de armazenamento.
Porém, talvez apenas precisemos manter os passos seguidos para obter o nosso *dataset*.

## 5º passo: incluindo um pipeline

O pipeline pode ser descrito como diferentes estágios necessários para se obter um resultado ou cumprir uma tarefa.

Através do comando `dvc stage add` é possível definir um estágio do pipeline. 
Um estágio é definido através de um nome para identificação e de um comando que define o *script*  que é executado. 
Também é possível definir os arquivos dos quais o estágio depende (arquivos de dependência) e os arquivos de saída gerados (*outputs*).

```bash
$ dvc stage add --name prepare \
                --deps \pipe.py
                --deps data\dirty_data.csv \
                --outs data\normalized\clean_data.csv
                python pipe.py

Added stage 'prepare' in 'dvc.yaml'

To track the changes with git, run:

        git add dvc.yaml 'data\normalized\.gitignore'
```

Note que após executar o comando, o texto de saída sugere rastrear o arquivo `dvc.yaml` com o `git`.

<!-- <summary>
  Side note: Windows Power Shell usa o caracter ` para indicar uma quebra de linha em um comando. 
</summary> -->

## Reproduzir um pipeline

É possível reproduzir todo o pipeline do projeto com o comando `dvc repro`. 
O dvc irá executar os *scripts* de cada estágio, se observar que houve uma mudança nos arquivos que um estágio depende (arquivos de entrada, ou de dados) ou mudanças em parâmetros (registrados no arquivo `params.yaml`).

```bash
$ dvc repro

'data\dirty_data.csv.dvc' didn't change, skipping
Running stage 'prepare':
> python .\pipe.py
Generating lock file 'dvc.lock'
Updating lock file 'dvc.lock'

To track the changes with git, run:

        git add dvc.lock
```

Ao reproduzir a sequência de estágios de um pipeline, é gerado um arquivo chamado `dvc.lock` que registra o *hash* dos arquivos de dependência e arquivos de saída (*outputs*) gerados.
Conforme podemos ver no exemplo de saída reproduzido acima, o `dvc` recomenda que esse arquivo seja rastreado pelo `git`.

## Visualizando o pipeline

É possível visualizar o pipeline, isto é, a sequência de etapas registrada em nosso projeto com o comando `dvc dag`.
É possível gerar essa visualização em diferentes formatos. Para saber mais consulte a documentação [nesta página](https://dvc.org/doc/command-reference/dag).

```bash
$ dvc dag
```

DAG nesse contexto significa *Directed Acyclic Graph*. 
Isso se refere ao fato de que pipelines definidos dentro do dvc não podem possuir dependências circulares, isto é, C depende de B, que depende de A, e este último depende de C.

Também é possível utilizar o comando `dvc stage list` para listar todos os estágios registrados no arquivo `dvc.yaml`.

<!-- Segundo o dvc [suporta apenas um workflow por projeto](https://github.com/explosion/weasel/blob/main/docs/tutorial/integrations.md). -->

# Referências

 DVC Documentation. Disponível em <https://dvc.org/doc>. Último acesso em: 

 Awesome Pipeline:A curated list of awesome pipeline toolkits. Disponível em <https://github.com/pditommaso/awesome-pipeline>
