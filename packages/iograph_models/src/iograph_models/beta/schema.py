from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Schema(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.schema"] = Field(alias="@odata.type",)
	baseType: Optional[str] = Field(alias="baseType", default=None,)
	properties: Optional[list[Property]] = Field(alias="properties", default=None,)

from .property import Property
