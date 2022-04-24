from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/contacts')
def contacts():
    return f'''<title>Информация</title>
            <h1>Адреса и контакты</h1>
            <a href="http://127.0.0.1:8080/main">Вернуться на главную</a>
            <div class="col-lg-7 col-md-12">
                <address><i class="sprite sprite-ico-04"></i>
                <span>г. Алматы, Бостандыкский район, Бульвар Бухар Жырау 36</span>
                <a href="https://yandex.kz/maps/org/1016863838/?ll=76.917620%2C43.231417&mode=search&sll=76.945456%2C43.238286&sspn=0.517044%2C0.213860&text=%D0%A0%D0%A4%D0%9C%D0%A8&z=16">На карте</a>
                </address>
            </div>
            <div class="col-lg-7 col-md-12">
                <address><i class="sprite sprite-ico-04"></i>
                <span>г. Нур-Султан, район Есиль, ул. Туркестан 2/1</span>
                <a href="https://yandex.kz/maps/org/97610247884/?ll=71.431741%2C51.119462&mode=search&sctx=ZAAAAAgBEAAaKAoSCaXz4VmCPFNAER6M2CeAnkVAEhIJDfrS25%2BL4D8Rchb2tMNfyz8iBgABAgMEBSgKOABAogFIAWoCa3qdAc3MTD2gAQCoAQC9AabfQKjCAQXeuPDkA%2BoBAPIBAPgBAIICCNCg0KTQnNCoigIAkgIAmgIMZGVza3RvcC1tYXBz&sll=71.431741%2C51.119462&sspn=0.014952%2C0.005356&text=%D0%A0%D0%A4%D0%9C%D0%A8&z=16.34">На карте</a>
                </address>
            </div>
            <li>Тел.: +7 (7172) 79-72-74, +7 (727) 395-01-83</li>
            <li>Почта: reception@fizmat.kz, astana@fizmat.kz</li>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
