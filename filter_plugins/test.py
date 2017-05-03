def ipsplit(ip):
    return str(ip).split('.')

class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''
    def filters(self):
        return {
            'ipsplit': ipsplit
        }
