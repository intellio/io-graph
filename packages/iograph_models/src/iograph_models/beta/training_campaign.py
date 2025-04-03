from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TrainingCampaign(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.trainingCampaign"] = Field(alias="@odata.type", default="#microsoft.graph.trainingCampaign")
	campaignSchedule: Optional[CampaignSchedule] = Field(alias="campaignSchedule", default=None,)
	createdBy: Optional[EmailIdentity] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endUserNotificationSetting: Optional[Union[NoTrainingNotificationSetting, TrainingNotificationSetting]] = Field(alias="endUserNotificationSetting", default=None,discriminator="odata_type", )
	excludedAccountTarget: Optional[Union[AddressBookAccountTargetContent, IncludeAllAccountTargetContent]] = Field(alias="excludedAccountTarget", default=None,discriminator="odata_type", )
	includedAccountTarget: Optional[Union[AddressBookAccountTargetContent, IncludeAllAccountTargetContent]] = Field(alias="includedAccountTarget", default=None,discriminator="odata_type", )
	lastModifiedBy: Optional[EmailIdentity] = Field(alias="lastModifiedBy", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	report: Optional[TrainingCampaignReport] = Field(alias="report", default=None,)
	trainingSetting: Optional[Union[CustomTrainingSetting, MicrosoftCustomTrainingSetting, MicrosoftManagedTrainingSetting, MicrosoftTrainingAssignmentMapping, NoTrainingSetting]] = Field(alias="trainingSetting", default=None,discriminator="odata_type", )

from .campaign_schedule import CampaignSchedule
from .email_identity import EmailIdentity
from .no_training_notification_setting import NoTrainingNotificationSetting
from .training_notification_setting import TrainingNotificationSetting
from .address_book_account_target_content import AddressBookAccountTargetContent
from .include_all_account_target_content import IncludeAllAccountTargetContent
from .training_campaign_report import TrainingCampaignReport
from .custom_training_setting import CustomTrainingSetting
from .microsoft_custom_training_setting import MicrosoftCustomTrainingSetting
from .microsoft_managed_training_setting import MicrosoftManagedTrainingSetting
from .microsoft_training_assignment_mapping import MicrosoftTrainingAssignmentMapping
from .no_training_setting import NoTrainingSetting
