# Pesquisa e Apresentação: Non-Functional Testing - Stress Testing and Performance Testing

## 1. Introdução sobre o Tema

Non-Functional Testing (Testes Não-Funcionais) é uma categoria de testes de software que avalia aspectos como desempenho, usabilidade, confiabilidade e escalabilidade de um sistema, em vez de suas funcionalidades específicas. Dentro desta categoria, Stress Testing e Performance Testing são duas técnicas críticas para garantir que um sistema opere adequadamente sob diversas condições.

## 2. Histórico

- **Década de 1970**: Surgimento dos primeiros conceitos de teste de software, focados principalmente em funcionalidades.
- **Década de 1990**: Crescimento da complexidade dos sistemas e necessidade de avaliar não apenas "o que" o software faz, mas "como" ele faz.
- **Anos 2000**: Popularização de metodologias ágeis e DevOps, aumentando a importância dos testes não-funcionais para garantir qualidade contínua.
- **Atualmente**: Stress Testing e Performance Testing são essenciais para aplicações críticas, como bancos, e-commerce e sistemas de saúde.

## 3. O que é?

- **Performance Testing**: Avalia a velocidade, capacidade de resposta e estabilidade do sistema sob uma carga de trabalho específica.
- **Stress Testing**: Testa os limites do sistema, submetendo-o a cargas extremas para identificar pontos de falha e comportamento sob condições adversas.

## 4. Qual o propósito?

- Garantir que o sistema atenda aos requisitos de desempenho em condições normais e extremas.
- Identificar gargalos, como lentidão ou falhas, antes que afetem os usuários finais.
- Validar a escalabilidade e robustez do sistema.

## 5. Principais vantagens e desvantagens

### Vantagens:
- **Melhoria da experiência do usuário**: Sistemas rápidos e estáveis aumentam a satisfação.
- **Prevenção de custos**: Identificar problemas antes da produção reduz gastos com correções.
- **Conformidade**: Atende a requisitos regulatórios e de negócios.

### Desvantagens:
- **Complexidade**: Requer ferramentas especializadas e conhecimento técnico.
- **Custo e tempo**: Pode ser demorado e caro, especialmente para sistemas grandes.
- **Ambiente controlado**: Resultados podem não refletir totalmente o cenário real.

## 6. Exemplos de ferramentas/frameworks

- **JMeter**: Ferramenta open-source para testes de carga e desempenho.
- **LoadRunner**: Solução robusta para testes de estresse e desempenho em ambientes complexos.
- **Gatling**: Ferramenta moderna focada em desempenho e facilidade de uso.
- **Locust**: Framework Python para testes de carga distribuídos.

## 7. Ilustração lúcida sobre o exemplo prático

Imagine um site de e-commerce durante a Black Friday:
- **Performance Testing**: Simula 10.000 usuários acessando o site simultaneamente para verificar se o tempo de resposta permanece aceitável.
- **Stress Testing**: Submete o site a 50.000 usuários para identificar se ele crasha ou como se comporta sob carga extrema.

## 8. Demonstração do exemplo prático

### Exemplo usando JMeter:
1. **Configurar o JMeter** para simular usuários acessando a página principal do e-commerce.
2. **Definir o número de threads (usuários simulados)**:
   - Performance Testing: 10.000 usuários.
   - Stress Testing: 50.000 usuários.
3. **Executar o teste** e monitorar métricas como tempo de resposta, taxa de erro e uso de CPU.
4. **Analisar resultados**:
   - Gráficos de tempo de resposta.
   - Relatórios de erros e gargalos identificados.

### Resultados esperados:
- Sob 10.000 usuários, o tempo de resposta deve ser inferior a 2 segundos.
- Sob 50.000 usuários, o sistema pode mostrar lentidão ou falhas, indicando a necessidade de otimização.

## 9. Referências

- **Livros**:
  - "Performance Testing Guidance for Web Applications" by Microsoft Patterns & Practices.
  - "Apache JMeter: A Practical Beginner's Guide to Automated Testing and Performance Measurement" by Emily H. Halili.
- **Artigos acadêmicos**:
  - "A Systematic Review of Performance Testing for Web Applications" (Journal of Systems and Software).
  - "Stress Testing in Software Engineering: Techniques and Tools" (IEEE Software).
- **Sites de ferramentas**:
  - [JMeter](https://jmeter.apache.org/)
  - [Gatling](https://gatling.io/)
  - [LoadRunner](https://www.microfocus.com/en-us/products/loadrunner-professional/overview)
