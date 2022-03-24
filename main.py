import sys
import requests
import dateparser
from datetime import datetime


def send_form(*, student_name: str, home_task: str, teacher_name: str) -> int:
    url = "https://docs.google.com/forms/d/e/1FAIpQLSc0Lk5uKCLMd9-5H0MZafGf-LmShY-VAgs5iYS21LG5bedD5A/formResponse"
    values = {
        # keys have taken from input tags of google form
        'entry.1052913965': student_name,
        'entry.2015510883': home_task,
        'entry.638434999': teacher_name
    }
    response = requests.post(url, data=values)
    return response.status_code


def wait_till(time_to_send_form: str) -> None:
    try:
        time_to_send_form = dateparser.parse(time_to_send_form).strftime('%H:%M:%S')
        while True:
            now = datetime.now().strftime('%H:%M:%S')
            if now >= time_to_send_form:
                print('The time has come!')
                break
            print('waiting...')
    except KeyboardInterrupt:
        print('not waiting anymore :(')
        sys.exit()


def main():
    wait_till("15:19:59")  # time when form will be sent
    code = send_form(student_name='Гринь Владислав Владимирович',
                     home_task='04. Implementor',
                     teacher_name='Каменев Юрий Владимирович')
    print(f'Response code: {code}')
    print('smth')


if __name__ == '__main__':
    main()
