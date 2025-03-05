from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HorizontalSectionColumn(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	width: Optional[int] = Field(default=None,alias="width",)
	webparts: SerializeAsAny[Optional[list[WebPart]]] = Field(default=None,alias="webparts",)

from .web_part import WebPart

