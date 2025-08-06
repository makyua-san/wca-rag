# RAGデモ用サンプルプロジェクト (FastAPI)

このプロジェクトは、RAG (Retrieval-Augmented Generation) のデモを行うために作成されたサンプルアプリケーションです。v1.1に更新され、より実践的なAPI機能が追加されました。

## 🎯 ユースケース：API仕様の確認（フロントエンド⇔バックエンド連携）

チーム開発で頻繁に発生するコミュニケーションコストを削減するユースケースです。

### シナリオ

フロントエンド開発者が、商品一覧を表示するためにバックエンドのAPIを呼び出したいと考えています。しかし、APIの正確なエンドポイントや、価格での絞り込み、ソート、ページネーションの方法が分かりません。（ドキュメントが古い、または存在しないケースを想定）

**👨‍💻 開発者の思考:**
「商品検索APIってどうやって使うんだっけ？価格での絞り込みは？名前でソートしたいんだけど、パラメータは何を指定すればいいんだろう？」

---

### 🤖 RAGへの質問 (プロンプト)

**(質問1: 一覧取得APIについて)**
```
商品一覧を取得するAPIのエンドポイントと、価格でのフィルタリング方法、そして名前で昇順にソートする方法を教えて。
```

**(質問2: 個別取得APIについて)**
```
IDが5番の商品を取得するAPIを教えて。
```

---

### 💡 RAGによる回答 (デモの見せどころ)

RAGは、このリポジトリのソースコード（`main.py`と`models.py`）を横断的に検索し、仕様をまとめて回答します。

**(期待される回答の例 - 質問1)**

> 商品一覧取得APIの仕様は以下の通りです。
>
> **エンドポイント:** `GET /api/v1/products`
>
> **担当コード:** `main.py` の `get_products` 関数
>
> **パラメータ:**
> - `q` (string, optional): 検索キーワード
> - `min_price` (integer, optional): 最小価格
> - `max_price` (integer, optional): 最大価格
> - `sort_by` (string, optional): ソート対象 (`name` または `price`)。デフォルトは `name`。
> - `order` (string, optional): ソート順 (`asc` または `desc`)。デフォルトは `asc`。
> - `skip` (integer, optional): スキップする件数。デフォルトは `0`。
> - `limit` (integer, optional): 取得する最大件数。デフォルトは `10`。
>
> **使用例 (curl):**
> 名前（name）で昇順（asc）にソートし、価格を1000円から20000円で絞り込む場合のコマンドは以下の通りです。
> ```bash
> curl "http://localhost:8000/api/v1/products?min_price=1000&max_price=20000&sort_by=name&order=asc"
> ```

**(期待される回答の例 - 質問2)**
> IDで商品を個別取得するAPIの仕様は以下の通りです。
>
> **エンドポイント:** `GET /api/v1/products/{product_id}`
>
> **担当コード:** `main.py` の `get_product_by_id` 関数
>
> **使用例 (curl):**
> ```bash
> curl "http://localhost:8000/api/v1/products/5"
> ```

### ✨ デモのポイント

*   **リッチな仕様の理解:** 機能が追加されても、RAGはコードから正確なパラメータや新しいエンドポイントを理解できます。
*   **具体的な利用例の提示:** 開発者がすぐ試せるように、`curl`コマンドのような具体的な例まで生成できます。

## 🚀 実行方法

1.  必要なパッケージをインストールします。
    ```bash
    pip install -r requirements.txt
    ```

2.  以下のコマンドでAPIサーバーを起動します。
    ```bash
    uvicorn main:app --reload
    ```

3.  ブラウザまたはcurlでAPIにアクセスします。
    *   **一覧取得 (ページネーション付き):**
        ```bash
        curl "http://localhost:8000/api/v1/products?skip=0&limit=5"
        ```
    *   **個別取得:**
        ```bash
        curl "http://localhost:8000/api/v1/products/3"
        ```
