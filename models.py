from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    """
    商品のデータモデル
    """
    id: int
    name: str
    price: int
    category: str

class ProductListResponse(BaseModel):
    """
    商品一覧APIのレスポンスモデル
    """
    message: str
    total: int
    count: int
    products: List[Product]
