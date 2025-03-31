from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PlannerCategoryDescriptions(BaseModel):
	category1: Optional[str] = Field(alias="category1", default=None,)
	category10: Optional[str] = Field(alias="category10", default=None,)
	category11: Optional[str] = Field(alias="category11", default=None,)
	category12: Optional[str] = Field(alias="category12", default=None,)
	category13: Optional[str] = Field(alias="category13", default=None,)
	category14: Optional[str] = Field(alias="category14", default=None,)
	category15: Optional[str] = Field(alias="category15", default=None,)
	category16: Optional[str] = Field(alias="category16", default=None,)
	category17: Optional[str] = Field(alias="category17", default=None,)
	category18: Optional[str] = Field(alias="category18", default=None,)
	category19: Optional[str] = Field(alias="category19", default=None,)
	category2: Optional[str] = Field(alias="category2", default=None,)
	category20: Optional[str] = Field(alias="category20", default=None,)
	category21: Optional[str] = Field(alias="category21", default=None,)
	category22: Optional[str] = Field(alias="category22", default=None,)
	category23: Optional[str] = Field(alias="category23", default=None,)
	category24: Optional[str] = Field(alias="category24", default=None,)
	category25: Optional[str] = Field(alias="category25", default=None,)
	category3: Optional[str] = Field(alias="category3", default=None,)
	category4: Optional[str] = Field(alias="category4", default=None,)
	category5: Optional[str] = Field(alias="category5", default=None,)
	category6: Optional[str] = Field(alias="category6", default=None,)
	category7: Optional[str] = Field(alias="category7", default=None,)
	category8: Optional[str] = Field(alias="category8", default=None,)
	category9: Optional[str] = Field(alias="category9", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

