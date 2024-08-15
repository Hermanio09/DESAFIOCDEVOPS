# DESAFIOCDEVOPS

# Aplicação de Geração de Logs de Informações Climáticas.

Esta aplicação coleta informações climáticas periodicamente em tempo real de uma localização específica usando a API do OpenWeatherMap. Os dados que sao coletados são a temperatura daquela localidade, a sensação termica, a porcentagem de umidade no ar, velocidade do vento, como esta o tempo e a pressão atmosferica, essas informações são armazenadas em um arquivo JSON e processados usando a stack ELK (Elasticsearch, Logstash, Kibana e Filebeat).

1. Iniciar os serviços utilizando Docker Compose:

   Para iniciar todos os serviços necessários, utilize o Docker Compose com o comando:
   Esse comando iniciará os contêineres em segundo plano (modo detached).

   docker compose up -d

   Para validar se os contêineres foram criados e estão em execução utilizando o comando:
   Este comando ira listar todos os contêineres, mostrando seu status atual (em execução, parado, etc.).
   
   docker ps -a 

   ![image](https://github.com/user-attachments/assets/70ed5d4f-adf6-4452-a641-b6f386366df8)

2. Descrição da aplicação.

    A aplicação foi feita em Python. Esta aplicação coleta informações climáticas a cada minuto em tempo real de uma localização específica (neste caso, Fortaleza, Ceará) usando a API do OpenWeatherMap. Os dados que sao coletados são: a temperatura daquela localidade, a sensação termica, a porcentagem de umidade no ar, velocidade do vento, como esta o tempo e a pressão atmosferica. Essas informações são armazenadas em um arquivo JSON e processados usando a stack ELK (Elasticsearch, Logstash e Kibana).


2. Acessando as portas do ELK definidos no "docker-compose.yaml" para validar se esta tudo correto com as aplicações. Foi definido uma porta especifia para cada ferramenta. No caso Elasticsearch(porta:9200), Logstash(5044) e Kibana(5601). Para fazer a validação das aplicações e necessario acessar o link "localhost:porta-aplicação".

Para validar se as aplicações estão rodando corretamente, acesse os seguintes links
        
  Elasticsearch(localhost:9200)
  ![image](https://github.com/user-attachments/assets/9d591767-bc08-456e-a3cf-756919dbbff7)
  ![image](https://github.com/user-attachments/assets/9ee0ac9e-1b05-40bf-8978-7ca5f9a82fcb)

  Logstash(locahost:5044)
  ![image](https://github.com/user-attachments/assets/6b300905-fb70-4cbd-a52d-c09fa7cc0f06)
  ![image](https://github.com/user-attachments/assets/43820bfe-deba-4dd1-9704-448e52a7ce4f)

  Kibana(localhost:5601)
  ![image](https://github.com/user-attachments/assets/fe66231a-a41b-485c-ab29-9a6e30d11604)
  ![image](https://github.com/user-attachments/assets/ff265089-fa37-45fd-b667-d1606cd8b919)

3. Acessar o Kibana para visualizar os Logs:
   
    È necessario acessar a porta '5601'.
    ![image](https://github.com/user-attachments/assets/8d088d17-5bb0-4d3a-9297-2e09f35787ab)

    Depois e necessario ir na opção 'Analytics'.
    ![image](https://github.com/user-attachments/assets/7483bf17-2d31-4c59-8364-3949d63eede9)

    Na pagina de 'Analytics' selecionar a opção 'Discover'.
    ![image](https://github.com/user-attachments/assets/5d6f9fe1-33cb-43c8-ab12-45340b5cd6f8)

    Onde será direcionado para a página onde os logs coletados são exibidos e processados.
    Configure um padrão de índice com o nome `clima_atual`.
    Após configurar, você poderá explorar e visualizar todos os logs processados.
    ![image](https://github.com/user-attachments/assets/d196a29a-5716-427a-b472-fb42e757e558)


# Informações Relevantes

- Persistência de Dados: Os volumes montados no `docker-compose.yml` garantem que os dados do Elasticsearch e do Filebeat persistam, mesmo que reinicie os containers.

- Monitoramento e Logs: Use o comando `docker-compose logs -f` para monitorar os logs dos serviços em tempo real.

## Comandos Úteis

- Parar todos os contêineres:

  Para encerrar todos os serviços:


  docker-compose down


- Verificar logs dos serviços:

  Para monitorar os logs dos serviços:


  docker-compose logs -f


- Acessar um contêiner em execução:

  Para entrar em um contêiner específico:


  docker exec -it <nome-do-contêiner> /bin/bash
