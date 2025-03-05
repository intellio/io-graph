from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityRetentionLabel(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	actionAfterRetentionPeriod: Optional[SecurityActionAfterRetentionPeriod | str] = Field(alias="actionAfterRetentionPeriod",default=None,)
	behaviorDuringRetentionPeriod: Optional[SecurityBehaviorDuringRetentionPeriod | str] = Field(alias="behaviorDuringRetentionPeriod",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	defaultRecordBehavior: Optional[SecurityDefaultRecordBehavior | str] = Field(alias="defaultRecordBehavior",default=None,)
	descriptionForAdmins: Optional[str] = Field(alias="descriptionForAdmins",default=None,)
	descriptionForUsers: Optional[str] = Field(alias="descriptionForUsers",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isInUse: Optional[bool] = Field(alias="isInUse",default=None,)
	labelToBeApplied: Optional[str] = Field(alias="labelToBeApplied",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	retentionDuration: SerializeAsAny[Optional[SecurityRetentionDuration]] = Field(alias="retentionDuration",default=None,)
	retentionTrigger: Optional[SecurityRetentionTrigger | str] = Field(alias="retentionTrigger",default=None,)
	descriptors: Optional[SecurityFilePlanDescriptor] = Field(alias="descriptors",default=None,)
	dispositionReviewStages: Optional[list[SecurityDispositionReviewStage]] = Field(alias="dispositionReviewStages",default=None,)
	retentionEventType: Optional[SecurityRetentionEventType] = Field(alias="retentionEventType",default=None,)

from .security_action_after_retention_period import SecurityActionAfterRetentionPeriod
from .security_behavior_during_retention_period import SecurityBehaviorDuringRetentionPeriod
from .identity_set import IdentitySet
from .security_default_record_behavior import SecurityDefaultRecordBehavior
from .identity_set import IdentitySet
from .security_retention_duration import SecurityRetentionDuration
from .security_retention_trigger import SecurityRetentionTrigger
from .security_file_plan_descriptor import SecurityFilePlanDescriptor
from .security_disposition_review_stage import SecurityDispositionReviewStage
from .security_retention_event_type import SecurityRetentionEventType

