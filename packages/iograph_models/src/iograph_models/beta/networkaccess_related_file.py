from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessRelatedFile(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.relatedFile"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.relatedFile")
	directory: Optional[str] = Field(alias="directory", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	sizeInBytes: Optional[int] = Field(alias="sizeInBytes", default=None,)

