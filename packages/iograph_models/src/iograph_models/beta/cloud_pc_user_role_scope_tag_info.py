from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcUserRoleScopeTagInfo(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	roleScopeTagId: Optional[str] = Field(alias="roleScopeTagId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

