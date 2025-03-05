from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VerticalSection(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	emphasis: Optional[str | SectionEmphasisType] = Field(alias="emphasis",default=None,)
	webparts: SerializeAsAny[Optional[list[WebPart]]] = Field(alias="webparts",default=None,)

from .section_emphasis_type import SectionEmphasisType
from .web_part import WebPart

