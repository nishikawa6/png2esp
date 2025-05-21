# PNGをEPSに変換するプログラム
論文作成の際に大量のpng画像をeps画像に変換する必要があったため作成．

png画像が配置されているディレクトリの構造は以下の場合を想定している．
```
png画像ディレクトリ
.
└── png画像ディレクトリ/
    ├── A/
    │   ├── 1.png
    │   ├── 2.png
    │   └── 3.png
    ├── B/
    │   ├── 1.png
    │   ├── 2.png
    │   └── 3.png
    └── ...

```
eps画像に変換後のディレクトリ構造は以下のようになる．
```
.
└── converted_images/
    ├── A/
    │   ├── 1.png
    │   ├── 2.png
    │   └── 3.png
    ├── B/
    │   ├── 1.png
    │   ├── 2.png
    │   └── 3.png
    └── ...

```

### バージョン
Python 3.12.7で動作確認済み

# 環境構築
1. venvで環境を作成
   ```
   python3 -m venv [envname]
   ```
2. 環境に入る
   - Linux, Macの場合
    ```
    source [envname]/bin/activate
    ```
   - Windowsの場合
    ```
    .\[envname]\Scripts\activate
    ```
3. 必要なライブラリをインポート
   ```
   pip install -r requirements.lock
   ```
4. png2eps.pyの以下の箇所に変換したい画像のディレクトリを指定
   ```
   if __name__ == "__main__":
    img_dir = "" # 変換したい画像があるディレクトリを指定
    convert_all(img_dir)
   ``` 
5. プログラムを実行
   ```
   python png2eps.py
   ```

