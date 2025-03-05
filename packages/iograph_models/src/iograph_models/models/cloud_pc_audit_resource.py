from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcAuditResource(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	modifiedProperties: Optional[list[CloudPcAuditProperty]] = Field(default=None,alias="modifiedProperties",)
	resourceId: Optional[str] = Field(default=None,alias="resourceId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .cloud_pc_audit_property import CloudPcAuditProperty

