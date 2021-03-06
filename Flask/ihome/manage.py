#coding=utf-8
from flask import Flask
from flask_script import Manager

from app.house_views import house_blue
from app.order_views import order_blue
from app.user_views import user_blue
from utils.functions import init_ext




app = Flask(__name__)

app.register_blueprint(blueprint=user_blue,url_prefix='/user')
app.register_blueprint(blueprint=house_blue, url_prefix='/house')
app.register_blueprint(blueprint=order_blue, url_prefix='/order')

app.secret_key = 'jiangxiucheng'




# 配置config文件
# app.config.from_object(Config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/ihome'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
# 初始化
init_ext(app)


manage = Manager(app)

if __name__ == '__main__':
    manage.run()