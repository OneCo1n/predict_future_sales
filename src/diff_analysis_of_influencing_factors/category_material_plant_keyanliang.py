from diff_analysis_of_influencing_factors.data_set.data_division import model_data_division
from diff_analysis_of_influencing_factors.train_model.lasso_lightGBM.lasso_lightGBM import \
    do_analysis_use_lasso_lightGBM
from diff_analysis_of_influencing_factors.train_model.lightGBM.lightGBM import use_lightGBM, do_analysis_use_lightGBM
from flaskTest.views.data_views.total_views import get_total_by_material, get_total_desc_by_material, \
    get_total_by_material_and_company, get_total_desc_by_material_and_company, get_total_by_category_and_company, \
    get_total_desc_by_category_and_company, get_total_by_category_and_keyanliang, \
    get_total_desc_by_category_and_keyanliang
from diff_analysis_of_influencing_factors.data_set.columns_name import exgColumnsName
from matplotlib import pyplot
from xgboost import XGBClassifier
from xgboost import plot_importance
from data_preprocess.columnsExg import *
import lightgbm as lgb
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
# sns.set_style('white',{'font.sans-serif':['simhei','Arial']})
sns.set(style='whitegrid',palette='tab10')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['axes.unicode_minus']=False
plt.rcParams['font.sans-serif']=['Microsoft YaHei']


def do_analysis_category_material_plant_group_by_keyanliang(category, start_time, end_time, keyanliang):

    # 获取该商品的销量数据、油站信息、poi信息、促销信息等，用于模型训练（已编码）
    data = get_total_by_category_and_keyanliang(category, start_time, end_time, keyanliang)

    # 更改列名
    data = exgColumnsName(data)

    # 划分数据集
    # 对销量进行分析
    target_name = 'quantity'

    mse, rmse, r2, importance_dict = do_analysis_use_lightGBM(data, target_name)
    mse, rmse, r2, importance_dict = do_analysis_use_lasso_lightGBM(data, target_name)

    print(importance_dict)
    plot_importance(importance_dict)
    pyplot.show()

    # 获取该商品的销量描述信息、油站描述信息、poi信息等（未编码）展示上面得出的影响因素与销量的具体影响
    data_desc = get_total_desc_by_category_and_keyanliang(category, start_time, end_time, keyanliang)
    # 更改列名
    data_desc = exgColumnsName(data_desc)

    pass



# 年销量5000-10000T
# 年销量3000-5000T
# 年销量500-1000T
# 年销量1000-3000T
# 年销量10000T以上

# 润滑油
# 汽车用品
# 汽车服务
# 收费服务
# 包装饮料
# 个人护理用品
# 酒类
# 速食
# 日用品
# 饼干/糕点
# 糖果
# 奶类
# 清洁用品
# 零食
# 雪糕
# 面包
# 药品/计生/保健
# 家庭食品
# 香烟
# 办公图书音像
# 通讯/数码/电脑
# 其他
# 散装饮料
# 化工农资

do_analysis_category_material_plant_group_by_keyanliang('包装饮料', '2019-09-01', '2019-12-01', '年销量5000-10000T')