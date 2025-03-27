from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SharePointIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.sharePointIdentity"] = Field(alias="@odata.type", default="#microsoft.graph.sharePointIdentity")
	loginName: Optional[str] = Field(alias="loginName", default=None,)


