# PathPlanningStudies
# This is a repo for RaulMyron studies into the PathPlanning world 

```py
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

# Sistema de Path Planning para RoboCup SSL
Implementação de sistema de navegação e planejamento de trajetória para robôs da categoria SSL.

## Requisitos de Implementação

### Performance
- Taxa de atualização: 60Hz mínimo
- Tempo de computação por caminho: < 5ms
- Suporte para até 6 robôs simultâneos

### Integração
- Sistema de visão SSL
- Comunicação com robôs via protocolo SSL
- Interface com sistema de controle existente

### Segurança
- Mecanismo de prevenção de colisões
- Sistema de parada de emergência 
- Validação de comandos de velocidade

### Desenvolvimento
- Testes em simulação obrigatórios
- Documentação de APIs
- Logs para depuração

## Métricas de Avaliação
- Tempo médio de computação de caminhos
- Taxa de sucesso em desvio de obstáculos
- Suavidade das trajetórias geradas
- Eficiência da coordenação entre robôs
- Cobertura de testes   