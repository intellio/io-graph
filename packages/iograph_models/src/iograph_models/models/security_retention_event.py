from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityRetentionEvent(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	eventPropagationResults: Optional[list[SecurityEventPropagationResult]] = Field(default=None,alias="eventPropagationResults",)
	eventQueries: Optional[list[SecurityEventQuery]] = Field(default=None,alias="eventQueries",)
	eventStatus: Optional[SecurityRetentionEventStatus] = Field(default=None,alias="eventStatus",)
	eventTriggerDateTime: Optional[datetime] = Field(default=None,alias="eventTriggerDateTime",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	lastStatusUpdateDateTime: Optional[datetime] = Field(default=None,alias="lastStatusUpdateDateTime",)
	retentionEventType: Optional[SecurityRetentionEventType] = Field(default=None,alias="retentionEventType",)

from .identity_set import IdentitySet
from .security_event_propagation_result import SecurityEventPropagationResult
from .security_event_query import SecurityEventQuery
from .security_retention_event_status import SecurityRetentionEventStatus
from .identity_set import IdentitySet
from .security_retention_event_type import SecurityRetentionEventType

