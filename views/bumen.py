from flask import Flask, render_template, request, redirect, url_for, session, Response

from comm import str2datetime
from module.model import *
from service.services import SysService
from service.PublicServices import PublicSysService
from utils.getPublicData import fetch_data_by_month
from flask import Flask,session,render_template,redirect,Blueprint,request
from module.GongziModel import Bumen
from views.__init__ import pb
from service.BumenService import BumenSysService

from service.PublicServices import PublicSysService,get_all_records,del_records,create_records,update_records,add_and_updata
@pb.route("/bumen", methods=["GET", "POST"])
def bumen():

    user = SysService.get_user_info(session.get("username"))
    msg = request.args.get("msg")
    err = request.args.get("err")
    bumen_records = get_all_records(Bumen)
    setting = SysService.get_setting()
    query_list = [(bumen, False) for bumen in bumen_records]

    return render_template('bumen.html', context={"user": user, "query_list": query_list, "setting": setting,
                                                           "msg": msg, "err": err})

@pb.route("/del_bumen", methods=["GET"])
def del_record():
    if not session.get("username"):
        return redirect(url_for("index"))
    if request.method == "GET":
        record_id = request.args.get("record_id")
        if not record_id:
            return redirect(url_for("home", err="参数错误"))
        ret = del_records(Bumen,record_id)
        if ret:
            return redirect(url_for("gongzi.bumen"))
        return redirect(url_for("gongzi.bumen", err="删除失败"))


@pb.route("/add_bumen", methods=["POST"])
def create_bumen():
    if not session.get("username"):
        return redirect(url_for("index"))
    if request.method == "POST":
        data = request.form
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 自动设置当前时间
        bumen_name = data.get("bumen_name", "")
        record_id = data.get("record_id", "")
        gonghao = data.get("gonghao", "")
        create_data = {
            "id":record_id,
            "gonghao":gonghao,
            "bumen_name":bumen_name,
            "create_time":date

        }
        ret = add_and_updata(Bumen,create_data)
        if ret==0:
            return redirect(url_for("gongzi.bumen", err="参数错误"))
        return redirect(url_for("gongzi.bumen"))
    return redirect(url_for("gongzi.bumen", err="参数错误"))


@pb.route("/bumen_import", methods=["POST"])
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
        ret, msg = PublicSysService.excel_import(Bumen,file.filename)
        if ret < 0:
            return redirect(url_for("home", err=msg))
        return redirect(url_for("gongzi.bumen", msg=msg))
