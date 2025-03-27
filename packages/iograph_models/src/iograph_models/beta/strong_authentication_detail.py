from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StrongAuthenticationDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	encryptedPinHashHistory: Optional[str] = Field(alias="encryptedPinHashHistory", default=None,)
	proofupTime: Optional[int] = Field(alias="proofupTime", default=None,)


