from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DirectoryAudit(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activityDateTime: Optional[datetime] = Field(alias="activityDateTime",default=None,)
	activityDisplayName: Optional[str] = Field(alias="activityDisplayName",default=None,)
	additionalDetails: Optional[list[KeyValue]] = Field(alias="additionalDetails",default=None,)
	category: Optional[str] = Field(alias="category",default=None,)
	correlationId: Optional[str] = Field(alias="correlationId",default=None,)
	initiatedBy: Optional[AuditActivityInitiator] = Field(alias="initiatedBy",default=None,)
	loggedByService: Optional[str] = Field(alias="loggedByService",default=None,)
	operationType: Optional[str] = Field(alias="operationType",default=None,)
	result: Optional[str | OperationResult] = Field(alias="result",default=None,)
	resultReason: Optional[str] = Field(alias="resultReason",default=None,)
	targetResources: Optional[list[TargetResource]] = Field(alias="targetResources",default=None,)

from .key_value import KeyValue
from .audit_activity_initiator import AuditActivityInitiator
from .operation_result import OperationResult
from .target_resource import TargetResource

