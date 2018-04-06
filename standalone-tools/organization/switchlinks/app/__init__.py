

import operator
from flask import Flask, render_template
from .switchlinks import get_accounts_details

app = Flask(__name__)


@app.route('/')
def return_links():
    roles = [
        'wh-SysAdmins',
        'wh-SrSysAdmins'
    ]
    accounts = get_accounts_details()
    print(len(accounts))
    return render_template('switchlinks.html.j2', accounts=accounts, roles=roles)
