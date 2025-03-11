from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcUserRoleScopeTagInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[CloudPcUserRoleScopeTagInfo]] = Field(alias="value",default=None,)

from .cloud_pc_user_role_scope_tag_info import CloudPcUserRoleScopeTagInfo

