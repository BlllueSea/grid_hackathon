from PIL import Image
import numpy as np


#前処理
#画像のサイズを変える
#numpy.array型に変換する
def resize_square_min(img, outpx=128):#短辺で切り取る
    size = min(img.size)
    width, height = img.size
    le, up = (width - size)//2, (height - size)//2
    ri, lo = (width + size)//2, (height + size)//2
    cropped = img.crop((le, up, ri, lo))
    return cropped.resize((outpx, outpx))


def resize_square_max(img, outpx=128):#長辺で切り取る
    size = max(img.size)
    width, height = img.size
    le, up = (width - size)//2, (height - size)//2
    ri, lo = (width + size)//2, (height + size)//2
    cropped = img.crop((le, up, ri, lo))
    return cropped.resize((outpx, outpx))


def pred_class_proba(img_arr, model):#予測ラベルとその確率を返す
    class_dict = {idx:name.decode() for idx, name in enumerate(model.class_map)}
    pred_probs = model.get_probability(img_arr)[0]
    pred_num = np.argmax(pred_probs)
    pred_proba = pred_probs[pred_num]
    pred_class = class_dict[pred_num]
    return pred_num, pred_proba


def predict_from_2img(original_img_path, model, px=128, show=False):#長辺切り取りと短辺切り取りの画像を生成して予測ラベルを返す
    class_dict = {idx:name.decode() for idx, name in enumerate(model.class_map)}
    img = Image.open(original_img_path)
    is_same = False
    if img.size[0] == img.size[1]:
        is_same = False
    img_1 = resize_square_min(img, outpx=px)
    img_2 = resize_square_max(img, outpx=px)
    convert = lambda x: np.asarray(x).transpose(2, 0, 1)[np.newaxis, :, :, :] #img -> 4d arr
    img_arr_1, img_arr_2 = convert(img_1), convert(img_2)
    num_1, proba_1 = pred_class_proba(img_arr_1, model=model)
    if is_same == True:
        num_2, proba_2 = pred_class_proba(img_arr_2, model=model)
    else:
        num_2, proba_2 = num_1, proba_1
    if show==True:
        print(class_dict[num_1], proba_1)
        print(class_dict[num_2], proba_2)
    if proba_1 > proba_2:
        return num_1
    else:
        return num_2
