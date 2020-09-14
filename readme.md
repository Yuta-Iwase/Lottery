
# Lottery

## 必要環境
* Python

## 使い方
1. 以下のファイルを記入する
    * `lot.txt`: 抽選対象の人の名前のリスト。人と人の間は改行。  
        例:
        ```
        菅 義偉
        岸田 文雄
        石破 茂
        ```
    * `position_list.txt`: 役職のリスト  
        例:
        ```
        総理大臣
        官房長官
        ```
        ※複数人が同じ役職に付く場合はその分だけ連ねる。  
        例:
        ```
        総理大臣
        大臣
        大臣
        大臣
        大臣
        ```
2. 以下のコマンドで抽選を実行
    ```sh
    python run.py
    ```

---

## あとがき
* Pythonを利用したのは、Python標準の乱数生成がメルセンヌ・ツイスタ法を使っていたから[[1](https://docs.python.org/ja/3/library/random.html)]。(Javaは線形合同法を用いるため[[2](https://docs.oracle.com/javase/jp/8/docs/api/java/util/Random.html)]、乱数生成の観点ではPythonが優れている。)