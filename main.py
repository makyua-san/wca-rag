from typing import Optional, List
from fastapi import FastAPI, HTTPException
from models import Product, ProductListResponse

# FastAPIアプリケーションのインスタンスを作成
app = FastAPI(
    title="RAGデモ用商品API",
    description="このAPIは、RAG（Retrieval-Augmented Generation）のデモンストレーション用に作成されたものです。",
    version="1.1.0",
)

# --- ダミーデータ ---
# 実際のアプリケーションではデータベースから取得する
DUMMY_PRODUCTS_DB: List[Product] = [
    Product(id=1, name="高機能スマートフォン", price=80000, category="electronics"),
    Product(id=2, name="ノイズキャンセリングヘッドホン", price=25000, category="electronics"),
    Product(id=3, name="オーガニックコットンTシャツ", price=4500, category="fashion"),
    Product(id=4, name="レザーバックパック", price=18000, category="fashion"),
    Product(id=5, name="自動掃除ロボット", price=45000, category="home"),
    Product(id=6, name="コーヒーメーカー", price=9800, category="home"),
]

# RAGがAPI仕様を理解しやすいように、パラメータの説明を充実させる
@app.get(
    "/api/v1/products",
    response_model=ProductListResponse,
    summary="商品一覧の取得",
    description="複数の条件を指定して商品を検索し、一覧で取得します。",
)
def get_products(
    q: Optional[str] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
    sort_by: Optional[str] = 'name',
    order: Optional[str] = 'asc',
    skip: int = 0,
    limit: int = 10,
) -> ProductListResponse:
    """
    商品の一覧を、検索キーワード、価格帯、ソート順、ページネーションを指定して取得します。

    - **q**: 商品名に含まれる検索キーワード (例: `スマートフォン`)
    - **min_price**: 最小価格 (例: `10000`)
    - **max_price**: 最大価格 (例: `50000`)
    - **sort_by**: ソート対象のフィールド (`name` または `price`)
    - **order**: ソート順 (`asc` または `desc`)
    - **skip**: スキップする件数 (ページネーション用)
    - **limit**: 取得する最大件数 (ページネーション用)
    """

    products = DUMMY_PRODUCTS_DB

    # フィルタリング
    if q:
        products = [p for p in products if q.lower() in p.name.lower()]
    if min_price is not None:
        products = [p for p in products if p.price >= min_price]
    if max_price is not None:
        products = [p for p in products if p.price <= max_price]

    # ソート
    if sort_by in ['name', 'price']:
        products.sort(key=lambda p: getattr(p, sort_by), reverse=(order == 'desc'))

    total_count = len(products)

    # ページネーション
    paginated_products = products[skip : skip + limit]

    return ProductListResponse(
        message="商品一覧を取得しました。",
        total=total_count,
        count=len(paginated_products),
        products=paginated_products
    )

@app.get(
    "/api/v1/products/{product_id}",
    response_model=Product,
    summary="単一商品の取得",
    description="IDを指定して特定の商品情報を取得します。",
)
def get_product_by_id(product_id: int) -> Product:
    """
    商品IDを指定して、単一の商品情報を取得します。

    - **product_id**: 取得対象の`id`
    """
    product = next((p for p in DUMMY_PRODUCTS_DB if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="商品が見つかりません。")
    return product

@app.get("/")
def read_root():
    return {"message": "RAGデモ用の商品APIへようこそ。/docs を確認してください。"}
