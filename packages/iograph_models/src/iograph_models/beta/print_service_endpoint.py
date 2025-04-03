from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PrintServiceEndpoint(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.printServiceEndpoint"] = Field(alias="@odata.type", default="#microsoft.graph.printServiceEndpoint")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	uri: Optional[str] = Field(alias="uri", default=None,)

