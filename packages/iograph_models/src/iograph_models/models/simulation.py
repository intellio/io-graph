from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Simulation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	attackTechnique: Optional[SimulationAttackTechnique] = Field(default=None,alias="attackTechnique",)
	attackType: Optional[SimulationAttackType] = Field(default=None,alias="attackType",)
	automationId: Optional[str] = Field(default=None,alias="automationId",)
	completionDateTime: Optional[datetime] = Field(default=None,alias="completionDateTime",)
	createdBy: Optional[EmailIdentity] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	durationInDays: Optional[int] = Field(default=None,alias="durationInDays",)
	endUserNotificationSetting: Optional[EndUserNotificationSetting] = Field(default=None,alias="endUserNotificationSetting",)
	excludedAccountTarget: Optional[AccountTargetContent] = Field(default=None,alias="excludedAccountTarget",)
	includedAccountTarget: Optional[AccountTargetContent] = Field(default=None,alias="includedAccountTarget",)
	isAutomated: Optional[bool] = Field(default=None,alias="isAutomated",)
	lastModifiedBy: Optional[EmailIdentity] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	launchDateTime: Optional[datetime] = Field(default=None,alias="launchDateTime",)
	oAuthConsentAppDetail: Optional[OAuthConsentAppDetail] = Field(default=None,alias="oAuthConsentAppDetail",)
	payloadDeliveryPlatform: Optional[PayloadDeliveryPlatform] = Field(default=None,alias="payloadDeliveryPlatform",)
	report: Optional[SimulationReport] = Field(default=None,alias="report",)
	status: Optional[SimulationStatus] = Field(default=None,alias="status",)
	trainingSetting: Optional[TrainingSetting] = Field(default=None,alias="trainingSetting",)
	landingPage: Optional[LandingPage] = Field(default=None,alias="landingPage",)
	loginPage: Optional[LoginPage] = Field(default=None,alias="loginPage",)
	payload: Optional[Payload] = Field(default=None,alias="payload",)

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

