from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcUserRoleScopeTagInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CloudPcUserRoleScopeTagInfo]] = Field(default=None,alias="value",)

from .cloud_pc_user_role_scope_tag_info import CloudPcUserRoleScopeTagInfo

