from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TiIndicator(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.tiIndicator"] = Field(alias="@odata.type", default="#microsoft.graph.tiIndicator")
	action: Optional[TiAction | str] = Field(alias="action", default=None,)
	activityGroupNames: Optional[list[str]] = Field(alias="activityGroupNames", default=None,)
	additionalInformation: Optional[str] = Field(alias="additionalInformation", default=None,)
	azureTenantId: Optional[str] = Field(alias="azureTenantId", default=None,)
	confidence: Optional[int] = Field(alias="confidence", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	diamondModel: Optional[DiamondModel | str] = Field(alias="diamondModel", default=None,)
	domainName: Optional[str] = Field(alias="domainName", default=None,)
	emailEncoding: Optional[str] = Field(alias="emailEncoding", default=None,)
	emailLanguage: Optional[str] = Field(alias="emailLanguage", default=None,)
	emailRecipient: Optional[str] = Field(alias="emailRecipient", default=None,)
	emailSenderAddress: Optional[str] = Field(alias="emailSenderAddress", default=None,)
	emailSenderName: Optional[str] = Field(alias="emailSenderName", default=None,)
	emailSourceDomain: Optional[str] = Field(alias="emailSourceDomain", default=None,)
	emailSourceIpAddress: Optional[str] = Field(alias="emailSourceIpAddress", default=None,)
	emailSubject: Optional[str] = Field(alias="emailSubject", default=None,)
	emailXMailer: Optional[str] = Field(alias="emailXMailer", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	fileCompileDateTime: Optional[datetime] = Field(alias="fileCompileDateTime", default=None,)
	fileCreatedDateTime: Optional[datetime] = Field(alias="fileCreatedDateTime", default=None,)
	fileHashType: Optional[FileHashType | str] = Field(alias="fileHashType", default=None,)
	fileHashValue: Optional[str] = Field(alias="fileHashValue", default=None,)
	fileMutexName: Optional[str] = Field(alias="fileMutexName", default=None,)
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	filePacker: Optional[str] = Field(alias="filePacker", default=None,)
	filePath: Optional[str] = Field(alias="filePath", default=None,)
	fileSize: Optional[int] = Field(alias="fileSize", default=None,)
	fileType: Optional[str] = Field(alias="fileType", default=None,)
	ingestedDateTime: Optional[datetime] = Field(alias="ingestedDateTime", default=None,)
	isActive: Optional[bool] = Field(alias="isActive", default=None,)
	killChain: Optional[list[str]] = Field(alias="killChain", default=None,)
	knownFalsePositives: Optional[str] = Field(alias="knownFalsePositives", default=None,)
	lastReportedDateTime: Optional[datetime] = Field(alias="lastReportedDateTime", default=None,)
	malwareFamilyNames: Optional[list[str]] = Field(alias="malwareFamilyNames", default=None,)
	networkCidrBlock: Optional[str] = Field(alias="networkCidrBlock", default=None,)
	networkDestinationAsn: Optional[int] = Field(alias="networkDestinationAsn", default=None,)
	networkDestinationCidrBlock: Optional[str] = Field(alias="networkDestinationCidrBlock", default=None,)
	networkDestinationIPv4: Optional[str] = Field(alias="networkDestinationIPv4", default=None,)
	networkDestinationIPv6: Optional[str] = Field(alias="networkDestinationIPv6", default=None,)
	networkDestinationPort: Optional[int] = Field(alias="networkDestinationPort", default=None,)
	networkIPv4: Optional[str] = Field(alias="networkIPv4", default=None,)
	networkIPv6: Optional[str] = Field(alias="networkIPv6", default=None,)
	networkPort: Optional[int] = Field(alias="networkPort", default=None,)
	networkProtocol: Optional[int] = Field(alias="networkProtocol", default=None,)
	networkSourceAsn: Optional[int] = Field(alias="networkSourceAsn", default=None,)
	networkSourceCidrBlock: Optional[str] = Field(alias="networkSourceCidrBlock", default=None,)
	networkSourceIPv4: Optional[str] = Field(alias="networkSourceIPv4", default=None,)
	networkSourceIPv6: Optional[str] = Field(alias="networkSourceIPv6", default=None,)
	networkSourcePort: Optional[int] = Field(alias="networkSourcePort", default=None,)
	passiveOnly: Optional[bool] = Field(alias="passiveOnly", default=None,)
	severity: Optional[int] = Field(alias="severity", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	targetProduct: Optional[str] = Field(alias="targetProduct", default=None,)
	threatType: Optional[str] = Field(alias="threatType", default=None,)
	tlpLevel: Optional[TlpLevel | str] = Field(alias="tlpLevel", default=None,)
	url: Optional[str] = Field(alias="url", default=None,)
	userAgent: Optional[str] = Field(alias="userAgent", default=None,)

from .ti_action import TiAction
from .diamond_model import DiamondModel
from .file_hash_type import FileHashType
from .tlp_level import TlpLevel
