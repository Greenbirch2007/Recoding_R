#-*- coding:utf-8 -*-



'''
Bayesian=[]
ChemPhys=[]
ClinicalTrials=[]
Cluster=[]
DifferentialEquations=[]
Distributions=[]
Econometrics=[]
Environmetrics=[]
ExperimentalDesign=[]
ExtremeValue=[]
Finance=[]
FunctionalData=[]
Genetics=[]
Graphics=[]
HighPerformanceComputing=[]
MachineLearning=[]
MedicalImaging=[]
MetaAnalysis=[]
ModelDeployment=[]
Multivariate=[]
NaturalLanguageProcessing=[]
NumericalMathematics=[]
OfficialStatistics=[]
Optimization=[]
Pharmacokinetics=[]
Phylogenetics=[]
Psychometrics=[]
ReproducibleResearch=[]
Robust=[]
SocialSciences=[]
Spatial=[]
SpatioTemporal=[]
Survival=[]
TimeSeries=[]
WebTechnologies=[]
gR=[]

'''

# 解析的部分

# url ="https://cloud.r-project.org/web/views/"


# 获取所有链接的请求
# def get_all_links(url):
# 	response = requests.get(url,timeout=10)
# 	return response.text

# 这个地方尝试使用bs4
# html = get_all_links(url)
# patt = re.compile('<td><a href=".*?">(.*?)</a></td>')
# items = re.findall(patt,html)
# for i in items:
# 	print('https://cloud.r-project.org/web/views/'+i + '.html')


# 下载的主题url列表
import time

"""
https://cloud.r-project.org/web/views/Bayesian.html
https://cloud.r-project.org/web/views/ChemPhys.html
https://cloud.r-project.org/web/views/ClinicalTrials.html
https://cloud.r-project.org/web/views/Cluster.html
https://cloud.r-project.org/web/views/DifferentialEquations.html
https://cloud.r-project.org/web/views/Distributions.html
https://cloud.r-project.org/web/views/Econometrics.html
https://cloud.r-project.org/web/views/Environmetrics.html
https://cloud.r-project.org/web/views/ExperimentalDesign.html
https://cloud.r-project.org/web/views/ExtremeValue.html
https://cloud.r-project.org/web/views/Finance.html
https://cloud.r-project.org/web/views/FunctionalData.html
https://cloud.r-project.org/web/views/Genetics.html
https://cloud.r-project.org/web/views/Graphics.html
https://cloud.r-project.org/web/views/HighPerformanceComputing.html
https://cloud.r-project.org/web/views/MachineLearning.html
https://cloud.r-project.org/web/views/MedicalImaging.html
https://cloud.r-project.org/web/views/MetaAnalysis.html
https://cloud.r-project.org/web/views/ModelDeployment.html
https://cloud.r-project.org/web/views/Multivariate.html
https://cloud.r-project.org/web/views/NaturalLanguageProcessing.html
https://cloud.r-project.org/web/views/NumericalMathematics.html
https://cloud.r-project.org/web/views/OfficialStatistics.html
https://cloud.r-project.org/web/views/Optimization.html
https://cloud.r-project.org/web/views/Pharmacokinetics.html
https://cloud.r-project.org/web/views/Phylogenetics.html
https://cloud.r-project.org/web/views/Psychometrics.html
https://cloud.r-project.org/web/views/ReproducibleResearch.html
https://cloud.r-project.org/web/views/Robust.html
https://cloud.r-project.org/web/views/SocialSciences.html
https://cloud.r-project.org/web/views/Spatial.html
https://cloud.r-project.org/web/views/SpatioTemporal.html
https://cloud.r-project.org/web/views/Survival.html
https://cloud.r-project.org/web/views/TimeSeries.html
https://cloud.r-project.org/web/views/WebTechnologies.html
https://cloud.r-project.org/web/views/gR.html
"""



import requests
import re
from lxml import etree



# 设置一个全局变量 全局变量不能遍历？
# themes = ['Bayesian', 'ChemPhys', 'ClinicalTrials', 'Cluster', 'DifferentialEquations', 'Distributions', 'Econometrics', 'Environmetrics', 'ExperimentalDesign', 'ExtremeValue', 'Finance', 'FunctionalData', 'Genetics', 'Graphics', 'HighPerformanceComputing', 'MachineLearning', 'MedicalImaging', 'MetaAnalysis', 'ModelDeployment', 'Multivariate', 'NaturalLanguageProcessing', 'NumericalMathematics', 'OfficialStatistics', 'Optimization', 'Pharmacokinetics', 'Phylogenetics', 'Psychometrics', 'ReproducibleResearch', 'Robust', 'SocialSciences', 'Spatial', 'SpatioTemporal', 'Survival', 'TimeSeries', 'WebTechnologies', 'gR']
# for theme in themes:
#     yield theme
#
# url ='https://cloud.r-project.org/web/views/' + str(theme) + '.html'
# print(url)

# proxies = {"https":"https://125.122.116.46"}

#传入url,获取响应  代码改进，如果出现链接中断异常，再次请求即可（从中断的地方）
def get_one_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre'
    }
    response = requests.get(url)
    html =response.text
    return html

#解析pdf文件的下载地址
def parse_one_page(html):
    selector=etree.HTML(html)
    names = selector.xpath("/html/body/ul[1]/li//text()")
    for i in names:
        pdf_link ="https://cloud.r-project.org/web/packages/"+  i+ "/" + i + ".pdf"
        yield pdf_link

# pdf 文件下载
def getFile(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("/home/lk/Documents/R_Graphics/%s .pdf"  %url.split("/")[-1][0:-4], "wb") as f:  # 切片之后优化了命名
            f.write(response.content)
            f.close()
    else:
        pass


if __name__ == "__main__":
    url = 'https://cloud.r-project.org/web/views/Graphics.html'
    html = get_one_page(url)
    link = parse_one_page(html)
    for i in link:
        getFile(i)
        time.sleep(1)
    print("下载完成")


