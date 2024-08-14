from flask import Flask, render_template, request, redirect, url_for, session

from comm import str2datetime
from module.model import *
from service.services import SysService
from utils.getPublicData import fetch_data_by_month
from views.bumen import bumen
from views.yuangong import yuangong
from views.shebao import shebao
from views.yibao import yibao
from views.duanxin_fare import duanxin_fare
from views.neitui import neitui
from views.kaoqin import kaoqin
from views.duanxin_service import duanxin_service
from views.zhichang_kaizhi import zhichang_kaizhi
from views.zongjingban_kaizhi import zongjingban_kaizhi
from views.jixiaofangan import jixiaofangan
from views.xiangmu_fangan import xiangmu_fangan
from views.yuangong_gongzi import yuangong_gongzi
from views.yuangong_jixiao import yuangong_jixiao
from views.__init__ import pb

app = Flask(__name__)

HOST = "127.0.0.1"  # 数据库地址
PORT = 3306
USERNAME = "root"   # 数据库账号
PASSWORD = "123456"  # 数据库密码
DATABASE = "gongzi"  # 数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "JKXOSDIFHL@ksljfflaj@sdfasdf"
db.init_app(app)

app.register_blueprint(pb)


with app.app_context():
    db.create_all()
    init_data()
    # TestData.random_data()




@app.route('/')
def index():  # put application's code here
    msg = request.args.get("msg")
    context = {
        "msg": msg
    }
    if not session.get("username"):
        return redirect(url_for("login", msg=msg))

    return redirect(url_for("home", msg=msg))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/login", methods=["get","post"])
def login():
    msg = request.args.get("msg")
    if request.method == "GET":
        return render_template("index.html", context={"msg": msg})

    username = request.form.get("username")
    password = request.form.get("password")
    if not all([username, password]):
        return render_template("index.html", context={"err": "参数错误"})
    user = User.query.filter_by(username=username).first()
    if not user:
        return render_template("index.html", context={"err": "用户名不存在"})
    if user.password != password:
        return render_template("index.html", context={"err": "密码错误"})

    session["username"] = username

    return redirect(url_for("home"))


@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")
    # do something with the form data
    if not all([username, confirm_password, password]):
        return render_template("index.html", context={"err": "参数错误"})
    if len(password) < 3:
        return render_template("index.html", context={"err": "密码长度必须大于3"})
    if confirm_password != password:
        return render_template("index.html", context={"err": "两次密码不一致"})

    user = User.query.filter_by(username=username).first()
    if user:
        return render_template("index.html", context={"err": "用户名已存在"})

    user = User()
    user.username = username
    user.password = password
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("index", msg="注册成功"))


@app.route("/home", methods=["GET", "POST"])
def home():
    if not session.get("username"):
        return redirect(url_for("index"))
    user = SysService.get_user_info(session.get("username"))
    msg = request.args.get("msg")
    err = request.args.get("err")

    if request.method == "POST":
        data = request.form
        record_id = data.get("record_id", "-1")
        position = data.get("position", "")
        date = data.get("date", "")
        try:
            date = str2datetime(date)
        except Exception as e:
            return redirect(url_for("home", err="日期格式错误"))
        jsl = data.get("jsl", "")
        ysl = data.get("ysl", "")
        sw = data.get("sw", "")
        temp = data.get("temp", "")
        sls = data.get("sls", "")
        dbcxwy = data.get("dbcxwy", "")
        wz = data.get("wz", "")
        if not all([position, date, jsl, ysl, sw, temp, sls, dbcxwy, wz]):
            return redirect(url_for("home", err="参数错误"))
        SysService.add_record(record_id, position, date, jsl, ysl, sw, temp, sls, dbcxwy, wz)


    position = request.args.get("position", "")
    query_list = SysService.get_record_list(position)
    setting = SysService.get_setting()
    query_list = [(x, SysService.set_flag(x, setting)) for x in query_list] if query_list else []

    return render_template('record_manager.html', context={"user": user, "query_list": query_list, "setting": setting,
                                                 "msg": msg, "err": err, "position": position})

@app.route("/del_record", methods=["GET"])
def del_record():
    if not session.get("username"):
        return redirect(url_for("index"))
    if request.method == "GET":
        record_id = request.args.get("record_id")
        if not record_id:
            return redirect(url_for("home", err="参数错误"))
        ret = SysService.delete_record(record_id)
        if ret:
            return redirect(url_for("home", msg="删除成功"))
        return redirect(url_for("home", err="删除失败"))

@app.route("/excel_import", methods=["POST"])
def excel_import():
    if not session.get("username"):
        return redirect(url_for("index"))
    if request.method == "POST":
        file = request.files.get("file")
        if not file:
            return redirect(url_for("home", err="请选择文件"))
        if not file.filename.endswith(".xlsx") or file.filename.endswith(".xls"):
            return redirect(url_for("home", err="请选择xlsx或xls文件"))
        file.save("./static/excel/" + file.filename)
        ret, msg = SysService.excel_import(file.filename)
        if ret < 0:
            return redirect(url_for("home", err=msg))
        return redirect(url_for("home", msg=msg))

@app.route("/setting", methods=["POST"])
def setting():
    if not session.get("username"):
        return redirect(url_for("index"))
    if request.method == "POST":
        data = request.form
        jsl = data.get("jsl", "")
        jsl_action = data.get("jsl_action", "")
        ysl = data.get("ysl", "")
        ysl_action = data.get("ysl_action", "")
        sw = data.get("sw", "")
        sw_action = data.get("sw_action", "")
        temp = data.get("temp", "")
        temp_action = data.get("temp_action", "")
        sls = data.get("sls", "")
        sls_action = data.get("sls_action", "")
        dbcxwy = data.get("dbcxwy", "")
        dbcxwy_action = data.get("dbcxwy_action", "")
        wz = data.get("wz", "")
        wz_action = data.get("wz_action", "")
        update_data = {
            "jsl": {"action": jsl_action, "value": jsl},
            "ysl": {"action": ysl_action, "value": ysl},
            "sw": {"action": sw_action, "value": sw},
            "temp": {"action": temp_action, "value": temp},
            "sls": {"action": sls_action, "value": sls},
            "dbcxwy": {"action": dbcxwy_action, "value": dbcxwy},
            "wz": {"action": wz_action, "value": wz},
        }
        SysService.update_setting(update_data)
        return redirect(url_for("home", msg="设置成功"))
    return redirect(url_for("home", err="参数错误"))


@app.route("/userInfo", methods=["POST", "GET"])
def userInfo():
    if not session.get("username"):
        return redirect(url_for("index"))

    user = SysService.get_user_info(session.get("username"))
    user_list = None
    if user.role == "admin":
        user_list = SysService.get_user_list()
    if not user:
        print("异常，数据库查不到user信息")
        return redirect(url_for("index"))
    if request.method == "POST":
        new_password = request.form.get("new_password")
        if not new_password or len(new_password) < 3:
            return render_template('userInfo.html', context={"err": "密码长度必须大于3", "user": user})
        # 判断患者信息
        name = request.form.get("name")
        age = request.form.get("age")
        sex = request.form.get("sex")
        if not all([name, age, sex]):
            return render_template('userInfo.html', context={"user": user,  "err": "参数错误"})
        if not age.isdigit() or int(age) < 0 or int(age) > 150:
            return render_template('userInfo.html', context={"user": user, "err": "年龄必须是整数且必须在0-150之间"})

        if sex not in ["男", "女"]:
            return render_template('userInfo.html', context={"user": user,  "err": "性别只能是男或女"})

        user.password = new_password
        db.session.commit()
        return render_template('userInfo.html', context={"msg": "修改密码成功", "user": user, "user_list": user_list})
    msg = request.args.get("msg")
    err = request.args.get("err")
    return render_template('userInfo.html', context={"user": user, "user_list": user_list,  "msg": msg, "err": err})


@app.route("/set_user_role", methods=["GET"])
def set_user_role():
    if not session.get("username"):
        return redirect(url_for("index"))
    user = SysService.get_user_info(session.get("username"))
    if user.role != "admin":
        return render_template("userInfo.html", context={"err": "非管理员无法修改角色", "user": user})
    username = request.args.get("username")
    role = request.args.get("role", "user")
    if role not in ["admin", "user"]:
        return redirect(url_for("userInfo", err="角色错误"))
    if username == session.get("username"):
        return redirect(url_for("userInfo", err="不能修改自己的角色"))

    SysService.set_user_role(username, role)
    return redirect(url_for("userInfo", msg="修改用户角色成功"))


@app.route("/help", methods=["GET"])
def help():
    if not session.get("username"):
        return redirect(url_for("index"))
    user = SysService.get_user_info(session.get("username"))
    return render_template('help.html', context={"user": user,})

if __name__ == '__main__':
    app.run(debug=True)
