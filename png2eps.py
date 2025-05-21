import os
from PIL import Image

def save_as_eps(img_path, img):
    """
    :param img_path: 元画像のパス
    :param img: 保存する画像

    元画像のパスを元に、変換後の画像の保存先を決定する。
    変換後の画像は、元画像と同じディレクトリに保存される。
    """
    save_path = os.path.join('./converted_images', os.path.basename(os.path.dirname(img_path)) , f"{os.path.basename(img_path).split('.')[0]}.eps")
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))
    img.save(save_path)

def convert(img_path):
    """
    :param img_path: 変換したい画像のパス
    :return: 変換後の画像
    """
    img = Image.open(img_path)
    img = img.convert("RGB")
    return img

def convert_all(img_dir):
    """
    :param img_dir: 変換したい画像があるディレクトリ

    変換したい画像があるディレクトリ内の全てのPNG画像を探索し，ePS形式に変換する。
    """
    if not os.path.exists('./converted_images'):
        os.makedirs('./converted_images')
    
    for root, dirs, files in os.walk(img_dir):
        for file in files:
            if file.endswith('.png'):
                img_path = os.path.join(root, file)
                converted_img = convert(img_path)
                save_as_eps(img_path, converted_img)

if __name__ == "__main__":
    img_dir = "" # 変換したい画像があるディレクトリを指定
    convert_all(img_dir)

    # 1枚だけ変換したい場合
    # img_path = "" # 変換したい画像のパスを指定
    # img = convert(img_path)
    # save_as_eps(img_path, img)
