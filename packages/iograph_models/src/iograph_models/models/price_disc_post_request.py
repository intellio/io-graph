from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Price_discPostRequest(BaseModel):
	settlement: Optional[str] = Field(default=None,alias="settlement",)
	maturity: Optional[str] = Field(default=None,alias="maturity",)
	discount: Optional[str] = Field(default=None,alias="discount",)
	redemption: Optional[str] = Field(default=None,alias="redemption",)
	basis: Optional[str] = Field(default=None,alias="basis",)


