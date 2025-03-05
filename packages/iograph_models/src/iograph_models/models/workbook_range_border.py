from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookRangeBorder(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	color: Optional[str] = Field(alias="color",default=None,)
	sideIndex: Optional[str] = Field(alias="sideIndex",default=None,)
	style: Optional[str] = Field(alias="style",default=None,)
	weight: Optional[str] = Field(alias="weight",default=None,)


