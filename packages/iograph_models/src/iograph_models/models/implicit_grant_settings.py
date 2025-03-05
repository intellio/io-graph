from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ImplicitGrantSettings(BaseModel):
	enableAccessTokenIssuance: Optional[bool] = Field(default=None,alias="enableAccessTokenIssuance",)
	enableIdTokenIssuance: Optional[bool] = Field(default=None,alias="enableIdTokenIssuance",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


