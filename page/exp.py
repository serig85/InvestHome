import json


impath = '../static/image/dtjxK5Y9Bt8.jpg'
im_file_name = impath.split('/')[-1]

datadict = {'fist_name':'Serg',
            'last_name':'Sper',
            'email'    :'test@test.te',
            'gender'   :'male',
            'mobile_num': '0123456789',
            'date_of_birch': '8 Jan 1985',
            'hobbies'   :['sport', 'music'],
            'subjects':"subg_text",
            'file_name':im_file_name}
print(datadict)

print(type(datadict))
jsdata = json.dumps(datadict)
print(type(jsdata))
print(jsdata)
rejs = json.loads(jsdata)
print(type(rejs))
print(rejs['fist_name'])