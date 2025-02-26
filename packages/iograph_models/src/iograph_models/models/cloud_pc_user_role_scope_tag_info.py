from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcUserRoleScopeTagInfo(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	roleScopeTagId: Optional[str] = Field(default=None,alias="roleScopeTagId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


