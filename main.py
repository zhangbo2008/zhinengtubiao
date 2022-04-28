#


'''数据样式:



输入:

	用户id
	全列:
		订单日期,市场类别,区域,产品类别,产品名称,预计毛利
		时间	, 字符串, 字符串, 字符串, 字符串, 数值
		4       ,2      ,2      ,    2   ,2     ,10           (去重之后有多少个)
输出:
	产品类别 预计毛利 (2或3)
	50个图里面一个(图的名)  id: 0-49


-------------
输入:

	用户id
	全列:
		订单日期,市场类别,区域,产品类别,产品名称,预计毛利
		时间	, 字符串, 字符串, 字符串, 字符串, 数值
		4       ,2      ,2      ,    2   ,2     ,10           (去重之后有多少个)
输出:
	产品类别 预计毛利 (2或3)
	50个图里面一个(图的名)  id: 0-49






'''



dummy_input=[
    'aaa',
    ['订单日期','time',4],
    ['市场类别','string',2],
    ['区域','string',2],
    ['产品类别','string',2],
    ['产品名称','string',2],
    ['预计毛利','num',10],

]         #解释:0是用户id,输入的是表的所有字段, 每一个字段有3个属性, 列名, 类别,去重后有多少个.

dummy_output=[
    ['产品类别', '预计毛利']
    ,'饼状图'
]



#柱状图
import sqlite3

cx = sqlite3.connect( " 1.db " )





dummy_input_str=str(dummy_input)
#调用时候eval就可以反序列化.
import pandas as pd

dict1={'input':[dummy_input_str ],'output':[str(dummy_output)]}
aaa=pd.DataFrame(dict1)
try:
    aaa.to_sql('data',cx,index=False)
except:
    pass

print(1)






def reset_db():

    dummy_input1 = [
        '1001',
        ['订单日期', 'time', 4],
        ['市场类别', 'string', 2],
        ['区域', 'string', 5],
        ['产品类别', 'string', 5],
        ['产品名称', 'string', 20],
        ['预计毛利', 'num', 10],

    ]  # 解释:0是用户id,输入的是表的所有字段, 每一个字段有3个属性, 列名, 类别,去重后有多少个.

    dummy_output1 = [
        ['产品类别', '预计毛利']
        , '饼状图'

    ]


    dummy_input2 = [
        '1002',
        ['订单日期', 'time', 4],
        ['市场类别', 'string', 2],
        ['区域', 'string', 5],
        ['产品类别', 'string', 20],
        ['产品名称', 'string', 20],
        ['预计毛利', 'num', 10],

    ]  # 解释:0是用户id,输入的是表的所有字段, 每一个字段有3个属性, 列名, 类别,去重后有多少个.

    dummy_output2 = [
        ['产品类别', '预计毛利']
        , '折线图'

    ]


    dummy_input3 = [
        '1003',
        ['订单日期', 'time', 4],
        ['市场类别', 'string', 2],
        ['区域', 'string', 5],
        ['产品类别', 'string', 20],
        ['产品名称', 'string', 20],
        ['预计毛利', 'num', 10],
        ['预计利润', 'num', 10],

    ]  # 解释:0是用户id,输入的是表的所有字段, 每一个字段有3个属性, 列名, 类别,去重后有多少个.

    dummy_output3 = [
        ['产品类别', '预计利润', '预计毛利']
        , '折线图'

    ]


    dummy_input4 = [
        '1004',
        ['订单日期', 'time', 20],
        ['市场类别', 'string', 2],
        ['区域', 'string', 5],
        ['产品类别', 'string', 20],
        ['产品名称', 'string', 20],
        ['预计毛利', 'num', 10],
        ['预计利润', 'num', 10],

    ]  # 解释:0是用户id,输入的是表的所有字段, 每一个字段有3个属性, 列名, 类别,去重后有多少个.

    dummy_output4 = [
        ['订单日期', '预计利润', '预计毛利']
        , '折线图'

    ]

    dict1 = {'input': [str(dummy_input1),str(dummy_input2),str(dummy_input3),str(dummy_input4)], 'output': [str(dummy_output1),str(dummy_output2),str(dummy_output3),str(dummy_output4)],}
    aaa = pd.DataFrame(dict1)
    try:
        aaa.to_sql('data', cx, index=False,if_exists='replace')
        return True
    except:
        return False

    print(1)
if 0:
    reset_db()






#convert data from database.

print('操作之前的数据库内容')
cursor=cx.cursor()
# a=cursor.execute('select * from data')
a=pd.read_sql('select * from data',cx)


print(a)
print('**********************************')


data=[]

for i in range(len(a)):
    tmp=a.iloc[i]
    print(1)
    small_data={'input':eval(tmp['input']), 'output':eval(tmp['output'])}
    data.append(small_data)




all_pic=['柱状图',
'3D柱状图',
'堆积柱状图',
'3D堆积柱状图',
'柱状范围图',
'条形图',
'堆积条形图',
'瀑布图',
'双Y轴图',
'平行坐标图',
'双向图',
'直方图',
'漏斗图',
'饼状图',
'3D饼状图',
'圆环',
'3D圆环',
'南丁格尔图玫瑰图',
'嵌套饼状图',
'旭日图'
'极坐标图',
'雷达图',
'散点图',
'气泡图',
'气泡填充图',
'词云',
'矩形树图',
'指标卡',
'桑基图',
'关系力图',
'关系图',
'平行关系饼图',
'圆形填充图',
'组织结构图',
'时序图',
'水球图',
'仪表盘图',
'甘特图',
'地图（连续型）',
'地图（分段型）',
'气泡地图',
'流向地图',
'GIS地图（气泡型）',
'GIS地图（热力型）',
'环形图'
]


# 基本算法.


#地区,字符串 5个以内输出饼状图 ,5个以上输出柱状图.




def func( input):#新来一个数据,我们让他跟data进行比较
    over = False  # 如果 已经over那么下面判断逻辑都不生效.
    dummy_input=[
    'zb',
    ['订单日期','time',4],
    ['市场类别','string',2],
    ['地区','string',2],
    ['产品类别','string',2],
    ['产品名称','string',2],
    ['预计毛利','num',10],
] #测试用
    dummy_input=input
    def find_first_num_col(input): #找到第一个num的东西
        for i in range(len(input)):
            if i==0:
                continue
            if 'num' == input[i][1]:
                return i
        return None


#========第一个匹配原则.如果地区存在, 就输出地区的图.
    if 0:
        all_col=[i[:2] for i in dummy_input[1:]]
        for i in range(len(all_col)):

            if ['地区','string'] ==all_col[i]:
                pipei=dummy_input[1:][i]
                over=True
                num=pipei[2]
                if num<=5:
                    aaa=find_first_num_col(dummy_input)
                    if aaa:
                        return  [['地区',dummy_input[aaa][0]],all_pic.index('饼状图')]
                else:
                    aaa = find_first_num_col(dummy_input)
                    if aaa:
                        return [['地区', dummy_input[aaa][0]], all_pic.index('柱状图')]
    if 1:
        #============一般策略:读取数据库的内容做对比. 也算是终极策略
        # print("========func数据库的内容",data)

        quanbudeshuchulieming=sum([i['output'][0] for i in data],[])
        inputliemingstrign=[i[0] for i in input[1:] if i[1]=='string']
        inputliemingnum=[i[0] for i in input[1:] if i[1]=='num']
        inputliemingtime=[i[0] for i in input[1:] if i[1]=='time']
        inputliemingstrigntime=inputliemingstrign+inputliemingtime




        if not inputliemingstrigntime:
            inputliemingstrigntime=[i[0] for i in input[1:]]
        if not inputliemingnum:
            inputliemingnum=[i[0] for i in input[1:]]


        inputliemingstrigntimecount=[quanbudeshuchulieming.count(i) for i in inputliemingstrigntime]
        inputliemingnumcount=[quanbudeshuchulieming.count(i) for i in inputliemingnum]

        a=inputliemingstrigntime[inputliemingstrigntimecount.index(max(inputliemingstrigntimecount))]
        b=inputliemingnum[inputliemingnumcount.index(max(inputliemingnumcount))]

        outpic=[i['output'][1] for i in data if  b in i['output'][0] or a in i['output'][0]]
        outpiccount=[outpic.count(i) for i in outpic]
        if outpiccount==[]:
            return [[a,b], '柱状图']
        outpic=outpic[outpiccount.index(max(outpiccount))]
        return [[a,b], outpic]
        print(1)








        return None


    print(1)

#==============================================================================================================下面进行测试的代码.
dummy_input=[
    'zb',
    ['订单日期','time',4],
    ['市场类别','string',2],
    ['地区','string',5],
    ['产品类别','string',2],
    ['产品名称','string',2],
    ['预计毛利','num',10],
    ['预计毛利','num',10],
    ['预计毛利','num',10],
    ['预计毛利','num',10],
    ['预计毛利','num',10],
    ['预计毛利','num',10],
]







def insert_to_database(input,output):
    try:
        cx = sqlite3.connect(" 1.db ")
        a=str(input)
        b=str(output)
        sql=f'insert into data (input,output)values ( "{a}" ,"{b}" );'
        print(sql,33333333333333333333333)
        cx.execute(sql)
        cx.commit()
        print(sql)
        return True
    except:
        return False
def read_all_data_from_db():
    a=pd.read_sql('select * from data',cx)
    return a
# print(insert_to_database(dummy_input,dummy_output))

print('打印数据库现在的内容情况')
print(read_all_data_from_db())

# 只能存字符串,然后再eval转化.

print('做dummy预测')


print(func(dummy_input))
















import os
import io
import json
# import torch

from PIL import Image
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # 解决跨域问题

# weights_path = "./MobileNetV2(flower).pth"
# class_json_path = "./class_indices.json"
#
# # select device
# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# print(device)
# # create model
# model = eval(num_classes=5)
# # load model weights
# model.load_state_dict(torch.load(weights_path, map_location=device))
# model.to(device)
# model.eval()

# load class info
# json_file = open(class_json_path, 'rb')
# class_indict = json.load(json_file)


def get_prediction(image_bytes):
    try:
        tensor = ""
        outputs = torch.softmax(model.forward(tensor).squeeze(), dim=0)
        prediction = outputs.detach().cpu().numpy()
        template = "class:{:<15} probability:{:.3f}"
        index_pre = [(class_indict[str(index)], float(p)) for index, p in enumerate(prediction)]
        # sort probability
        index_pre.sort(key=lambda x: x[1], reverse=True)
        text = [template.format(k, v) for k, v in index_pre]
        return_info = {"result": text}
    except Exception as e:
        return_info = {"result": [str(e)]}
    return return_info








#
"""\
demo:


["aaa",
    ["订单日期","time",4],
    ["市场类别","string",2],
    ["区域","string",2],
    ["产品类别","string",2],
    ["产品名称","string",2],
    ["预计毛利","num",10]
] 
"""
@app.route("/func", methods=["POST","GET"])
# @torch.no_grad()

def editorData():
    # 获取图片文件 name = upload
    img = request.get_json()

    # 定义一个图片存放的位置 存放在static下面
    print('获取json',img
          )
    return jsonify(func(img))




"""\
demo:


{"input":["aaa",
    ["订单日期","time",4],
    ["市场类别","string",2],
    ["区域","string",2],
    ["产品类别","string",2],
    ["产品名称","string",2],
    ["预计毛利","num",10]
] ,"output":


[
        ["产品类别", "预计毛利"]
        , "饼状图"

    ]}
"""




@app.route("/insert_to_database", methods=["POST","GET"])
# @torch.no_grad()

def editorData222():
    # 获取图片文件 name = upload
    img = request.get_json()

    # 定义一个图片存放的位置 存放在static下面
    a=insert_to_database(img['input'],img['output'])
    return jsonify(a)

@app.route("/reset_db", methods=["GET", "POST"])
def reset_db2():
    a=reset_db()
    return a


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)








