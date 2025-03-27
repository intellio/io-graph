from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SoftwareOathAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.softwareOathAuthenticationMethod"] = Field(alias="@odata.type", default="#microsoft.graph.softwareOathAuthenticationMethod")
	secretKey: Optional[str] = Field(alias="secretKey", default=None,)


