from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CurrencyColumn(BaseModel):
	locale: Optional[str] = Field(default=None,alias="locale",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


