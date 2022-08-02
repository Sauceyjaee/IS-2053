from asyncio.windows_events import NULL


def companyRegistry(name, attribute):
    employeeDictionary = { "employees": {
        "John Appletree": 
        {   
            "Salary": "$100,000",
            "Title": "Chief Information Officer",
            "Home Address": "7654 Criple Lane. \nSan Antonio TX 78249",
            "Contact Info": "512-422-9847"
        }
        ,
        "Jae Hill": 
        {
            "Salary": "$10,000,000",
            "Title": "CEO",
            "Home Address": "3457 Intel Blvd. \nMilwaukee WI 53216",
            "Contact Info": '414-479-6349'
        }
        ,
        "Liyah Latiker": 
        {   
            "Salary": "$45,000",
            "Title": "Janitor",
            "Home Address": "3178 Louneck st. \nSan Antonio TX 78249",
            "Contact Info": "512-422-9847"
        }
        ,
        "Darien Robert": 
        {
            "Salary": "$97,000",
            "Title": "Store Manager",
            "Home Address": "7345 Stockbrook. \nDallas TX 64392",
            "Contact Info": '414-279-4386'
        }
        ,
    }
    }
    #if name in employeeDictionary['employees']:
    """
    1. if I get a KeyError when calling an attribute, how can i differntiate it from a key error with the employee name?
    2. How can I make my dictionary case insensitive?
    """
    return (employeeDictionary["employees"][name][attribute])
    """"
    
    try:
        return (employeeDictionary["employees"][name][attribute])
    except KeyError:
        print ('Employee Name or desired criteria not found')
        ans = input('Would you like to try again?: ')
        if ans.lower() == 'yes' or ans.lower() == 'y':
            main()
        else:
            print('Bye')
            quit()
    """


