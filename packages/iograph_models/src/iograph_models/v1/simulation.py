from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Simulation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	attackTechnique: Optional[SimulationAttackTechnique | str] = Field(alias="attackTechnique", default=None,)
	attackType: Optional[SimulationAttackType | str] = Field(alias="attackType", default=None,)
	automationId: Optional[str] = Field(alias="automationId", default=None,)
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime", default=None,)
	createdBy: Optional[EmailIdentity] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	durationInDays: Optional[int] = Field(alias="durationInDays", default=None,)
	endUserNotificationSetting: Optional[Union[NoTrainingNotificationSetting, TrainingNotificationSetting]] = Field(alias="endUserNotificationSetting", default=None,discriminator="odata_type", )
	excludedAccountTarget: Optional[Union[AddressBookAccountTargetContent, IncludeAllAccountTargetContent]] = Field(alias="excludedAccountTarget", default=None,discriminator="odata_type", )
	includedAccountTarget: Optional[Union[AddressBookAccountTargetContent, IncludeAllAccountTargetContent]] = Field(alias="includedAccountTarget", default=None,discriminator="odata_type", )
	isAutomated: Optional[bool] = Field(alias="isAutomated", default=None,)
	lastModifiedBy: Optional[EmailIdentity] = Field(alias="lastModifiedBy", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	launchDateTime: Optional[datetime] = Field(alias="launchDateTime", default=None,)
	oAuthConsentAppDetail: Optional[OAuthConsentAppDetail] = Field(alias="oAuthConsentAppDetail", default=None,)
	payloadDeliveryPlatform: Optional[PayloadDeliveryPlatform | str] = Field(alias="payloadDeliveryPlatform", default=None,)
	report: Optional[SimulationReport] = Field(alias="report", default=None,)
	status: Optional[SimulationStatus | str] = Field(alias="status", default=None,)
	trainingSetting: Optional[Union[CustomTrainingSetting, MicrosoftCustomTrainingSetting, MicrosoftManagedTrainingSetting, MicrosoftTrainingAssignmentMapping, NoTrainingSetting]] = Field(alias="trainingSetting", default=None,discriminator="odata_type", )
	landingPage: Optional[LandingPage] = Field(alias="landingPage", default=None,)
	loginPage: Optional[LoginPage] = Field(alias="loginPage", default=None,)
	payload: Optional[Payload] = Field(alias="payload", default=None,)

from .simulation_attack_technique import SimulationAttackTechnique
from .simulation_attack_type import SimulationAttackType
from .email_identity import EmailIdentity
from .no_training_notification_setting import NoTrainingNotificationSetting
from .training_notification_setting import TrainingNotificationSetting
from .address_book_account_target_content import AddressBookAccountTargetContent
from .include_all_account_target_content import IncludeAllAccountTargetContent
from .address_book_account_target_content import AddressBookAccountTargetContent
from .include_all_account_target_content import IncludeAllAccountTargetContent
from .email_identity import EmailIdentity
from .o_auth_consent_app_detail import OAuthConsentAppDetail
from .payload_delivery_platform import PayloadDeliveryPlatform
from .simulation_report import SimulationReport
from .simulation_status import SimulationStatus
from .custom_training_setting import CustomTrainingSetting
from .microsoft_custom_training_setting import MicrosoftCustomTrainingSetting
from .microsoft_managed_training_setting import MicrosoftManagedTrainingSetting
from .microsoft_training_assignment_mapping import MicrosoftTrainingAssignmentMapping
from .no_training_setting import NoTrainingSetting
from .landing_page import LandingPage
from .login_page import LoginPage
from .payload import Payload

