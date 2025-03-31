from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ItemActivityOLDCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ItemActivityOLD]] = Field(alias="value", default=None,)

from .item_activity_o_l_d import ItemActivityOLD
