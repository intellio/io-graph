from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class BasicAuthentication(BaseModel):
	odata_type: Literal["#microsoft.graph.basicAuthentication"] = Field(alias="@odata.type", default="#microsoft.graph.basicAuthentication")
	password: Optional[str] = Field(alias="password", default=None,)
	username: Optional[str] = Field(alias="username", default=None,)


