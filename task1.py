
def format_postcode(postcode):
    '''Converts integer into the postcode, by adding dash after 2 digits'''
    postcode = '{}-{}'.format(str(postcode)[:2],str(postcode)[2:])
    return postcode

def postcodes_generator(start,end):
    '''Returns the list of postcodes in between start and end postcodes passed as arguments'''
    start = int(start.replace('-', ''))
    end = int(end.replace('-',''))
    postcodes_between = [format_postcode(postcode) for postcode in range(start+1, end)]
    return postcodes_between

print(postcodes_generator("79-900", "80-155"))