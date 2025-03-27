from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessUrl(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.url"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.url")
	value: Optional[str] = Field(alias="value", default=None,)


