from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RetentionLabelSettings(BaseModel):
	behaviorDuringRetentionPeriod: Optional[SecurityBehaviorDuringRetentionPeriod | str] = Field(alias="behaviorDuringRetentionPeriod",default=None,)
	isContentUpdateAllowed: Optional[bool] = Field(alias="isContentUpdateAllowed",default=None,)
	isDeleteAllowed: Optional[bool] = Field(alias="isDeleteAllowed",default=None,)
	isLabelUpdateAllowed: Optional[bool] = Field(alias="isLabelUpdateAllowed",default=None,)
	isMetadataUpdateAllowed: Optional[bool] = Field(alias="isMetadataUpdateAllowed",default=None,)
	isRecordLocked: Optional[bool] = Field(alias="isRecordLocked",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_behavior_during_retention_period import SecurityBehaviorDuringRetentionPeriod

