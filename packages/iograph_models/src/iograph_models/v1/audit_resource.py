from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuditResource(BaseModel):
	auditResourceType: Optional[str] = Field(alias="auditResourceType",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	modifiedProperties: Optional[list[AuditProperty]] = Field(alias="modifiedProperties",default=None,)
	resourceId: Optional[str] = Field(alias="resourceId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .audit_property import AuditProperty

