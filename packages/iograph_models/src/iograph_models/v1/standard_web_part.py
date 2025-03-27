from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class StandardWebPart(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.standardWebPart"] = Field(alias="@odata.type", default="#microsoft.graph.standardWebPart")
	containerTextWebPartId: Optional[str] = Field(alias="containerTextWebPartId", default=None,)
	data: Optional[WebPartData] = Field(alias="data", default=None,)
	webPartType: Optional[str] = Field(alias="webPartType", default=None,)

from .web_part_data import WebPartData

