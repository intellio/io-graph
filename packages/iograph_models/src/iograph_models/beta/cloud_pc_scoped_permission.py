from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcScopedPermission(BaseModel):
	permission: Optional[str] = Field(alias="permission",default=None,)
	scopeIds: Optional[list[str]] = Field(alias="scopeIds",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


