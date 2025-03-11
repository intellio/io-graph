from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AddWatermark(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	fontColor: Optional[str] = Field(alias="fontColor",default=None,)
	fontSize: Optional[int] = Field(alias="fontSize",default=None,)
	text: Optional[str] = Field(alias="text",default=None,)
	orientation: Optional[PageOrientation | str] = Field(alias="orientation",default=None,)

from .page_orientation import PageOrientation

