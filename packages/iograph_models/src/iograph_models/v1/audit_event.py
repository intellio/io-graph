from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AuditEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.auditEvent"] = Field(alias="@odata.type", default="#microsoft.graph.auditEvent")
	activity: Optional[str] = Field(alias="activity", default=None,)
	activityDateTime: Optional[datetime] = Field(alias="activityDateTime", default=None,)
	activityOperationType: Optional[str] = Field(alias="activityOperationType", default=None,)
	activityResult: Optional[str] = Field(alias="activityResult", default=None,)
	activityType: Optional[str] = Field(alias="activityType", default=None,)
	actor: Optional[AuditActor] = Field(alias="actor", default=None,)
	category: Optional[str] = Field(alias="category", default=None,)
	componentName: Optional[str] = Field(alias="componentName", default=None,)
	correlationId: Optional[UUID] = Field(alias="correlationId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	resources: Optional[list[AuditResource]] = Field(alias="resources", default=None,)

from .audit_actor import AuditActor
from .audit_resource import AuditResource
