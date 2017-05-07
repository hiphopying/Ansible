def ipsplit(ip):
    lst = str(ip).split('.')
    if len(lst[2]) < 3:
        lst[2] = "0" + lst[2]
    if len(lst[3]) < 3:
        lst[3] = "0" + lst[3]

    return lst


class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''
    def filters(self):
        return {
            'ipsplit': ipsplit
        }
