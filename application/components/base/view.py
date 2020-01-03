import os
import requests
import random, string
from datetime import datetime
import json as json_load
from sqlalchemy import and_, or_
from gatco.response import json
from gatco import Blueprint
import aiofiles
from gatco.response import json, text, html
from gatco_restapi.helpers import to_dict
from application.extensions import apimanager
from application.extensions import auth
from application.database import db
from application.server import app
from .model import Configuration, ConnectionApp, Notify
# from application.common.constants import ERROR_CODE, ERROR_MSG, STATUS_CODE
from application.common.helper import get_local_today

SKEY = "5IH6U2QU2DL57W2I3D5VP7B72UW7CCA70X4KP0LXJCSGY057J09EDQBLRXITFY76L1WG773GP1MT7XRHN6L7M3IJQR3WV0877UT4S3ANU27SQOF30Q0SJ92G6BIRHG4E"

def auth_func(request=None, **kw):
    try:
        if auth_func(request):
            return {
                "valid": True
            }
        else:
            app_key = request.headers.get('X-UPCRM-APPKEY', None)
            app_secret = request.headers.get('X-UPCRM-SECRETKEY', None)
            super_key = request.headers.get('X-UPCRM-SUPERKEY', None)
            connector = get_3nd_auth(app_key)
            if app_key is not None and app_secret is not None and connector is not None:
                if connector['app_id'] == app_key and connector['secret_key'] == app_secret:
                    return {
                        "valid": True
                    }
                else:
                    return {
                        "valid": False,
                        "error": {
                            "error_code": ERROR_CODE['AUTH_ERROR'],
                            "error_message": ERROR_MSG['AUTH_ERROR']
                        },
                        "status": 523
                    }
            elif (super_key is not None and super_key == SKEY):
                return {
                    "valid": True
                }
            else:
                return {
                    "valid": False,
                    "error": {
                        "error_code": ERROR_CODE['AUTH_ERROR'],
                        "error_message": ERROR_MSG['AUTH_ERROR']
                    },
                    "status": 523
                }
    except:
        return {
            "valid": False,
            "error": {
                "error_code": ERROR_CODE['AUTH_ERROR'],
                "error_message": ERROR_MSG['AUTH_ERROR']
            },
            "status": 523
        }


def verify_access(request, **kw):

    result = auth_func(request)
    
    if 'valid' in result and result['valid'] == False:
        return json(result['error'])



def super_access(request, **kw):
    super_key = request.headers.get('X-UPCRM-SUPERKEY', None)
    if (super_key is not None and super_key == SKEY):
        return {
            "valid": True
        }
    else:
        return {
            "valid": False,
            "error": {
                "error_code": ERROR_CODE['AUTH_ERROR'],
                "error_message": ERROR_MSG['AUTH_ERROR']
            },
            "status": 523
        }


def verify_token(request, **kw):
    app_token = request.headers.get('X-UPCRM-TOKEN', None)
    if app_token is None:
        return {
            "valid": False,
            "error": {
                "error_code": ERROR_CODE['TOKEN_ERROR'],
                "error_message": ERROR_MSG['TOKEN_ERROR']
            },
            "status": 523
        }
    
    session_data = session_redis_db.get("sessions:" + app_token)
    if session_data is None:
        return {
            "valid": False,
            "error": {
                "error_code": ERROR_CODE['TOKEN_ERROR'],
                "error_message": ERROR_MSG['TOKEN_ERROR']
            },
            "status": 523
        }
    token_info = json_load.loads(str(session_data.decode('ascii'))) 
    
    return {
        "valid": True
    }


def request_new_token():
#     try:
    configuration = Configuration.query.filter().first()
        
    if configuration is not None:
        headers = {
            'content-type': 'application/json'
        }
        data = {
            "appkey": configuration.app_key,
            "appsecret": configuration.app_secret
        }

        response = requests.post(app.config['APP_TOKEN_API'], data=json_load.dumps(data), headers=headers)
        
        if response.status_code == STATUS_CODE['OK']:
            res = to_dict(response.json())
            configuration.token = res['token']
            db.session.commit()
            
            return {
                "status": STATUS_CODE['OK'],
                "token": configuration.token
            }
        else:
            error = to_dict(response.json())
            return {
                "status": STATUS_CODE['ERROR'],
                "error": {
                    "error_code": error['error_code'],
                    "error_message": error['error_message']
                }
            }
    return {
        "status": STATUS_CODE['ERROR'],
        "error": {
            "error_code": ERROR_CODE['INPUT_DATA_ERROR'],
            "error_message": app.config['INPUT_DATA_ERROR']
        }
    }
#     except:
#         return {
#             "status": STATUS_CODE['ERROR'],
#             "error": {
#                 "error_code": ERROR_CODE['EXCEPTION'],
#                 "error_message": ERROR_CODE['EXCEPTION'],
#             }
#         }
    
    
@app.route("/api/auth/test")
async def auth_test(request):
    a = request_new_token()

    return json(None)


#
def get_app_key(**kw):
    try:
        config = db.session.query(Configuration.data['app_key']).filter().first()

        return to_dict(config)[0]
    except:
        return None


def get_contact_code_prefix(**kw):
    try:
        config = db.session.query(Configuration.data['contact_code_prefix']).filter().first()

        return to_dict(config)[0]
    except:
        return None
    
# AA1234, AA12345...
def get_contact_code_length(**kw):
    try:
        config = db.session.query(Configuration.data['contact_code_length']).filter().first()

        return to_dict(config)[0]
    except:
        return None


def get_score_config(**kw):
    try:
        config = db.session.query(Configuration.data['score']).filter().first()
        
        return to_dict(config)[0]
    except:
        return None


def allow_promotion_by_contact_info(**kw):
    try:
        config = db.session.query(Configuration.data['promotion_by_contact_info']).filter().first()
        return to_dict(config)[0]
    except:
        return False

def get_chatbot_integrating_info(**kw):
    try:
        config = db.session.query(Configuration.data['chatbot']).filter().first()
        
        return to_dict(config)[0]
    except:
        return None
    

def get_ipos_integrating_info(**kw):
    try:
        config = db.session.query(Configuration.data['ipos']).filter().first()
        
        return to_dict(config)[0]
    except:
        return None
    
    
def get_stringee_integrating_info(**kw):
    try:
        config = db.session.query(Configuration.data['stringee']).filter().first()
        
        return to_dict(config)[0]
    except:
        return None


def get_3nd_auth(app_key, **kw):
    today = datetime.now()
    connected_app = ConnectionApp.query.filter(and_(or_(ConnectionApp.expired_at == None,\
                                                         ConnectionApp.app_id == str(app_key),\
                                                         ConnectionApp.expired_at >= today),\
                                                     ConnectionApp.deleted == False)).first()
    
    return to_dict(connected_app)
    


def generate_number_id(num=16):
    code = ''.join(random.choice(string.digits) for _ in range(num))
    return code



def generate_hash_key(num=64, uppercase=True):
    code = ""
    
    if uppercase == True:
        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num))
    else:
        code = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(num))
        
    return code



def veridy_app_data(data=None, **kw):
    if data is not None:
        if 'app_id' in data and data['app_id'] is None:
            data['app_id'] = generate_number_id(16)
        if 'secret_key' in data and data['secret_key'] is None:
            data['secret_key'] = generate_hash_key(64, True)


##################################################################
########### START IMAGE UPLOAD                         ###########
##################################################################

imageupload = Blueprint('image', url_prefix='/image')

@imageupload.route('/')
async def bp_root(request):
    return json({'image': 'blueprint'})


@imageupload.route('/upload', methods=['POST'])
async def imgupload(request):
    ret = None
    url = app.config['IMAGE_SERVICE_URL']
    fsroot = app.config['FS_ROOT']
    if request.method == 'POST':
        file = request.files.get('image', None)
        if file :
            rand = ''.join(random.choice(string.digits) for _ in range(5))
            file_name = os.path.splitext(file.name)[0]
            extname = os.path.splitext(file.name)[1]
            newfilename = file_name + "-" + rand + "-" + get_local_today(7).timestamp() + "-" + extname
            
            async with aiofiles.open(fsroot + newfilename, 'wb+') as f:
                await f.write(file.body)

            ret = {
                "link": url  + "/" + newfilename  ,
                #"link": "/" + newfilename  ,
                "width": None,
                "height": None
            }
    return json(ret)

##################################################################
########### END IMAGE UPLOAD                           ###########
##################################################################




@app.route("/api/v1/configuration/save", methods=["OPTIONS", "POST"])
async def save_config(request):
    data = request.json
#     try:
    if data is None:
        return json({
            "error_code": ERROR_CODE['NULL_ERROR'],
            "error_message": ERROR_MSG['NULL_ERROR']
        }, status=STATUS_CODE['ERROR'])

    config = Configuration.query.filter().first()
    if config is None:
        config = Configuration()
    
    if config is not None and (config.app_key is None\
        or ('app_key' is data and data['app_key'] is not None and config.app_key == data['app_key'])):

        if config.app_key is None and 'app_key' in data and data['app_key'] is not None:
            config.app_key = data['app_key']
        if 'app_secret' in data and data['app_secret'] is not None:
            config.app_secret = data['app_secret']

    if 'category' in data and data['category'] is not None:
        config.category = data['category']
    if 'token' in data and data['token'] is not None:
        config.token = data['token']
    if 'data' in data:
        config.data = data['data']
        
    db.session.add(config)
    db.session.commit()

    return json({
        "message": "success"
    }, status=STATUS_CODE['OK'])
#     except:
#         return json({
#             "error_code": ERROR_CODE['EXCEPTION'],
#             "error_message": ERROR_MSG['EXCEPTION']
#         }, status=STATUS_CODE['ERROR'])
    


apimanager.create_api(Configuration,
    methods=['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix='/api/v1',
    preprocess=dict(GET_SINGLE=[verify_access],\
                    GET_MANY=[verify_access],\
                    POST=[verify_access],\
                    PUT_SINGLE=[verify_access]),
    collection_name='configuration')


apimanager.create_api(ConnectionApp,
    methods=['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix='/api/v1',
    preprocess=dict(GET_SINGLE=[verify_access],\
                    GET_MANY=[verify_access],\
                    POST=[veridy_app_data],\
                    PUT_SINGLE=[veridy_app_data]),
    collection_name='connection_app')


apimanager.create_api(Notify,
    methods=['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix='/api/v1',
    preprocess=dict(GET_SINGLE=[verify_access],\
                    GET_MANY=[verify_access],\
                    POST=[verify_access],\
                    PUT_SINGLE=[verify_access]),
    collection_name='notify')
