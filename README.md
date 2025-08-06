# RAGデモ用サンプルプロジェクト (FastAPI)

このプロジェクトは、RAG (Retrieval-Augmented Generation) のデモを行うために作成されたサンプルアプリケーションです。

## 🎯 ユースケース：API仕様の確認（フロントエンド⇔バックエンド連携）

チーム開発で頻繁に発生するコミュニケーションコストを削減するユースケースです。

### シナリオ

フロントエンド開発者が、商品一覧を表示するためにバックエンドのAPIを呼び出したいと考えています。しかし、APIの正確なエンドポイントや、価格で絞り込むためのパラメータ名が分かりません。（ドキュメントが古い、または存在しないケースを想定）

**👨‍💻 開発者の思考:**
「商品検索APIって`/products`だっけ？ `/api/v1/products`だっけ？ 価格での絞り込みって`price_range`？ それとも`min_price`と`max_price`？」

---

### 🤖 RAGへの質問 (プロンプト)

```
商品一覧を取得するAPIのエンドポイントと、価格でフィルタリングする方法を教えて。
```

---

### 💡 RAGによる回答 (デモの見せどころ)

RAGは、このリポジトリのソースコード（特に `main.py`）を横断的に検索し、仕様をまとめて回答します。

**(期待される回答の例)**

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
>
> **使用例 (curl):**
> ```bash
> curl "http://localhost:8000/api/v1/products?min_price=1000&max_price=20000"
> ```
>
> **関連コード:**
> 関連コードは `main.py` の `get_products` 関数にあります。

### ✨ デモのポイント

*   **ドキュメントの代替:** コードそのものが最新のドキュメントとして機能します。
*   **コミュニケーションコストの削減:** バックエンド担当者に質問したり、古いドキュメントを探したりする手間が省けます。
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

3.  ブラウザまたはcurlで `http://localhost:8000/api/v1/products` にアクセスします。
    ```bash
    curl "http://localhost:8000/api/v1/products?min_price=10000&max_price=50000"
    ```
