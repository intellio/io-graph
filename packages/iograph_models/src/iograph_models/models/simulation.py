from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Simulation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	attackTechnique: Optional[str | SimulationAttackTechnique] = Field(alias="attackTechnique",default=None,)
	attackType: Optional[str | SimulationAttackType] = Field(alias="attackType",default=None,)
	automationId: Optional[str] = Field(alias="automationId",default=None,)
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime",default=None,)
	createdBy: Optional[EmailIdentity] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	durationInDays: Optional[int] = Field(alias="durationInDays",default=None,)
	endUserNotificationSetting: SerializeAsAny[Optional[EndUserNotificationSetting]] = Field(alias="endUserNotificationSetting",default=None,)
	excludedAccountTarget: SerializeAsAny[Optional[AccountTargetContent]] = Field(alias="excludedAccountTarget",default=None,)
	includedAccountTarget: SerializeAsAny[Optional[AccountTargetContent]] = Field(alias="includedAccountTarget",default=None,)
	isAutomated: Optional[bool] = Field(alias="isAutomated",default=None,)
	lastModifiedBy: Optional[EmailIdentity] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	launchDateTime: Optional[datetime] = Field(alias="launchDateTime",default=None,)
	oAuthConsentAppDetail: Optional[OAuthConsentAppDetail] = Field(alias="oAuthConsentAppDetail",default=None,)
	payloadDeliveryPlatform: Optional[str | PayloadDeliveryPlatform] = Field(alias="payloadDeliveryPlatform",default=None,)
	report: Optional[SimulationReport] = Field(alias="report",default=None,)
	status: Optional[str | SimulationStatus] = Field(alias="status",default=None,)
	trainingSetting: SerializeAsAny[Optional[TrainingSetting]] = Field(alias="trainingSetting",default=None,)
	landingPage: Optional[LandingPage] = Field(alias="landingPage",default=None,)
	loginPage: Optional[LoginPage] = Field(alias="loginPage",default=None,)
	payload: Optional[Payload] = Field(alias="payload",default=None,)

from .simulation_attack_technique import SimulationAttackTechnique
from .simulation_attack_type import SimulationAttackType
from .email_identity import EmailIdentity
from .end_user_notification_setting import EndUserNotificationSetting
from .account_target_content import AccountTargetContent
from .account_target_content import AccountTargetContent
from .email_identity import EmailIdentity
from .o_auth_consent_app_detail import OAuthConsentAppDetail
from .payload_delivery_platform import PayloadDeliveryPlatform
from .simulation_report import SimulationReport
from .simulation_status import SimulationStatus
from .training_setting import TrainingSetting
from .landing_page import LandingPage
from .login_page import LoginPage
from .payload import Payload

