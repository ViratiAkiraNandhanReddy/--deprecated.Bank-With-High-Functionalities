import json
# bytes('Aki',encoding='UTF-16')
myDict = {'Virati Akira Nandhan Reddy':{
    'Password':'Viratiaki@Ai@GoogleAi',
    'Email':'viratiaki53@gmail.com',
    'Security Code':'Viratiaki@Akki',
    'Balance':19724228629,
    'Dark Mode':True,
    'Email Verified':False,
    'Account Type':'Gold',
    'isActive':True,
    'Created On':'22-Jan-2025 12:52 AM',
    'Loan':{
        'Interest':0,
        'Lend Amount':0,
        'Total Available':10E6,
        'Taken On':'12-Jan-2025 07:52 PM',
        'Repaid':True,
        'Repaid On':'02-Feb-2025 01:45 PM',
        'Interest To Bank':0
    },
    'Last Five Transactions':{
        '02-Jan-2025 06:02 PM':'500 Deposit',
        '01-Jan-2025 12:52 AM':'300 Deposit',
        '31-Dec-2024 01:15 PM':'700 Deposit'

    }
    
},
    'Akira Nandhan Reddy':{
    'Password':'Viratiaki@Ai@GoogleAi',
    'Email':'viratiaki53@gmail.com',
    'Security Code':'Viratiaki@Akki',
    'Balance':19724228629,
    'Dark Mode':True,
    'Email Verified':False,
    'Account Type':'Gold',
    'isActive':True,
    'Created On':'22-Jan-2025 12:52 AM',
    'Loan':{
        'Interest':0,
        'Lend Amount':0,
        'Total Available':10E6,
        'Taken On':'12-Jan-2025 07:52 PM',
        'Repaid':True,
        'Repaid On':'02-Feb-2025 01:45 PM',
        'Interest To Bank':0
    },
    'Last Five Transactions':{
        '02-Jan-2025 06:02 PM':'500 Deposit',
        '01-Jan-2025 12:52 AM':'300 Deposit',
        '31-Dec-2024 01:15 PM':'700 Deposit'

    }
}}
print(myDict)
with open(r'Bank_Package\User_Data.json','w') as Data:
    json.dump(myDict,fp=Data,indent=4)
    # Data.write(dat)

# print(json.dumps(myDict,indent=4))

with open(r'Bank_Package\User_Data.json','r') as Data:
    data = json.load(Data)
    print(type(data))

bank = {'isActivated':True,'Manager Name':'Virati Akira Nandhan Reddy','Downloaded On':'12-Dec-2025 01:52 PM',
        'Path Of User Data':r'D:\GitHub\Bank-With-High-Functionalities\Bank_Package\User_Data.json',
        'License Check':True,'Recently Used On':'22-Feb-2025 4:53 PM'}
with open(r'Bank_Package\Bank Initialization.json','w') as Dat:
    json.dump(bank,Dat,indent=4)

    
