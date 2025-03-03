from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuditResource(BaseModel):
	auditResourceType: Optional[str] = Field(default=None,alias="auditResourceType",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	modifiedProperties: Optional[list[AuditProperty]] = Field(default=None,alias="modifiedProperties",)
	resourceId: Optional[str] = Field(default=None,alias="resourceId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .audit_property import AuditProperty

