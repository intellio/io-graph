from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TrainingCampaign(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	campaignSchedule: Optional[CampaignSchedule] = Field(alias="campaignSchedule",default=None,)
	createdBy: Optional[EmailIdentity] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	endUserNotificationSetting: SerializeAsAny[Optional[EndUserNotificationSetting]] = Field(alias="endUserNotificationSetting",default=None,)
	excludedAccountTarget: SerializeAsAny[Optional[AccountTargetContent]] = Field(alias="excludedAccountTarget",default=None,)
	includedAccountTarget: SerializeAsAny[Optional[AccountTargetContent]] = Field(alias="includedAccountTarget",default=None,)
	lastModifiedBy: Optional[EmailIdentity] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	report: Optional[TrainingCampaignReport] = Field(alias="report",default=None,)
	trainingSetting: SerializeAsAny[Optional[TrainingSetting]] = Field(alias="trainingSetting",default=None,)

from .campaign_schedule import CampaignSchedule
from .email_identity import EmailIdentity
from .end_user_notification_setting import EndUserNotificationSetting
from .account_target_content import AccountTargetContent
from .account_target_content import AccountTargetContent
from .email_identity import EmailIdentity
from .training_campaign_report import TrainingCampaignReport
from .training_setting import TrainingSetting

