# Pipeline ETL para Notificar Clientes sobre Novidades em Artes

Este é um exemplo de um Pipeline ETL (Extração, Transformação e Carga) em Python que extrai dados de um arquivo CSV, realiza transformações e envia notificações por e-mail para clientes de uma revista eletrônica sobre novidades no mundo do design. O pipeline é baseado no uso do Pandas para manipulação de dados e no módulo smtplib para o envio de e-mails.

## Pré-requisitos
Antes de executar o pipeline, certifique-se de que você tenha o Python instalado em seu sistema e as seguintes bibliotecas:

## Pandas
smtplib
email.mime

## Configuração
Antes de executar o pipeline, é necessário configurar as informações de e-mail. Edite o arquivo pipeline_etl.py e ajuste as seguintes configurações:

- email_host: O servidor SMTP do seu provedor de e-mail.
- email_port: A porta do servidor SMTP.
- email_username: Seu nome de usuário de e-mail.
- email_password: Sua senha de e-mail.
- sender_email: O endereço de e-mail do remetente.

## Uso

Siga as etapas a seguir para executar o pipeline:

Crie um arquivo CSV com os dados dos clientes, incluindo nome, endereço de e-mail e um indicador de novidades. 

Salve o arquivo CSV na mesma pasta onde você possui o arquivo teste-pipeline-etl.py

Abra um terminal ou prompt de comando e navegue até o diretório onde os arquivos estão localizados.

Execute o pipeline com o seguinte comando:
python teste-pipeline-etl.py

O código processará os dados do arquivo CSV, verificará se há novidades a serem notificadas para cada cliente e enviará e-mails apropriados.

## Personalização

Você pode personalizar o pipeline ETL para atender às necessidades específicas do seu projeto. Isso inclui a lógica de processamento de dados, a mensagem de e-mail e a integração com outras fontes de dados ou serviços de envio de e-mail.

## Notas Adicionais

Certifique-se de que seu servidor de e-mail permita o envio de e-mails por meio do SMTP. Você pode precisar configurar permissões de segurança.

Para depuração e desenvolvimento, você pode usar um servidor de e-mail local, como o Mailtrap, para evitar o envio de e-mails reais durante o teste.

Thais Di Gianni

Sinta-se à vontade para personalizar e adicionar mais informações ao README, conforme necessário, para atender aos requisitos do seu projeto e torná-lo mais informativo para outros colaboradores e usuários.
