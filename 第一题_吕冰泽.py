import requests
import re
import json
import csv
import pandas as pd
import urllib.request

# 1.保存成htm文件
def getHtml(url):
 html = urllib.request.urlopen(url).read()
 return html

def saveHtml(file_name, file_content):
 # 注意windows文件命名的禁用符，比如 /
 with open(file_name.replace('/', '_') + ".html", "wb") as f:
  # 写文件用bytes而不是str，所以要转码
  f.write(file_content)

aurl = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4"
html = getHtml(aurl)
saveHtml(r'/sduview', html)

print("下载成功")


# 2 获取疫情信息
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('_sduview.html', encoding='utf-8'), features='html.parser')  # features值可为lxml
print(soup)

# 3 存为CSV

headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
        }
url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4'

#发送请求

response=requests.get(url=url,headers=headers)

#数据解析

data_html=response.text
print(data_html)

#【0】转换数据类型从list到str,强大的正则

json_str=re.findall('"component":\[(.*)\],',data_html)[0]
#print(json_str)
#转换字典

json_dict=json.loads(json_str)

caseList=json_dict['caseList']
print(caseList)
for case in caseList:

    area=case['area']#

    confirmed=case['confirmed']#

    curConfirm=case['curConfirm']

    asymptomatic=case['asymptomatic']

    crued=case['crued']#

    died=case['died']#

    confirmedRelative=case['confirmedRelative']

    diedRelative=case['diedRelative']

    curedRelative=case['curedRelative']

    asymptomaticRelative=case['asymptomaticRelative']

    nativeRelative=case['nativeRelative']

    overseasInputRelative=case['overseasInputRelative']

#打印检查  print(area,confirmed,curConfirm,confirmedRelative,nativeRelative,overseasInputRelative, asymptomatic,asymptomaticRelative,crued,curedRelative,died,diedRelative)

#写入表格

with open('./data.csv',mode='a',encoding='utf-8',newline='')as f:

        csv_writer=csv.writer(f)

        csv_writer.writerow([area,confirmed,curConfirm,confirmedRelative,nativeRelative,overseasInputRelative,asymptomatic,asymptomaticRelative,crued,curedRelative,died,diedRelative])

