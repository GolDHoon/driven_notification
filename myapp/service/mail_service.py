import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import os


def send_email(receiver_email, subject, body):
    smtp_server = 'smtp.daum.net'
    smtp_port = 465

    msg = MIMEMultipart()
    msg['From'] = 'master@datamon.kr'
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    current_directory = os.path.dirname(os.path.abspath(__file__))
    cert_path = '/etc/ssl/certs/driven-notification.xyz_crt.pem'
    key_path = '/etc/ssl/certs/driven-notification.xyz_key.pem'

    key_password = 'emflqms1!'  # 키 암호 입력

    print(f'인증서 경로: {cert_path}')
    print(f'키 파일 경로: {key_path}')

    if not os.path.isfile(cert_path):
        print(f'인증서 파일을 찾을 수 없습니다: {cert_path}')
        return
    if not os.path.isfile(key_path):
        print(f'키 파일을 찾을 수 없습니다: {key_path}')
        return

    server = None  # 초기화

    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        print('SSL 컨텍스트가 성공적으로 생성되었습니다.')

        context.load_cert_chain(certfile=cert_path, keyfile=key_path, password=key_password)
        print('인증서와 키 파일이 성공적으로 로드되었습니다.')

        print(f'SMTP 서버 연결 시도: {smtp_server}:{smtp_port}')
        server = smtplib.SMTP_SSL(smtp_server, smtp_port, context=context)
        print('SMTP 서버에 성공적으로 연결되었습니다.')

        print('로그인 시도')
        server.login('master@datamon.kr', 'xsjouhivvsavxnti')  # 서버에 로그인합니다.
        print('로그인 성공')

        print('메일 발송 시도')
        server.send_message(msg)
        print('이메일을 성공적으로 발송했습니다.')
    except ssl.SSLError as ssl_error:
        print(f'SSL 오류가 발생했습니다: {ssl_error}')
    except Exception as e:
        print(f'이메일 발송에 실패했습니다: {e}')
    finally:
        if server is not None:
            server.quit()
            print('SMTP 연결이 종료되었습니다.')


if __name__ == "__main__":
    receiver_email = 'sch@driven.co.kr'
    subject = '테스트 이메일'
    body = '이것은 테스트 이메일입니다.'

    send_email(receiver_email, subject, body)
