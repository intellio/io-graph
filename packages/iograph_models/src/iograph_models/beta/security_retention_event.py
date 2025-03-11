from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityRetentionEvent(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	eventPropagationResults: Optional[list[SecurityEventPropagationResult]] = Field(alias="eventPropagationResults",default=None,)
	eventQueries: Optional[list[SecurityEventQuery]] = Field(alias="eventQueries",default=None,)
	eventStatus: Optional[SecurityRetentionEventStatus] = Field(alias="eventStatus",default=None,)
	eventTriggerDateTime: Optional[datetime] = Field(alias="eventTriggerDateTime",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	lastStatusUpdateDateTime: Optional[datetime] = Field(alias="lastStatusUpdateDateTime",default=None,)
	retentionEventType: Optional[SecurityRetentionEventType] = Field(alias="retentionEventType",default=None,)

from .identity_set import IdentitySet
from .security_event_propagation_result import SecurityEventPropagationResult
from .security_event_query import SecurityEventQuery
from .security_retention_event_status import SecurityRetentionEventStatus
from .identity_set import IdentitySet
from .security_retention_event_type import SecurityRetentionEventType

