from flask import Flask, render_template, request, redirect, url_for, session, Response

from comm import str2datetime
from module.model import *
from service.services import SysService
from service.PublicServices import PublicSysService
from utils.getPublicData import fetch_data_by_month
from flask import Flask,session,render_template,redirect,Blueprint,request
from module.GongziModel import Yuangong
from views.__init__ import pb

from service.PublicServices import PublicSysService,get_all_records,del_records,create_records,update_records,add_and_updata,get_create_data_from_model



@pb.route("/yuangong", methods=["GET", "POST"])
def yuangong():
    user = SysService.get_user_info(session.get("username"))
    msg = request.args.get("msg")
    err = request.args.get("err")
    yuangong_records = get_all_records(Yuangong)
    setting = SysService.get_setting()
    query_list = [(yuangong, False) for yuangong in yuangong_records]

    return render_template('yuangong.html', context={"user": user, "query_list": query_list, "setting": setting,
                                                           "msg": msg, "err": err})

@pb.route("/del_yuangong", methods=["GET"])
def del_yuangong():
    if not session.get("username"):
        return redirect(url_for("index"))
    if request.method == "GET":
        record_id = request.args.get("id")
        if not record_id:
            return redirect(url_for("home", err="参数错误"))
        ret = del_records(Yuangong,record_id)
        if ret:
            return redirect(url_for("gongzi.yuangong"))
        return redirect(url_for("gongzi.yuangong", err="删除失败"))


@pb.route("/add_yuangong", methods=["POST"])
def create_yuangong():
    if not session.get("username"):
        return redirect(url_for("index"))
    if request.method == "POST":
        data = request.form
        print(data)
        # 动态获取Yuangong模型的字段，并构建create_data
        create_data = get_create_data_from_model(Yuangong, data)

        # 假设你有一个函数可以将字典添加到数据库
        ret = add_and_updata(Yuangong, create_data)
        if ret == 0:
            return redirect(url_for("gongzi.yuangong", err="参数错误"))
        return redirect(url_for("gongzi.yuangong"))
    return redirect(url_for("gongzi.yuangong", err="参数错误"))


@pb.route("/yuangong_import", methods=["POST"])
def yuangong_import():
    if not session.get("username"):
        return redirect(url_for("index"))
    if request.method == "POST":
        file = request.files.get("file")
        if not file:
            return redirect(url_for("home", err="请选择文件"))
        if not file.filename.endswith(".xlsx") or file.filename.endswith(".xls"):
            return redirect(url_for("home", err="请选择xlsx或xls文件"))

        file.save("./static/excel/" + file.filename)
        ret, msg = PublicSysService.excel_import(Yuangong,file.filename)
        if ret < 0:
            return redirect(url_for("home", err=msg))
        return redirect(url_for("gongzi.yuangong", msg=msg))
