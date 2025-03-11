from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcAuditResource(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	modifiedProperties: Optional[list[CloudPcAuditProperty]] = Field(alias="modifiedProperties",default=None,)
	resourceId: Optional[str] = Field(alias="resourceId",default=None,)
	resourceType: Optional[str] = Field(alias="resourceType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .cloud_pc_audit_property import CloudPcAuditProperty

