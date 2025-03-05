from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RetentionLabelSettings(BaseModel):
	behaviorDuringRetentionPeriod: Optional[SecurityBehaviorDuringRetentionPeriod] = Field(default=None,alias="behaviorDuringRetentionPeriod",)
	isContentUpdateAllowed: Optional[bool] = Field(default=None,alias="isContentUpdateAllowed",)
	isDeleteAllowed: Optional[bool] = Field(default=None,alias="isDeleteAllowed",)
	isLabelUpdateAllowed: Optional[bool] = Field(default=None,alias="isLabelUpdateAllowed",)
	isMetadataUpdateAllowed: Optional[bool] = Field(default=None,alias="isMetadataUpdateAllowed",)
	isRecordLocked: Optional[bool] = Field(default=None,alias="isRecordLocked",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_behavior_during_retention_period import SecurityBehaviorDuringRetentionPeriod

