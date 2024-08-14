from flask import Blueprint
# from . import pb
goods_bp = Blueprint('goods', __name__)
pb = Blueprint('gongzi',__name__,url_prefix='/gongzi')