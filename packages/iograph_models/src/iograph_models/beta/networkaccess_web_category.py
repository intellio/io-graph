from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessWebCategory(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.webCategory"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.webCategory")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	group: Optional[str] = Field(alias="group", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)


