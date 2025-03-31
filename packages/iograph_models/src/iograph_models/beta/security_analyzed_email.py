from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityAnalyzedEmail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.analyzedEmail"] = Field(alias="@odata.type",)
	alertIds: Optional[list[str]] = Field(alias="alertIds", default=None,)
	attachments: Optional[list[SecurityAnalyzedEmailAttachment]] = Field(alias="attachments", default=None,)
	authenticationDetails: Optional[SecurityAnalyzedEmailAuthenticationDetail] = Field(alias="authenticationDetails", default=None,)
	bulkComplaintLevel: Optional[str] = Field(alias="bulkComplaintLevel", default=None,)
	clientType: Optional[str] = Field(alias="clientType", default=None,)
	contexts: Optional[list[str]] = Field(alias="contexts", default=None,)
	detectionMethods: Optional[list[str]] = Field(alias="detectionMethods", default=None,)
	directionality: Optional[SecurityAntispamDirectionality | str] = Field(alias="directionality", default=None,)
	distributionList: Optional[str] = Field(alias="distributionList", default=None,)
	dlpRules: Optional[list[SecurityAnalyzedEmailDlpRuleInfo]] = Field(alias="dlpRules", default=None,)
	emailClusterId: Optional[str] = Field(alias="emailClusterId", default=None,)
	exchangeTransportRules: Optional[list[SecurityAnalyzedEmailExchangeTransportRuleInfo]] = Field(alias="exchangeTransportRules", default=None,)
	forwardingDetail: Optional[str] = Field(alias="forwardingDetail", default=None,)
	inboundConnectorFormattedName: Optional[str] = Field(alias="inboundConnectorFormattedName", default=None,)
	internetMessageId: Optional[str] = Field(alias="internetMessageId", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)
	latestDelivery: Optional[SecurityAnalyzedEmailDeliveryDetail] = Field(alias="latestDelivery", default=None,)
	loggedDateTime: Optional[datetime] = Field(alias="loggedDateTime", default=None,)
	networkMessageId: Optional[str] = Field(alias="networkMessageId", default=None,)
	originalDelivery: Optional[SecurityAnalyzedEmailDeliveryDetail] = Field(alias="originalDelivery", default=None,)
	overrideSources: Optional[list[str]] = Field(alias="overrideSources", default=None,)
	phishConfidenceLevel: Optional[str] = Field(alias="phishConfidenceLevel", default=None,)
	policy: Optional[str] = Field(alias="policy", default=None,)
	policyAction: Optional[str] = Field(alias="policyAction", default=None,)
	policyType: Optional[str] = Field(alias="policyType", default=None,)
	primaryOverrideSource: Optional[str] = Field(alias="primaryOverrideSource", default=None,)
	recipientDetail: Optional[SecurityAnalyzedEmailRecipientDetail] = Field(alias="recipientDetail", default=None,)
	recipientEmailAddress: Optional[str] = Field(alias="recipientEmailAddress", default=None,)
	returnPath: Optional[str] = Field(alias="returnPath", default=None,)
	senderDetail: Optional[SecurityAnalyzedEmailSenderDetail] = Field(alias="senderDetail", default=None,)
	sizeInBytes: Optional[int] = Field(alias="sizeInBytes", default=None,)
	spamConfidenceLevel: Optional[str] = Field(alias="spamConfidenceLevel", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	threatDetectionDetails: Optional[list[SecurityThreatDetectionDetail]] = Field(alias="threatDetectionDetails", default=None,)
	threatTypes: Optional[list[SecurityThreatType | str]] = Field(alias="threatTypes", default=None,)
	timelineEvents: Optional[list[SecurityTimelineEvent]] = Field(alias="timelineEvents", default=None,)
	urls: Optional[list[SecurityAnalyzedEmailUrl]] = Field(alias="urls", default=None,)

from .security_analyzed_email_attachment import SecurityAnalyzedEmailAttachment
from .security_analyzed_email_authentication_detail import SecurityAnalyzedEmailAuthenticationDetail
from .security_antispam_directionality import SecurityAntispamDirectionality
from .security_analyzed_email_dlp_rule_info import SecurityAnalyzedEmailDlpRuleInfo
from .security_analyzed_email_exchange_transport_rule_info import SecurityAnalyzedEmailExchangeTransportRuleInfo
from .security_analyzed_email_delivery_detail import SecurityAnalyzedEmailDeliveryDetail
from .security_analyzed_email_recipient_detail import SecurityAnalyzedEmailRecipientDetail
from .security_analyzed_email_sender_detail import SecurityAnalyzedEmailSenderDetail
from .security_threat_detection_detail import SecurityThreatDetectionDetail
from .security_threat_type import SecurityThreatType
from .security_timeline_event import SecurityTimelineEvent
from .security_analyzed_email_url import SecurityAnalyzedEmailUrl
