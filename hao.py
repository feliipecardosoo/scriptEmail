import smtplib
from email.mime.text import MIMEText

# Configurações do servidor SMTP
smtp_server = 'smtp.mail.me.com'
smtp_port = 587
smtp_user = ''
smtp_password = ''

# Lista de empregados, e-mails, pagamentos e retornos
empregados = ["AMANDA ANTUNES PEREPELICIA", "Angel Soares Ribeiro", "BARBARA SANTOS DE OLIVEIRA",
              "BRUNA BARCELOS DE SIMAS", "BRUNO DE SOUZA MACHADO", "BRUNO SILVA HEMPEL", "CAMILA BLOS RIBEIRO",
              "Carolina de Jesus de Camargo", "CASSANDRA DE CASSIA RUFATO", "CINTIA APARECIDA LUCAS",
              "Daniel Goulart Bernardes", "ELIANE MARQUES DE SOUZA", "Elias Arlindo Barbosa",
              "Fernanda Severo Schreiner", "GABRIELA DE SOUZA", "Giovanna Santos Dede", "Gisele de Oliveira Roque",
              "GIULIA THEREZA MAGALHAES", "Guilherme Zaia", "Henrique Mattevi Lisboa", "JOSE ANDERSON GUIMARAES",
              "JOSOE BUENO IENERICH", "Julia Beatriz Agnes", "Juliana Aparecida Sutil da Silva",
              "JULIANA SCHMIDT ROSA", "KALEU DO NASCIMENTO DA ROCHA", "LETICIA ILBERTO DA SILVA",
              "LUIS HENRIQUE CEREGHINI PIRES", "Marcio Vinicius Collares da Silva", "Marcus Vinicius da Silva",
              "Mariana Castello Branco Iwakami", "Mariane Correa Silveira", "Marilia Melina May",
              "Marina Aparecida Magnini Portes", "Millena Biff", "Paola de Jesus", "PEDRO HENRIQUE VAZ",
              "ROBSON LOPES ATOLINI", "ROSELI FAUSTINO DA SILVA", "SERGIO LUIZ RODRIGUES JUNIOR",
              "SHEILA LOBO DOS SANTOS", "Suellen Lima da Silva", "THAIS ADRIANO", "Thayna Correa", "Vilson da Rocha",
              "Willian Goncalves da Silva", "WILLIAN ULIANA"]
emails = ['administrativo@westarblog.com.br']
pagamentos = ["15/12/2023", "22/12/2023", "15/12/2023", "22/12/2023", "22/12/2023", "01/12/2023", "15/12/2023",
              "08/12/2023", "08/12/2023", "15/12/2023", "22/12/2023", "22/12/2023", "01/12/2023", "22/12/2023",
              "15/12/2023", "15/12/2023", "22/12/2023", "15/12/2023", "15/12/2023", "01/12/2023", "01/12/2023",
              "15/12/2023", "15/12/2023", "22/12/2023", "22/12/2023", "15/12/2023", "22/12/2023", "22/12/2023",
              "08/12/2023", "15/12/2023", "22/12/2023", "22/12/2023", "22/12/2023", "22/12/2023", "22/12/2023",
              "08/12/2023", "15/12/2023", "15/12/2023", "22/12/2023", "22/12/2023", "15/12/2023", "22/12/2023",
              "15/12/2023", "08/12/2023", "01/12/2023", "22/12/2023", "15/12/2023"]
retornos = ["04/01/2024", "02/01/2024", "28/12/2023", "02/01/2024", "05/01/2024", "19/12/2023", "26/12/2023",
            "18/12/2023", "26/12/2023", "28/12/2023", "10/01/2024", "10/01/2024", "11/12/2023", "10/01/2024",
            "02/01/2024", "02/01/2024", "02/01/2024", "18/01/2024", "26/12/2023", "19/12/2023", "19/12/2023",
            "02/01/2024", "02/01/2024", "10/01/2024", "10/01/2024", "17/01/2024", "11/01/2024", "10/01/2024",
            "27/12/2023", "26/12/2023", "10/01/2024", "10/01/2024", "02/01/2024", "02/01/2024", "02/01/2024",
            "10/01/2024", "02/01/2024", "02/01/2024", "10/01/2024", "10/01/2024", "17/01/2024", "02/01/2024",
            "09/01/2024", "22/12/2023", "14/12/2023", "02/01/2024", "02/01/2024"]

mensagem = '<html><body><p>Conforme solicitado, segue anexo os avisos e recibos de férias</p>'
for empregado, pagamento, retorno in zip(empregados, pagamentos, retornos):
    mensagem += f'<p><strong>{empregado}</strong><br/>• Pagamento em: <strong>{pagamento}</strong><br/>• Retorno em: <strong>{retorno}</strong></p>'
mensagem += '</body></html>'

# Configurar o e-mail como HTML
msg = MIMEText(mensagem, 'html')
msg['Subject'] = 'teste 02'
msg['From'] = smtp_user
msg['To'] = ', '.join(emails)

# Configurar o servidor SMTP e enviar e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(smtp_user, emails, msg.as_string())

print('E-mail consolidado enviado com sucesso!')
