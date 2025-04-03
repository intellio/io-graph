from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamworkPeripheral(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamworkPeripheral"] = Field(alias="@odata.type", default="#microsoft.graph.teamworkPeripheral")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	productId: Optional[str] = Field(alias="productId", default=None,)
	vendorId: Optional[str] = Field(alias="vendorId", default=None,)

