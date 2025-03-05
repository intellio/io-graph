from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StandardWebPart(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	containerTextWebPartId: Optional[str] = Field(default=None,alias="containerTextWebPartId",)
	data: Optional[WebPartData] = Field(default=None,alias="data",)
	webPartType: Optional[str] = Field(default=None,alias="webPartType",)

from .web_part_data import WebPartData

