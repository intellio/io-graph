from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CloudPcAuditEvent(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activity: Optional[str] = Field(default=None,alias="activity",)
	activityDateTime: Optional[datetime] = Field(default=None,alias="activityDateTime",)
	activityOperationType: Optional[CloudPcAuditActivityOperationType] = Field(default=None,alias="activityOperationType",)
	activityResult: Optional[CloudPcAuditActivityResult] = Field(default=None,alias="activityResult",)
	activityType: Optional[str] = Field(default=None,alias="activityType",)
	actor: Optional[CloudPcAuditActor] = Field(default=None,alias="actor",)
	category: Optional[CloudPcAuditCategory] = Field(default=None,alias="category",)
	componentName: Optional[str] = Field(default=None,alias="componentName",)
	correlationId: Optional[str] = Field(default=None,alias="correlationId",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	resources: list[CloudPcAuditResource] = Field(alias="resources",)

from .cloud_pc_audit_activity_operation_type import CloudPcAuditActivityOperationType
from .cloud_pc_audit_activity_result import CloudPcAuditActivityResult
from .cloud_pc_audit_actor import CloudPcAuditActor
from .cloud_pc_audit_category import CloudPcAuditCategory
from .cloud_pc_audit_resource import CloudPcAuditResource

