from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRelatedUser(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.relatedUser"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.relatedUser")
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)


