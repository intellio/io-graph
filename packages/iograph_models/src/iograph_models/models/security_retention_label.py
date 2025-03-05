from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityRetentionLabel(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	actionAfterRetentionPeriod: Optional[SecurityActionAfterRetentionPeriod] = Field(default=None,alias="actionAfterRetentionPeriod",)
	behaviorDuringRetentionPeriod: Optional[SecurityBehaviorDuringRetentionPeriod] = Field(default=None,alias="behaviorDuringRetentionPeriod",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	defaultRecordBehavior: Optional[SecurityDefaultRecordBehavior] = Field(default=None,alias="defaultRecordBehavior",)
	descriptionForAdmins: Optional[str] = Field(default=None,alias="descriptionForAdmins",)
	descriptionForUsers: Optional[str] = Field(default=None,alias="descriptionForUsers",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isInUse: Optional[bool] = Field(default=None,alias="isInUse",)
	labelToBeApplied: Optional[str] = Field(default=None,alias="labelToBeApplied",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	retentionDuration: SerializeAsAny[Optional[SecurityRetentionDuration]] = Field(default=None,alias="retentionDuration",)
	retentionTrigger: Optional[SecurityRetentionTrigger] = Field(default=None,alias="retentionTrigger",)
	descriptors: Optional[SecurityFilePlanDescriptor] = Field(default=None,alias="descriptors",)
	dispositionReviewStages: Optional[list[SecurityDispositionReviewStage]] = Field(default=None,alias="dispositionReviewStages",)
	retentionEventType: Optional[SecurityRetentionEventType] = Field(default=None,alias="retentionEventType",)

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

