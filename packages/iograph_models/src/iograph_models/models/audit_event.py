from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AuditEvent(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activity: Optional[str] = Field(default=None,alias="activity",)
	activityDateTime: Optional[datetime] = Field(default=None,alias="activityDateTime",)
	activityOperationType: Optional[str] = Field(default=None,alias="activityOperationType",)
	activityResult: Optional[str] = Field(default=None,alias="activityResult",)
	activityType: Optional[str] = Field(default=None,alias="activityType",)
	actor: Optional[AuditActor] = Field(default=None,alias="actor",)
	category: Optional[str] = Field(default=None,alias="category",)
	componentName: Optional[str] = Field(default=None,alias="componentName",)
	correlationId: Optional[UUID] = Field(default=None,alias="correlationId",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	resources: list[AuditResource] = Field(alias="resources",)

from .audit_actor import AuditActor
from .audit_resource import AuditResource

