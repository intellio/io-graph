from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SourcedAttribute(BaseModel):
	odata_type: Literal["#microsoft.graph.sourcedAttribute"] = Field(alias="@odata.type", default="#microsoft.graph.sourcedAttribute")
	id: Optional[str] = Field(alias="id", default=None,)
	isExtensionAttribute: Optional[bool] = Field(alias="isExtensionAttribute", default=None,)
	source: Optional[str] = Field(alias="source", default=None,)


