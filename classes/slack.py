import requests, os, yaml

class slack():

    PWD = os.getenv("HOME")
  
    with open("%s/.python_auth_cfg.yml" % PWD, 'r') as auth:
        auth_conf = yaml.load(auth, Loader=yaml.FullLoader)

    def __init__(self):

        try:
            auth_data = slack.auth_conf['slack']

            self.token      =  auth_data['api_token']
            self.namespace  =  auth_data['name_space']
            self.api_url    = 'https://%s.slack.com/api' % self.namespace

            self.command    = {
                                'user_list'     : '%s/users.list' % self.api_url,
                                'user_inactive' : '%s/users.admin.setInactive' % self.api_url,
                                'users_invite'  : '%s/users.admin.invite' % self.api_url
                            }
        except KeyError as error:
            print('slack.init | Error <%s>' % error )

    def user_invite(self, **data_account):
        
        data_account_create = {
                               'email'     : data_account['email'],
                               'first_name': data_account['first_name'],
                               'last_name' : data_account['last_name'],
                               'token'     : self.token,
                               'set_active': "true",
                               'resend'    : "true"
                               }

        r = requests.post(self.command['users_invite'], data = data_account_create)
        print('slack.init | <%s | %s>' % (r.status_code, r.json()))

    def user_inactive(self, username):

        data_accounts  =    {
                            'token'     : self.token,
                            }

        r  = requests.post(self.command['user_list'], data = data_accounts)

        members                 = r.json().get('members')

        for user in members:

            user_id         = user.get('id')
            status          = user.get('deleted') 
            email           = user.get('profile').get('email')

            try:
                user_name   = email.split('@')[0]

            except AttributeError or IndexError or KeyError as error:
                print('slack.init.user_inactive |','{:<15} | {}'.format(user_name, error))
 
            if user_name == username and status == False:
                
                data_account_inactive   =   {
                                             'token' : self.token,
                                             'user'  : user_id
                                             }

                r = requests.post(self.command['user_inactive'], data=data_account_inactive)
                print('slack.init.user_inactive |','{:<15} | {}'.format(user_name, r.json()))
                