from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookRangeBorder(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	color: Optional[str] = Field(default=None,alias="color",)
	sideIndex: Optional[str] = Field(default=None,alias="sideIndex",)
	style: Optional[str] = Field(default=None,alias="style",)
	weight: Optional[str] = Field(default=None,alias="weight",)


