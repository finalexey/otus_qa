import socket
import random
import logging
import re
from http import HTTPStatus

logging.basicConfig(level=logging.DEBUG)

HOST = "127.0.0.1"
PORT = random.randint(10000, 20000)


def collecting_out_string(dict_data):
    out_str = ''
    for k, v in dict_data.items():
        out_str += str(k)
        out_str += ': '
        out_str += str(v)
        out_str += '\r\n'
    return out_str


def parsing_data(raw_data):
    decoded_data = raw_data.decode('UTF-8')
    splited_data = decoded_data.split('\r\n')
    lists = []
    method = re.search(r"(POST|GET|PUT|PATCH|OPTIONS|DELETE|HEAD)", str(raw_data))[0]

    for i in splited_data:
        lists.append(i.split(':', 1))

    if re.search(r"=\d{3}", str(lists[0][0])):
        code = re.search(r"\s/\S*", str(lists[0][0]))
        status_code = int((code.group())[-3:])
        status_text = HTTPStatus(status_code).name
    else:
        status_code = 200
        status_text = HTTPStatus(status_code).name

    request_method = method
    request_source = (lists[1][1].split(':'))
    response_status = f'{status_code} {status_text}'

    out_data = {
        "Request Method": request_method,
        "Request Source": (str(request_source[0][1:]), int(request_source[1])),
        "Response Status": response_status
    }

    for i in lists[2:-2]:
        out_data[i[0]] = i[1][1:]
    return out_data


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Binding server on {HOST}:{PORT}")
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()

        data = conn.recv(1024)
        if not data or data == b"close":
            print("Got termination signal", data, "and closed connection")
            conn.close()
            break
        elif data != b"close" and data:
            parsed_data = parsing_data(data)
            out_string = collecting_out_string(parsed_data)
            conn.send(str(out_string).encode("utf-8"))
            logging.info(f"Sent '{data}' to {addr}")
            conn.close()
