from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DirectoryAudit(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activityDateTime: Optional[datetime] = Field(default=None,alias="activityDateTime",)
	activityDisplayName: Optional[str] = Field(default=None,alias="activityDisplayName",)
	additionalDetails: list[KeyValue] = Field(alias="additionalDetails",)
	category: Optional[str] = Field(default=None,alias="category",)
	correlationId: Optional[str] = Field(default=None,alias="correlationId",)
	initiatedBy: Optional[AuditActivityInitiator] = Field(default=None,alias="initiatedBy",)
	loggedByService: Optional[str] = Field(default=None,alias="loggedByService",)
	operationType: Optional[str] = Field(default=None,alias="operationType",)
	result: Optional[OperationResult] = Field(default=None,alias="result",)
	resultReason: Optional[str] = Field(default=None,alias="resultReason",)
	targetResources: list[TargetResource] = Field(alias="targetResources",)

from .key_value import KeyValue
from .audit_activity_initiator import AuditActivityInitiator
from .operation_result import OperationResult
from .target_resource import TargetResource

