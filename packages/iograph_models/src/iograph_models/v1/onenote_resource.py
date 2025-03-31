from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OnenoteResource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.onenoteResource"] = Field(alias="@odata.type", default="#microsoft.graph.onenoteResource")
	self: Optional[str] = Field(alias="self", default=None,)
	content: Optional[str] = Field(alias="content", default=None,)
	contentUrl: Optional[str] = Field(alias="contentUrl", default=None,)

