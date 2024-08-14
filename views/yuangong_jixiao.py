from flask import Flask, render_template, request, redirect, url_for, session, Response

from comm import str2datetime
from module.model import *
from service.services import SysService
from service.PublicServices import PublicSysService
from utils.getPublicData import fetch_data_by_month
from flask import Flask,session,render_template,redirect,Blueprint,request
from module.GongziModel import YuangongJixiao
from views.__init__ import pb

from service.PublicServices import PublicSysService,get_all_records,del_records,create_records,update_records,add_and_updata,get_create_data_from_model



@pb.route("/yuangong_jixiao", methods=["GET", "POST"])
def yuangong_jixiao():
    user = SysService.get_user_info(session.get("username"))
    msg = request.args.get("msg")
    err = request.args.get("err")
    yuangong_jixiao_records = get_all_records(YuangongJixiao)
    setting = SysService.get_setting()
    query_list = [(yuangong_jixiao, False) for yuangong_jixiao in yuangong_jixiao_records]

    return render_template('yuangong_jixiao.html', context={"user": user, "query_list": query_list, "setting": setting,
                                                           "msg": msg, "err": err})

@pb.route("/del_yuangong_jixiao", methods=["GET"])
def del_yuangong_jixiao():
    if not session.get("username"):
        return redirect(url_for("index"))
    if request.method == "GET":
        record_id = request.args.get("id")
        if not record_id:
            return redirect(url_for("home", err="参数错误"))
        ret = del_records(YuangongJixiao,record_id)
        if ret:
            return redirect(url_for("gongzi.yuangong_jixiao"))
        return redirect(url_for("gongzi.yuangong_jixiao", err="删除失败"))


@pb.route("/add_yuangong_jixiao", methods=["POST"])
def create_yuangong_jixiao():
    if not session.get("username"):
        return redirect(url_for("index"))
    if request.method == "POST":
        data = request.form
        print(data)
        # 动态获取yuangong_jixiao模型的字段，并构建create_data
        create_data = get_create_data_from_model(YuangongJixiao, data)
        # 假设你有一个函数可以将字典添加到数据库
        ret = add_and_updata(YuangongJixiao, create_data)
        if ret == 0:
            return redirect(url_for("gongzi.yuangong_jixiao", err="参数错误"))
        return redirect(url_for("gongzi.yuangong_jixiao"))
    return redirect(url_for("gongzi.yuangong_jixiao", err="参数错误"))


@pb.route("/yuangong_jixiao_import", methods=["POST"])
def yuangong_jixiao_import():
    if not session.get("username"):
        return redirect(url_for("index"))
    if request.method == "POST":
        file = request.files.get("file")
        if not file:
            return redirect(url_for("home", err="请选择文件"))
        if not file.filename.endswith(".xlsx") or file.filename.endswith(".xls"):
            return redirect(url_for("home", err="请选择xlsx或xls文件"))

        file.save("./static/excel/" + file.filename)
        ret, msg = PublicSysService.excel_import(YuangongJixiao,file.filename)
        if ret < 0:
            return redirect(url_for("home", err=msg))
        return redirect(url_for("gongzi.yuangong_jixiao", msg=msg))
