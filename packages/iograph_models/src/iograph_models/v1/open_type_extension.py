from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class OpenTypeExtension(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.openTypeExtension"] = Field(alias="@odata.type", default="#microsoft.graph.openTypeExtension")
	extensionName: Optional[str] = Field(alias="extensionName", default=None,)


