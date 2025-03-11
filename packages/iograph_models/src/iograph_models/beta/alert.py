from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Alert(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activityGroupName: Optional[str] = Field(alias="activityGroupName",default=None,)
	alertDetections: Optional[list[AlertDetection]] = Field(alias="alertDetections",default=None,)
	assignedTo: Optional[str] = Field(alias="assignedTo",default=None,)
	azureSubscriptionId: Optional[str] = Field(alias="azureSubscriptionId",default=None,)
	azureTenantId: Optional[str] = Field(alias="azureTenantId",default=None,)
	category: Optional[str] = Field(alias="category",default=None,)
	closedDateTime: Optional[datetime] = Field(alias="closedDateTime",default=None,)
	cloudAppStates: Optional[list[CloudAppSecurityState]] = Field(alias="cloudAppStates",default=None,)
	comments: Optional[list[str]] = Field(alias="comments",default=None,)
	confidence: Optional[int] = Field(alias="confidence",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	detectionIds: Optional[list[str]] = Field(alias="detectionIds",default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime",default=None,)
	feedback: Optional[AlertFeedback | str] = Field(alias="feedback",default=None,)
	fileStates: Optional[list[FileSecurityState]] = Field(alias="fileStates",default=None,)
	historyStates: Optional[list[AlertHistoryState]] = Field(alias="historyStates",default=None,)
	hostStates: Optional[list[HostSecurityState]] = Field(alias="hostStates",default=None,)
	incidentIds: Optional[list[str]] = Field(alias="incidentIds",default=None,)
	investigationSecurityStates: Optional[list[InvestigationSecurityState]] = Field(alias="investigationSecurityStates",default=None,)
	lastEventDateTime: Optional[datetime] = Field(alias="lastEventDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	malwareStates: Optional[list[MalwareState]] = Field(alias="malwareStates",default=None,)
	messageSecurityStates: Optional[list[MessageSecurityState]] = Field(alias="messageSecurityStates",default=None,)
	networkConnections: Optional[list[NetworkConnection]] = Field(alias="networkConnections",default=None,)
	processes: Optional[list[Process]] = Field(alias="processes",default=None,)
	recommendedActions: Optional[list[str]] = Field(alias="recommendedActions",default=None,)
	registryKeyStates: Optional[list[RegistryKeyState]] = Field(alias="registryKeyStates",default=None,)
	securityResources: Optional[list[SecurityResource]] = Field(alias="securityResources",default=None,)
	severity: Optional[AlertSeverity | str] = Field(alias="severity",default=None,)
	sourceMaterials: Optional[list[str]] = Field(alias="sourceMaterials",default=None,)
	status: Optional[AlertStatus | str] = Field(alias="status",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	triggers: Optional[list[AlertTrigger]] = Field(alias="triggers",default=None,)
	uriClickSecurityStates: Optional[list[UriClickSecurityState]] = Field(alias="uriClickSecurityStates",default=None,)
	userStates: Optional[list[UserSecurityState]] = Field(alias="userStates",default=None,)
	vendorInformation: Optional[SecurityVendorInformation] = Field(alias="vendorInformation",default=None,)
	vulnerabilityStates: Optional[list[VulnerabilityState]] = Field(alias="vulnerabilityStates",default=None,)

from .alert_detection import AlertDetection
from .cloud_app_security_state import CloudAppSecurityState
from .alert_feedback import AlertFeedback
from .file_security_state import FileSecurityState
from .alert_history_state import AlertHistoryState
from .host_security_state import HostSecurityState
from .investigation_security_state import InvestigationSecurityState
from .malware_state import MalwareState
from .message_security_state import MessageSecurityState
from .network_connection import NetworkConnection
from .process import Process
from .registry_key_state import RegistryKeyState
from .security_resource import SecurityResource
from .alert_severity import AlertSeverity
from .alert_status import AlertStatus
from .alert_trigger import AlertTrigger
from .uri_click_security_state import UriClickSecurityState
from .user_security_state import UserSecurityState
from .security_vendor_information import SecurityVendorInformation
from .vulnerability_state import VulnerabilityState

