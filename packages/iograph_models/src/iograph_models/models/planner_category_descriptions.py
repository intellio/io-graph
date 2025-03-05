from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerCategoryDescriptions(BaseModel):
	category1: Optional[str] = Field(default=None,alias="category1",)
	category10: Optional[str] = Field(default=None,alias="category10",)
	category11: Optional[str] = Field(default=None,alias="category11",)
	category12: Optional[str] = Field(default=None,alias="category12",)
	category13: Optional[str] = Field(default=None,alias="category13",)
	category14: Optional[str] = Field(default=None,alias="category14",)
	category15: Optional[str] = Field(default=None,alias="category15",)
	category16: Optional[str] = Field(default=None,alias="category16",)
	category17: Optional[str] = Field(default=None,alias="category17",)
	category18: Optional[str] = Field(default=None,alias="category18",)
	category19: Optional[str] = Field(default=None,alias="category19",)
	category2: Optional[str] = Field(default=None,alias="category2",)
	category20: Optional[str] = Field(default=None,alias="category20",)
	category21: Optional[str] = Field(default=None,alias="category21",)
	category22: Optional[str] = Field(default=None,alias="category22",)
	category23: Optional[str] = Field(default=None,alias="category23",)
	category24: Optional[str] = Field(default=None,alias="category24",)
	category25: Optional[str] = Field(default=None,alias="category25",)
	category3: Optional[str] = Field(default=None,alias="category3",)
	category4: Optional[str] = Field(default=None,alias="category4",)
	category5: Optional[str] = Field(default=None,alias="category5",)
	category6: Optional[str] = Field(default=None,alias="category6",)
	category7: Optional[str] = Field(default=None,alias="category7",)
	category8: Optional[str] = Field(default=None,alias="category8",)
	category9: Optional[str] = Field(default=None,alias="category9",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


