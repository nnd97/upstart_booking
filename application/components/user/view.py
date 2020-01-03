import time
import json as json_load
import requests
from sqlalchemy import and_, or_
from gatco.response import json, text, html
from application.extensions import apimanager
from application.extensions import auth
from application.database import db
from application.server import app
from gatco_restapi.helpers import to_dict
from application.components.base.view import verify_access
# from application.common.constants import STATUS_CODE, ERROR_CODE, ERROR_MSG
from application.components import User, Permission, Role
# Configuration,  Workstation,, Tenant
# import view
# from application.components.tenant.view import get_tenant


if app.config.get("DEVELOPMENT_MODE", False) is not True:
    @auth.user_loader
    def user_loader(token):
        if token is not None:
            if 'exprire' in token:
                if token['exprire'] < time.time():
                    return None
                del(token["exprire"])
            return token
        return None
else:
    @app.route('/login', methods=['POST'])
    async def login(request):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        user = db.session.query(User).filter(and_(or_(User.user_name == username, User.email == username), User.active == True)).first()
        if (user is not None) and auth.verify_password(password, user.password):
            auth.login_user(request, user)
            return json(get_user_with_permission(to_dict(user)))
        return json({"error_code":"LOGIN_FAILED","error_message":"user does not exist or incorrect password"}, status=501)


@app.route('/logout')
async def logout(request):
    try:
        auth.logout_user(request)
    except:
        pass
    return json({})


def get_user_with_permission(user_info):

    user = User.query.filter(or_(User.id == user_info.get('id', None), User.phone == user_info.get('phone', None))).first()

    if user is None:
        user = User()
        user.id = user_info["id"]
        user.phone = user_info['phone']
        user.email = user_info['email']
        user.user_image = user_info['avatar_url'] if 'avatar_url' in user_info else None
        user.display_name = user_info['display_name'] if ('display_name' in user_info) else None
        role = None
        if 'tenant_role' in user_info and user_info['tenant_role'] == "admin":
            role = db.session.query(Role).filter(Role.role_code == 0).first()
            if role is None:
                role = Role()
                role.role_code = 0
                role.role_name = "admin"
                role.display_name = "Admin"
        else:
            role = db.session.query(Role).filter(Role.role_code == 1).first()
            if role is None:
                role = Role()
                role.role_code = 1
                role.role_name = "user"
                role.display_name = "User"

        user.roles.append(role)
        db.session.add(user)
        db.session.commit()

    insystem_user = to_dict(user)

#     roles = [{"id":str(role.id),"display_name":role.display_name,"role_name":role.role_name} for role in user.roles]
#     roleids = [role.id for role in user.roles]
#     user_info["roles"] = roles
#     
#     #permission:
#     perms = Permission.query.filter(Permission.role_id.in_(roleids)).order_by(Permission.subject).all()
#     permobj = {}
#     
#     for perm in perms:
#         if perm.subject not in permobj:
#             permobj[perm.subject] = {}
#             
#         if perm.permission not in permobj[perm.subject]:
#             permobj[perm.subject][perm.permission] = perm.value
#         elif not permobj[perm.subject][perm.permission]:
#             permobj[perm.subject][perm.permission] = perm.value        
#     user_info["permission"] = permobj
#     
#     #division:
#     workstations = None
#     if user.has_role("Admin"):
#         workstations = [to_dict(restaurant) for restaurant in Workstation.query.all()]
#     else:
#         workstations = [to_dict(restaurant) for restaurant in user.workstations]
#     
#     user_info["workstations"] = workstations


    return insystem_user


@app.route('/current-user')
async def get_current_user(request):
    return json({
        'id':"06064fb7-baf0-4d76-ac34-b5d59b238eb3",
        'email':'test@gmail.com',
        'phone':'0329090667',
        'display_name':'nguyen ngoc dat',
        'created_at':'578667'
    })
    # current_user = auth.current_user(request)
    # print ("current_user ", current_user)
    # if current_user is not None:

    #     # CHECK THAT CURRENT USER HAVE PERMISSION TO ACCESS APP
    #     if 'tenants' in current_user and isinstance(current_user['tenants'], list):
    #         flag = False
    #         current_tenant = get_tenant()
    #         for _ in current_user['tenants']:
    #             if _['id'] == app.config['TENANT_ID']:
    #                 if current_tenant is None:
    #                     tenant = Tenant()
    #                     tenant.tenant_no = _['id']
    #                     tenant.tenant_name = _['tenant_name']
    #                     tenant.tenant_image = _['image_url']
    #                     db.session.add(tenant)
    #                     db.session.commit()

    #                 current_user['tenant_role'] = _['role']
    #                 flag = True

    #     if flag == False:
    #         return json({
    #             "error_code": ERROR_CODE['TOKEN_ERROR'],
    #             "error_message": ERROR_MSG['TOKEN_ERROR']
    #         }, status=STATUS_CODE['AUTH'])
        
        
    #     user_info = get_user_with_permission(current_user)
            
    #     if user_info is not None:
    #         return json(user_info)
        
    #     else:
    #         return json({
    #             "error_code": ERROR_CODE['NOT_FOUND'],
    #             "error_message": "User does not exist"
    #         }, status = STATUS_CODE['NOT_FOUND'])

    # return json({
    #     "error_code": ERROR_CODE['NOT_FOUND'],
    #     "error_message":"User does not exist"
    # }, status = STATUS_CODE['NOT_FOUND'])
    
    
# @app.route('/user/change-password', methods=["POST"])
# async def change_password(request):
#     error_msg = None
#     currentUser = current_user(request)
#     if currentUser is not None:
#         data = request.json
#         
#         if data['user_password'] != data['confirm_password']:
#             return json({"error_message": "Mật khẩu nhập lại không khớp", "error_code": "NOT_MARK"}, status= 520)
#         
#         if data is not None:
# #             if data['id'] is not None and data['id'] != currentUser.id:
# #                 return json({"error_message": "Session Error", "error_code": "NOT_MARK"}, status= 520)
#             
#             user = User.query.filter(User.id == data['id']).first()
#             if user is None:
#                 return json({"error_message": "User is not found", "error_code": "NOT_FOUND"}, status= 520)
#             
#             if auth.verify_password(data['password'], user.user_password) != True:
#                 return json({"error_message": "Password is not correct", "error_code": "NOT_CORRECT_PASSWORD"}, status= 520)
#             
#             user.user_password = auth.encrypt_password(data['user_password'])
#             
#             db.session.add(user)
#             db.session.commit()
#             return json({"message": "success"})
#     else:
#         error_msg = "User does not exist"
#         return json({
#             "error_code": "USER_NOT_FOUND",
#             "error_message":error_msg
#         }, status = 520)


@app.route("/api/v1/user/attrs", methods=["PUT", "OPTIONS"])
async def update_properties(request):
    verify_access(request)
    
    if request.method == "OPTIONS":
        return json(None)
    try:
        data = request.json
        if data is None or 'id' not in data or data['id'] is None:
            return json({"error_code": ERROR_CODE['DATA_FORMAT'], "error_message": ERROR_MSG['DATA_FORMAT']}, status=STATUS_CODE['ERROR'])
         
        contact = User.query.get(data['id'])
        if contact is not None:
            for name, value in data.items():
                if name != 'id':
                    setattr(contact, name, value)

            db.session.add(contact)
            db.session.commit()
            
            return json({"message": "success"})
    except:
        return json({"error_code": ERROR_CODE['EXCEPTION'], "error_message": ERROR_MSG['EXCEPTION']}, status=STATUS_CODE['ERROR'])



@app.route("/api/v1/verify-info", methods=["OPTIONS", "GET"])
async def verify_info(request):
    if request.method == "OPTIONS":
        return "OK"
    
    configuration = Configuration.query.filter().first()
    
    if configuration is not None and (configuration.app_key is None or configuration.app_secret is None):
#         try:
#             headers = {
#                 'content-type': 'application/json'
#             }
#             data = {
#                 "tenant_id": app.config['TENANT_ID'],
#                 "app_type": app.config['APP_TYPE'].lower()
#             }
#             response = requests.post(app.config['APP_INFO_API'], data=json_load.dumps(data), headers=headers)
#             print ("VERIFY-INFO STATUS: ", response.status_code)
#             if response.status_code == STATUS_CODE['OK']:
#                 res = to_dict(response.json())
#                 configuration.app_key = res['appkey']
#                 configuration.app_secret = res['appsecret']
#                 db.session.add(configuration)
#                 db.session.commit()
#             else:
#                 print ("ERROR: APP_INFO_API", response.status_code)
#                 return json({
#                     "error_code": response.status_code,
#                     "error_message": app.config['APP_INFO_API']
#                 }, status=STATUS_CODE['ERROR'])
#         except:
#             return json({
#                 "error_code": ERROR_CODE['EXCEPTION'],
#                 "error_message": ERROR_CODE['EXCEPTION'],
#             }, status=STATUS_CODE['ERROR'])
        return json({
            "error_code": ERROR_CODE['NOT_FOUND'],
            "error_message": ERROR_MSG['NOT_FOUND']
        }, status=STATUS_CODE['ERROR'])

    else:
        # PING ACCOUNT TO UPDATE SOME CHANGES
        pass

    return json({
        "message": "OK"
    }, status=STATUS_CODE['OK'])


@app.route("/api/v1/user/entry", methods=["OPTIONS", "POST", "PUT"])
async def user_wekhook(request):
    if request.method == "OPTIONS":
        return text("OK")
    
    data = request.json
    if data is not None:

        objectData = data['data'] if 'data' in data else None
        if data is not None:
            user = None
            if objectData is not None:
                if 'instance_id' in data and data['instance_id'] is not None:
                    user = User.query.get(data['instance_id'])
                
                if user is None:
                    # CREATE NEW USER
                    user = User()
                    user.id = data['instance_id']

                user.phone = objectData['phone']
                user.display_name = objectData['display_name'] if 'display_name' in objectData else None
                user.email = objectData['email'] if 'email' in objectData else None
                user.birthday = objectData['birthday'] if 'birthday' in objectData else None
                if 'deleted' in objectData:
                    user.deleted = objectData['deleted'] if 'deleted' in objectData else False
                user.roles = []
                if 'role' in objectData and objectData['role'] is not None:
                    if objectData['role'] == 'user':
                        role = Role.query.filter(Role.role_name == 'user').first()
                        if role is None:
                            role = Role()
                            role.role_name = "user"
                            role.display_name = "User"
                        user.roles.append(role)
                    elif objectData['role'] == 'admin':
                        all_users = User.query.filter(User.deleted == False).all()
                        role_name = None
                        role_display = None
                        if len(all_users) == 0:
                            role_name = "admin"
                            role_display = "Admin"
                        else:
                            role_name = "workstation-admin"
                            role_display = "Workstaion Admin"
                        role = Role.query.filter(Role.role_name == role_name).first()
                        if role is None:
                            role = Role()
                            role.role_name = role_name
                            role.display_name = role_display
                        user.roles.append(role)
    
                db.session.add(user)
                db.session.commit()
    
    return json({"message": "success"})



apimanager.create_api(User,
    methods=['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix='/api/v1',
    preprocess=dict(GET_SINGLE=[verify_access],
                    GET_MANY=[verify_access],
                    POST=[verify_access],
                    PUT_SINGLE=[verify_access]),
    exclude_columns = ['password'],
    collection_name='user')

apimanager.create_api(Role,
    methods=['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix='/api/v1',
    preprocess=dict(GET_SINGLE=[verify_access],
                    GET_MANY=[verify_access],
                    POST=[verify_access],
                    PUT_SINGLE=[verify_access]),
    collection_name='role')

apimanager.create_api(Permission,
    methods=['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix='/api/v1',
    preprocess=dict(GET_SINGLE=[verify_access],
                    GET_MANY=[verify_access],
                    POST=[verify_access],
                    PUT_SINGLE=[verify_access]),
    collection_name='permission')
