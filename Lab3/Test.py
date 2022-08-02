"""""
def database():
    datastore = { "office": {
        "medical": [
        { "room-number": 100,
            "use": "reception",
            "sq-ft": 50,
            "price": 75
        },
        { "room-number": 101,
            "use": "waiting",
            "sq-ft": 250,
            "price": 75
        },
        { "room-number": 102,
            "use": "examination",
            "sq-ft": 125,
            "price": 150
        }
        ],
        "parking": {
        "location": "premium",
        "style": "covered",
        "price": 750
        }
    }
    }
    print (datastore["office"]["parking"]['location'])
    for item in datastore['office']['medical']: # This loop shows the change is not only in books, but is also in database
        if item.get('use') == "examination" :
            print ('The {} rooms now cost {}'.format(item.get("use"), item.get("price")))
if __name__== '__main__':
    database()

"""
def companyRegistry(name, attribute):
    employeeDictionary = { "employees": {
        "John Appletree": 
        {   
            "salary": 100,
            "Title": "Chief Information Officer",
            "Home Address": '7654 Criple Lane',
            "Contact Info": '512-422-9847'
        }
        ,
        "Jae": 
        {
            "salary": 100,
            "title": "reception",
            "home address": 50,
            "contact Info": '512-422-9848'
        }
    }
    }
   # 
    #if name in employeeDictionary['employees']:
    """
    str1 = "Hello"
    str2 = "HELLO"

    if str1.lower() == str2.lower():
        print('Both Strings are same')
    else:
        print('Strings are not same')
    """
    try:
        if name in employeeDictionary.lower():
            return (employeeDictionary["employees"][name.lower()][attribute])
    except:
        print ('Employee Name not found')
        print(employeeDictionary["employees".lower()])
def main():
    employeeName = input('Enter Employee Name: ')
    desiredField = input('Enter desired Field: ')
    pass

if __name__ == "__main__":
    employeeName = input('Enter Employee Name: ')
    desiredField = input('Enter desired Field: ')

    ans = companyRegistry(employeeName.lower(), desiredField.lower())
    print (ans)


