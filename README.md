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

### Boas práticas
- Documente cada DAG com docstring.
- Utilize variáveis de ambiente para dados sensíveis.
- Versione apenas arquivos necessários.

---
Consulte as issues para tarefas pendentes e sugestões de melhorias.