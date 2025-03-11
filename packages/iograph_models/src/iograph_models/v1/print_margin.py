from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrintMargin(BaseModel):
	bottom: Optional[int] = Field(alias="bottom",default=None,)
	left: Optional[int] = Field(alias="left",default=None,)
	right: Optional[int] = Field(alias="right",default=None,)
	top: Optional[int] = Field(alias="top",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


