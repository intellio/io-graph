from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Item(BaseModel):
	baseUnitOfMeasureId: Optional[UUID] = Field(alias="baseUnitOfMeasureId", default=None,)
	blocked: Optional[bool] = Field(alias="blocked", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	gtin: Optional[str] = Field(alias="gtin", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	inventory: Optional[int] = Field(alias="inventory", default=None,)
	itemCategoryCode: Optional[str] = Field(alias="itemCategoryCode", default=None,)
	itemCategoryId: Optional[UUID] = Field(alias="itemCategoryId", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	number: Optional[str] = Field(alias="number", default=None,)
	priceIncludesTax: Optional[bool] = Field(alias="priceIncludesTax", default=None,)
	taxGroupCode: Optional[str] = Field(alias="taxGroupCode", default=None,)
	taxGroupId: Optional[UUID] = Field(alias="taxGroupId", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	unitCost: Optional[int] = Field(alias="unitCost", default=None,)
	unitPrice: Optional[int] = Field(alias="unitPrice", default=None,)
	itemCategory: Optional[ItemCategory] = Field(alias="itemCategory", default=None,)
	picture: Optional[list[Picture]] = Field(alias="picture", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .item_category import ItemCategory
from .picture import Picture

