from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class StrongAuthenticationDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.strongAuthenticationDetail"] = Field(alias="@odata.type", default="#microsoft.graph.strongAuthenticationDetail")
	encryptedPinHashHistory: Optional[str] = Field(alias="encryptedPinHashHistory", default=None,)
	proofupTime: Optional[int] = Field(alias="proofupTime", default=None,)

