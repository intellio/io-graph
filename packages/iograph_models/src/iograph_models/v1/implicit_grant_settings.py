from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ImplicitGrantSettings(BaseModel):
	enableAccessTokenIssuance: Optional[bool] = Field(alias="enableAccessTokenIssuance", default=None,)
	enableIdTokenIssuance: Optional[bool] = Field(alias="enableIdTokenIssuance", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


