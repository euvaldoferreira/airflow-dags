# airflow-dags

## Estrutura do Projeto

Este repositório tem como objetivo versionar as DAGs do Airflow utilizadas no ambiente.

### Diretórios

- `dags/`: Armazena todas as DAGs versionadas.

### Como adicionar uma nova DAG

1. Crie o arquivo da DAG em `dags/` seguindo o padrão de nomenclatura.
2. Realize testes locais antes de subir para produção.
3. Abra um Pull Request para revisão.

### Exemplo de DAG

Veja o arquivo `dags/example_dag.py` para um exemplo básico.

## Padrão de Versionamento e Boas Práticas

### Convenção de Nomenclatura

- Use nomes descritivos para os arquivos de DAG, separados por underline. Exemplo: `etl_vendas_diario.py`
- O nome da DAG (`dag_id`) deve refletir o propósito do fluxo.

### Organização dos Arquivos

- Todas as DAGs devem estar no diretório `dags/`.
- Evite arquivos de configuração ou dados sensíveis no repositório.

### Docstrings e Comentários

- Cada DAG deve conter uma docstring no início explicando seu objetivo, autor e data de criação.
- Comente trechos complexos do código.

### Variáveis de Ambiente

- Utilize variáveis de ambiente para credenciais e dados sensíveis.
- Nunca versionar senhas ou tokens.

### Versionamento

- Cada alteração relevante em uma DAG deve ser registrada via commit.
- Utilize Pull Requests para revisão e aprovação.
- Recomenda-se adotar versionamento semântico no nome da DAG, se aplicável (ex: `etl_vendas_diario_v2`).

### Revisão de Código

- Toda DAG nova ou alterada deve passar por revisão de outro membro do time.
- Utilize o checklist de boas práticas antes de aprovar.

### Testes

- Sempre que possível, adicione testes unitários para funções críticas das DAGs.
