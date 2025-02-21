import json
# bytes('Aki',encoding='UTF-16')
myDict = {'Aki': {'Password':str(bytes('Aki',encoding='UTF-16')),'Email':'viratiaki53','Security_Code':'kdhbvkvhdb','Balance':123456765432,'isDark':False,'Loan':10E5,'isPrimum':None},
          'Developer': {'Password':'dev','Email':'dev@433','Security_Code':'kdhbvk6444b','Balance':123456765432,'isDark':True,'Loan':10E5,'isPrimum':None},
          'Virati Akira Nandhan Reddy':{'Password':'alfdtauy','Email':'akifh@khg','Security_Code':'katsfajd57','Balance':123456765432,'isDark':True,'Loan':10E5,'isPrimum':None},
          'Akira Nandhan Reddy':{'Password':'akaytdsuy','Email':'argfsfd','Security_Code':'katspiyafduofsa','Balance':123456765432,'isDark':True,'Loan':10E5,'isPrimum':None},
          'jyufduyfdfddfeydfeuyfdyefdffdfddfdjfjfadfsgjadasg':{'Password':'akaytdsuy','Email':'argfsfd','Security_Code':'katspiyafduofsa','Balance':123456765432,'isDark':True,'Loan':10E5,'isPrimum':None}}

with open(r'Bank_Package\User_Data.json','w') as Data:
    json.dump(myDict,fp=Data,indent=4)
    # Data.write(dat)

# print(json.dumps(myDict,indent=4))

with open(r'Bank_Package\User_Data.json','r') as Data:
    data = json.load(Data)
    print(type(data))



    
