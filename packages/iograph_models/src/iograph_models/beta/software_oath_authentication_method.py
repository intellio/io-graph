from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SoftwareOathAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.softwareOathAuthenticationMethod"] = Field(alias="@odata.type", default="#microsoft.graph.softwareOathAuthenticationMethod")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	secretKey: Optional[str] = Field(alias="secretKey", default=None,)


