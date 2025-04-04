from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityEmailThreatSubmissionPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.emailThreatSubmissionPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.security.emailThreatSubmissionPolicy")
	customizedNotificationSenderEmailAddress: Optional[str] = Field(alias="customizedNotificationSenderEmailAddress", default=None,)
	customizedReportRecipientEmailAddress: Optional[str] = Field(alias="customizedReportRecipientEmailAddress", default=None,)
	isAlwaysReportEnabledForUsers: Optional[bool] = Field(alias="isAlwaysReportEnabledForUsers", default=None,)
	isAskMeEnabledForUsers: Optional[bool] = Field(alias="isAskMeEnabledForUsers", default=None,)
	isCustomizedMessageEnabled: Optional[bool] = Field(alias="isCustomizedMessageEnabled", default=None,)
	isCustomizedMessageEnabledForPhishing: Optional[bool] = Field(alias="isCustomizedMessageEnabledForPhishing", default=None,)
	isCustomizedNotificationSenderEnabled: Optional[bool] = Field(alias="isCustomizedNotificationSenderEnabled", default=None,)
	isNeverReportEnabledForUsers: Optional[bool] = Field(alias="isNeverReportEnabledForUsers", default=None,)
	isOrganizationBrandingEnabled: Optional[bool] = Field(alias="isOrganizationBrandingEnabled", default=None,)
	isReportFromQuarantineEnabled: Optional[bool] = Field(alias="isReportFromQuarantineEnabled", default=None,)
	isReportToCustomizedEmailAddressEnabled: Optional[bool] = Field(alias="isReportToCustomizedEmailAddressEnabled", default=None,)
	isReportToMicrosoftEnabled: Optional[bool] = Field(alias="isReportToMicrosoftEnabled", default=None,)
	isReviewEmailNotificationEnabled: Optional[bool] = Field(alias="isReviewEmailNotificationEnabled", default=None,)

