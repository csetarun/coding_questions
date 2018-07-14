import json
import requests
events_endpoint = settings.SKEDOOL_EXCHANGE_SERVICE.strip('/') + '/calendarEvents'
def post_data(email, action):
        '''
        this function returns a dictionary containing basic required parameters
        for making a post call to the exchange mailbox service endpoint
        '''
        email_object = Assistant.objects.get(email = email)
        creds =  email_object.creds
        details = json.loads(creds.credentials)
        # logger.debug(details.keys())
        password = details['encrypted_data']
        encryption_key = details['encryption_key']
        username = creds.exchange_username
        auto_discover_url = creds.exchange_url
        data = {
        'userName' : username,
        'password' : password,
        'encryptionKey': encryption_key,
        'autoDiscoverURL' : auto_discover_url,
        'action' : action,
        }
        return data

data = post_data('alex.powwow@alexbox.info','create')
event_data = {'start':'2018-03-1213:04:42',
            'end':'2018-03-1213:10:42',
            'location':'Hyd',
            'description':'Nothing',
            'emailIDs':['tarun.k@myally.ai'],
            'title':'Testing Attachments',
            'timezone':'IST',
            'messageID':'AAMkAGJjMDYyY2MyLTAzNDUtNDUzOC1hMzMyLTdmNGY2ZWY2NDUyYQBGAAAAAABtvMYy8bXjQoSUjsVWPmIRBwCKcIeutmzLT5mbuNLg79kPAAAAAAEMAACKcIeutmzLT5mbuNLg79kPAACMg0HDAAA=',
            'attachmentID':'AAMkAGJjMDYyY2MyLTAzNDUtNDUzOC1hMzMyLTdmNGY2ZWY2NDUyYQBGAAAAAABtvMYy8bXjQoSUjsVWPmIRBwCKcIeutmzLT5mbuNLg79kPAAAAAAEMAACKcIeutmzLT5mbuNLg79kPAACMg0HDAAABEgAQAAS+GDno3GpOhDYwCS9dZfg=',
            'organizer':'tarun.k@myally.ai'
}
data.update(event_data)
response = requests.post(events_endpoint, data=data).json()
print response