from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityNetworkAdapter(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.networkAdapter"] = Field(alias="@odata.type",)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)

