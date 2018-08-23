import os
import json
import pandas as pd
data = os.listdir('../data')
for x in data:
    if not x.isdigit():
        data.remove(x)

data.remove('rename.py')

# count = 0
# folders = ['01', '02', '24', '25', '26', '27', '28', '29', '30', '31']
# for folder in folders:
#     print('*' * 20, folder, '*' * 20)
#     for file in os.listdir('../data/' + folder):
#         print('-' * 15, '-' * 15, '\n')
#         print('../data/{}/{}'.format(folder, file))
#         print('-' * 15, '-' * 15, '\n')
#         count += 1
#         # os.rename(input_file, output_file)
# print(count)
# f = open('profile.json')
# data = f.read()
# profiles = json.loads(data)
# for profile in profiles:
#     tid = profile['id']
#     file = open('../output/'+tid + '.txt', 'w')
#
# file.close()
# f.close()
def read_files():
    folders = ['01', '02', '24', '25', '26', '27', '28', '29', '30', '31']
    count=0
    for folder in folders:
        print('*' * 20+ folder+ '*' * 20)
        path='../data/' + folder
        for file in os.listdir(path):
            if file.find('.txt')!=-1:
                file_loc=path+'/'+file
                print 'Reading file:- ',file
                f=open(file_loc)
                data=f.read()
                data=json.loads(data)
                df=pd.DataFrame(data)
                print df.columns
                print df.head()
                count+=1
    print count
read_files()

