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
    0,
    ['订单日期','time',4],
    ['市场类别','string',2],
    ['区域','string',2],
    ['产品类别','string',2],
    ['产品名称','string',2],
    ['预计毛利','num',10],

]         #解释:0是用户id,输入的是表的所有字段, 每一个字段有3个属性, 列名, 类别,去重后有多少个.

dummy_output=[
    ['产品类别', '预计毛利']
    ,2
]




import sqlite3

cx = sqlite3.connect( " 2.db " )





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

sql="create table if not exists {}(id integer primary key autoincrement,input json,output json)".format('data')


# 有2个注意点，一个是非标准json格式的字典需要用json.dumps(dict)转一下再存入，
# 还有一个就是使用self.cursor.fetchall()返回的结果需要是一个tuple,里面的不是json是一个str,需要eval再转一下。









#convert data from database.


cursor=cx.cursor()
# a=cursor.execute('select * from data')
a=pd.read_sql('select * from data',cx)

print(111)
print(a)
print('**********************************')


data=[]

for i in range(len(a)):
    tmp=a.iloc[i]
    print(1)
    small_data={'input':eval(tmp['input']), 'output':eval(tmp['output'])}
    data.append(small_data)
print(1)



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



    if 1:
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
        return None
    print(1)


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




print(func(dummy_input))


def insert_to_database(input):

    a=str(dummy_input)
    b=str(dummy_input)
    sql=f'insert into data (input,output)values ( "{a}" ,"{b}" );'
    cx.execute(sql)
    cx.commit()
    print(sql)
def read_all_data_from_db():
    a=pd.read_sql('select * from data',cx)
    print(a)
print(insert_to_database(111))
print(read_all_data_from_db())




