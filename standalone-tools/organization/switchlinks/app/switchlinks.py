"""

Organization functions

"""

import boto3

def get_self_account_id():
    """
    Easy WhoIam function to get the account id
    :return: String()
    """
    client = boto3.client('sts')
    return client.get_caller_identity()['Account']


def get_all_accounts(accounts_list=[], next_token=None):
    """
    :return: list of accounts linked to the organization
    """

    self_acct = get_self_account_id()
    client = boto3.client('organizations')
    if isinstance(next_token, str):
        print("Next token present")
        accounts_r = client.list_accounts(NextToken=next_token)
    else:
        print("no next token found")
        accounts_r = client.list_accounts()

    if 'NextToken' in accounts_r.keys():
        for account in accounts_r['Accounts']:
            if account['Id'] != self_acct and account['Status'] == 'ACTIVE':
                del account['JoinedTimestamp']
                accounts_list.append(account)
        return get_all_accounts(accounts_list, accounts_r['NextToken'])
    else:
        for account in accounts_r['Accounts']:
            if account['Id'] != self_acct and account['Status'] == 'ACTIVE':
                del account['JoinedTimestamp']
                accounts_list.append(account)
        return accounts_list


def get_accounts_details():
    accts_list = get_all_accounts([], None)
    print(len(accts_list))
    accounts_details = []

    for account in accts_list:
        acct_number=account['Id']
        acct_name=account['Name'].strip().split(' ')[0]
        signin_info = {
            'account_id': acct_number,
            'account_name': acct_name
        }
        accounts_details.append(signin_info)
    print(len(accounts_details))
    return accounts_details
