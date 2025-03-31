from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CloudPcAuditEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcAuditEvent"] = Field(alias="@odata.type",)
	activity: Optional[str] = Field(alias="activity", default=None,)
	activityDateTime: Optional[datetime] = Field(alias="activityDateTime", default=None,)
	activityOperationType: Optional[CloudPcAuditActivityOperationType | str] = Field(alias="activityOperationType", default=None,)
	activityResult: Optional[CloudPcAuditActivityResult | str] = Field(alias="activityResult", default=None,)
	activityType: Optional[str] = Field(alias="activityType", default=None,)
	actor: Optional[CloudPcAuditActor] = Field(alias="actor", default=None,)
	category: Optional[CloudPcAuditCategory | str] = Field(alias="category", default=None,)
	componentName: Optional[str] = Field(alias="componentName", default=None,)
	correlationId: Optional[str] = Field(alias="correlationId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	resources: Optional[list[CloudPcAuditResource]] = Field(alias="resources", default=None,)

from .cloud_pc_audit_activity_operation_type import CloudPcAuditActivityOperationType
from .cloud_pc_audit_activity_result import CloudPcAuditActivityResult
from .cloud_pc_audit_actor import CloudPcAuditActor
from .cloud_pc_audit_category import CloudPcAuditCategory
from .cloud_pc_audit_resource import CloudPcAuditResource
