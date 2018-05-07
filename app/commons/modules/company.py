import app.company.models as model
import hashlib

def get_all_companys():
    response = {}
    try:
        data = model.fetch_all_companys()
        response['status'] = 'success'
        response['data'] = data
    except Exception as e:
        response['status'] = 'failure'
        response['data'] = None
        response['message'] = str(e)
    return response

def exists(email):
    return model.exists(email)

def get_company(rid):
    response = {}
    data = model.fetch_company(rid)
    try:
        data = model.fetch_company(rid)
        if data == {}:
            return {'status': 'failure', 'message': 'company doesn\'t exist'}
        response['status'] = 'success'
        response['data'] = data
    except Exception, e:
        response['status'] = 'failure'
        response['data'] = None
        response['message'] = str(e)
    return response

def register(form_data):
    response = {}
    data = {}
    data['user_name'] = str(form_data['user_name'])
    data['user_email'] = str(form_data['user_email'])
    data['user_password'] = hashlib.md5(str(form_data['password'])).hexdigest()

    try:
        status = model.register_company(data)
        response['status'] = 'success'
        response['user_email'] = data['user_email']
        response['user_name'] = data['user_name']
    except Exception as e:
        response['status'] = 'failure'
        response['data'] = None
        response['message'] = str(e)
    return response

def correct_credentials(user_email, user_password):
    stored_pass = model.get_pass(user_email)

    print '++++', hashlib.md5(str(user_password)).hexdigest()
    print '++++',stored_pass
    # print user_password, user_email

    return hashlib.md5(str(user_password)).hexdigest() == str(stored_pass)


def remove_company(rid):
    response = {}
    try:
        model.delete_company(rid)
        response['status'] = 'success'
    except Exception as e:
        response['status'] = 'failure'
        response['message'] = str(e)
    return response