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

## Política de Revisão de Código para DAGs

### Checklist de Revisão
- [ ] Nome do arquivo e `dag_id` seguem padrão definido
- [ ] Docstring presente e clara
- [ ] Código está bem comentado e legível
- [ ] Não há dados sensíveis ou credenciais no código
- [ ] Uso correto de variáveis de ambiente
- [ ] Estrutura e dependências da DAG estão corretas
- [ ] Testes unitários presentes (se aplicável)
- [ ] DAG executa sem erros locais
- [ ] CI/CD passou sem falhas

### Processo
1. Abrir Pull Request com a nova DAG ou alteração
2. Outro membro do time realiza revisão utilizando o checklist
3. Correções sugeridas devem ser aplicadas antes do merge
4. Após aprovação, realizar merge na branch principal

### Testes

- Sempre que possível, adicione testes unitários para funções críticas das DAGs.

## Testes Automatizados para DAGs

Exemplo de teste automatizado para DAGs disponível em `tests/test_example_dag.py`.

### Como executar os testes
1. Instale as dependências de desenvolvimento:
	```bash
	pip install -r requirements-dev.txt
	```
2. Execute os testes localmente:
	```bash
	pytest tests/
	```
3. Pré-commit: Instale e configure o pre-commit para rodar os testes antes de cada commit:
	```bash
	pip install pre-commit
	pre-commit install
	```
	O hook irá rodar `pytest` automaticamente.
4. CI/CD: Os testes automatizados são executados no pipeline do GitHub Actions a cada push ou PR.

Os testes verificam se a DAG pode ser importada corretamente e se sua estrutura está conforme o esperado.

## Processo de Deploy das DAGs no Airflow

1. Realize as alterações desejadas nas DAGs dentro do diretório `dags/`.
2. Garanta que todas as validações locais e do CI/CD estejam passando.
3. Abra um Pull Request para revisão e aprovação.
4. Após o merge na branch principal, o código será versionado e estará pronto para deploy.
5. O deploy das DAGs pode ser realizado de duas formas:
	- **Deploy automático:** Caso o ambiente Airflow esteja integrado ao repositório, o código será sincronizado automaticamente (ex: via CI/CD ou mount do diretório).
	- **Deploy manual:** Realize o upload dos arquivos do diretório `dags/` para o servidor Airflow, respeitando a estrutura definida.
6. Verifique no Airflow se as DAGs aparecem corretamente e estão habilitadas.
7. Monitore a execução inicial para garantir que não há erros.

**Observações:**
- Nunca faça deploy de DAGs sem revisão e validação.
- Mantenha o histórico de alterações e utilize tags/releases para versões importantes.
