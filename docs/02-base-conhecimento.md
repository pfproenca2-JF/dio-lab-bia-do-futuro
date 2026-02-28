Dados Utilizados
O IAGO utiliza a estrutura de dados mockados para fundamentar todas as decisões e análises operacionais.
| Arquivo | Formato | Utilização no Agente |
|---|---|---|
| historico_atendimento.csv | CSV | Identificar problemas recorrentes e o tom de voz preferido pelo cliente. |
| perfil_investidor.json | JSON | Definir os limites de risco para sugestão de novos aportes. |
| produtos_financeiros.json | JSON | Catálogo oficial de ativos disponíveis para recomendação operacional. |
| transacoes.csv | CSV | Base para auditoria de gastos e detecção de anomalias financeiras. |
Adaptações nos Dados
Os dados originais foram mantidos em sua estrutura padrão para garantir a compatibilidade com o desafio, porém, o IAGO realiza uma pré-processamento lógico:
 * Agrupamento de transações por categoria (Lazer, Saúde, Alimentação).
 * Cruzamento do nível de risco do produto com o score do perfil do investidor.
Estratégia de Integração
Como os dados são carregados?
Os dados são carregados via biblioteca Pandas no Python assim que a aplicação é iniciada. Eles são armazenados em DataFrames na memória para acesso rápido durante a sessão do chat.
Como os dados são usados no prompt?
Os dados não são inseridos inteiros no prompt (para evitar consumo excessivo de tokens). O IAGO utiliza uma técnica de RAG (Retrieval-Augmented Generation) simplificada:
 * O código identifica quais dados são relevantes para a pergunta do usuário.
 * Um resumo estruturado (JSON ou texto formatado) é injetado no contexto da conversa.
Exemplo de Contexto Montado
Quando o cliente pergunta "Posso investir este mês?", o contexto injetado no IAGO é formatado assim:
[DADOS OPERACIONAIS DO CLIENTE]
- Perfil: Arrojado (Score 8/10)
- Saldo em conta: R$ 12.450,00
- Gastos Fixos Médios: R$ 4.200,00

[PRODUTOS DISPONÍVEIS COMPATÍVEIS]
1. ETF de Tecnologia (Risco: Alto / Retorno: Alto)
2. Ações Dividendos (Risco: Médio / Retorno: Médio)

[ÚLTIMO INSIGHT DE GASTOS]
- Identificada economia de 10% em 'Alimentação' este mês.
