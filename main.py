from typing import Optional, List, Dict, Any
from fastapi import FastAPI

# FastAPIアプリケーションのインスタンスを作成
app = FastAPI()

# --- ダミーデータ ---
# 実際のアプリケーションではデータベースから取得する
DUMMY_PRODUCTS = [
    {"id": 1, "name": "高機能スマートフォン", "price": 80000, "category": "electronics"},
    {"id": 2, "name": "ノイズキャンセリングヘッドホン", "price": 25000, "category": "electronics"},
    {"id": 3, "name": "オーガニックコットンTシャツ", "price": 4500, "category": "fashion"},
    {"id": 4, "name": "レザーバックパック", "price": 18000, "category": "fashion"},
    {"id": 5, "name": "自動掃除ロボット", "price": 45000, "category": "home"},
    {"id": 6, "name": "コーヒーメーカー", "price": 9800, "category": "home"},
]

@app.get("/api/v1/products", summary="商品一覧取得")
def get_products(
    q: Optional[str] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
) -> Dict[str, Any]:
    """
    商品の一覧を検索キーワードと価格帯でフィルタリングして取得します。

    Args:
        q (Optional[str]): 検索キーワード。商品名に含まれる場合にマッチします。
        min_price (Optional[int]): フィルタリング対象の最小価格。
        max_price (Optional[int]): フィルタリング対象の最大価格。

    Returns:
        Dict[str, Any]: フィルタリングされた商品リストを含む辞書。
    """

    # このコントローラがRAGによって解析されることを想定しています。
    # フロントエンド開発者は、このコードを見ることで、
    # エンドポイントのパス、HTTPメソッド、そして利用可能なパラメータ
    # (q, min_price, max_price) を知ることができます。

    filtered_products = DUMMY_PRODUCTS

    # 検索キーワードでのフィルタリング
    if q:
        filtered_products = [
            p for p in filtered_products if q.lower() in p["name"].lower()
        ]

    # 最小価格でのフィルタリング
    if min_price is not None:
        filtered_products = [p for p in filtered_products if p["price"] >= min_price]

    # 最大価格でのフィルタリング
    if max_price is not None:
        filtered_products = [p for p in filtered_products if p["price"] <= max_price]

    return {
        "message": "商品一覧を取得しました。",
        "parameters": {
            "q": q,
            "min_price": min_price,
            "max_price": max_price,
        },
        "products": filtered_products,
    }

# ルートパスへのアクセス
@app.get("/")
def read_root():
    return {"message": "RAGデモ用の商品APIへようこそ。/api/v1/products にアクセスしてください。"}
