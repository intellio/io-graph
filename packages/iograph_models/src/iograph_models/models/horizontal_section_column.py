from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HorizontalSectionColumn(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	width: Optional[int] = Field(alias="width",default=None,)
	webparts: SerializeAsAny[Optional[list[WebPart]]] = Field(alias="webparts",default=None,)

from .web_part import WebPart

