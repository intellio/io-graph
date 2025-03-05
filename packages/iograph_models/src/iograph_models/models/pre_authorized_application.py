from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PreAuthorizedApplication(BaseModel):
	appId: Optional[str] = Field(default=None,alias="appId",)
	delegatedPermissionIds: Optional[list[str]] = Field(default=None,alias="delegatedPermissionIds",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


