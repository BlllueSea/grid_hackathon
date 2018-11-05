#!/usr/bin/env python
# -*- coding: utf-8 -*-

from service import analysis_per, draw_graph, convert_img, recommend
import json
import os
from bottle import route, run, static_file, HTTPResponse, request
from http.server import BaseHTTPRequestHandler, HTTPServer

from renom_img.api.classification.vgg import VGG16

model = VGG16()
model.load("paramater/vgg16_18c_jp0_last.h")



# jsonのレスポンス作成
def create_response(body):
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    r.set_header('Access-Control-Allow-Origin', '*')
    return r


@route('/')
def index():
    return static_file("./index.html", "./")


# ./jsディレクトリ以下のファイル読み込み
@route('/js/<filename:path>')
def read_js(filename):
    return static_file(filename, "./js/")


# ./cssディレクトリ以下のファイル読み込み
@route('/css/<filename:path>')
def read_css(filename):
    return static_file(filename, "./css/")

# ./staticディレクトリ以下のファイル読み込み
@route('/static/<filename:path>')
def read_static(filename):
    return static_file(filename, "./static/")

# ./tmpディレクトリ以下のファイル読み込み
@route('/tmp/<filename:path>')
def read_tmp(filename):
    return static_file(filename, "./tmp/")


# 画像をフォームデータとして受け取り、結果画像のパスを返す
@route('/upload', method='POST')
def upload():
    image = request.files.get('file')
    sex = int(request.forms.get("sex"))
    print(image.filename)
    print("sex",sex)
    name, _ = os.path.splitext(image.filename)

    if _ not in ('.png', '.jpg', '.jpeg'):
        return "File extension not allowed."

    tmp_dir = os.getcwd() + "/tmp"
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    upload_path = "/{path}/{file}".format(path=tmp_dir, file=name+".png")
    image.save(upload_path, overwrite=True)
    print(upload_path)

# get prediction
    predict_value = convert_img.predict_from_2img(upload_path, model)

# get food-name and persentage
    food_name, per_dict, real_value_list = analysis_per.compare_nutrition(predict_value, sex)
    recommend_img, recommend_menu = recommend.recommend(per_dict)

# prepare data to send
    main_dict = {
        "food_name": food_name,
        "per_dict": per_dict,
        "real_value": real_value_list,
        "recommend_img_path": "/static/" + recommend_img,
        "recommend_menu": recommend_menu
    }
    print(main_dict)
    json_body = json.dumps(main_dict)
    send_data = create_response(json_body)
    return send_data



@route('/img/<filename:path>')
def read_img(filename):
    print('img', filename)
    return static_file(filename, "./img/")




run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
