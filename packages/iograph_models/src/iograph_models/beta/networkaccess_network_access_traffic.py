from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessNetworkAccessTraffic(BaseModel):
	action: Optional[NetworkaccessFilteringPolicyAction | str] = Field(alias="action",default=None,)
	agentVersion: Optional[str] = Field(alias="agentVersion",default=None,)
	applicationSnapshot: Optional[NetworkaccessApplicationSnapshot] = Field(alias="applicationSnapshot",default=None,)
	connectionId: Optional[str] = Field(alias="connectionId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	destinationFQDN: Optional[str] = Field(alias="destinationFQDN",default=None,)
	destinationIp: Optional[str] = Field(alias="destinationIp",default=None,)
	destinationPort: Optional[int] = Field(alias="destinationPort",default=None,)
	destinationUrl: Optional[str] = Field(alias="destinationUrl",default=None,)
	destinationWebCategory: Optional[NetworkaccessWebCategory] = Field(alias="destinationWebCategory",default=None,)
	deviceCategory: Optional[NetworkaccessDeviceCategory | str] = Field(alias="deviceCategory",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	deviceOperatingSystem: Optional[str] = Field(alias="deviceOperatingSystem",default=None,)
	deviceOperatingSystemVersion: Optional[str] = Field(alias="deviceOperatingSystemVersion",default=None,)
	filteringProfileId: Optional[str] = Field(alias="filteringProfileId",default=None,)
	filteringProfileName: Optional[str] = Field(alias="filteringProfileName",default=None,)
	headers: Optional[NetworkaccessHeaders] = Field(alias="headers",default=None,)
	httpMethod: Optional[NetworkaccessHttpMethod | str] = Field(alias="httpMethod",default=None,)
	initiatingProcessName: Optional[str] = Field(alias="initiatingProcessName",default=None,)
	networkProtocol: Optional[NetworkaccessNetworkingProtocol | str] = Field(alias="networkProtocol",default=None,)
	operationStatus: Optional[NetworkaccessNetworkTrafficOperationStatus | str] = Field(alias="operationStatus",default=None,)
	policyId: Optional[str] = Field(alias="policyId",default=None,)
	policyName: Optional[str] = Field(alias="policyName",default=None,)
	policyRuleId: Optional[str] = Field(alias="policyRuleId",default=None,)
	policyRuleName: Optional[str] = Field(alias="policyRuleName",default=None,)
	popProcessingRegion: Optional[str] = Field(alias="popProcessingRegion",default=None,)
	privateAccessDetails: Optional[NetworkaccessPrivateAccessDetails] = Field(alias="privateAccessDetails",default=None,)
	receivedBytes: Optional[int] = Field(alias="receivedBytes",default=None,)
	remoteNetworkId: Optional[str] = Field(alias="remoteNetworkId",default=None,)
	resourceTenantId: Optional[str] = Field(alias="resourceTenantId",default=None,)
	responseCode: Optional[int] = Field(alias="responseCode",default=None,)
	sentBytes: Optional[int] = Field(alias="sentBytes",default=None,)
	sessionId: Optional[str] = Field(alias="sessionId",default=None,)
	sourceIp: Optional[str] = Field(alias="sourceIp",default=None,)
	sourcePort: Optional[int] = Field(alias="sourcePort",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	threatType: Optional[str] = Field(alias="threatType",default=None,)
	trafficType: Optional[NetworkaccessTrafficType | str] = Field(alias="trafficType",default=None,)
	transactionId: Optional[str] = Field(alias="transactionId",default=None,)
	transportProtocol: Optional[NetworkaccessNetworkingProtocol | str] = Field(alias="transportProtocol",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	vendorNames: Optional[list[str]] = Field(alias="vendorNames",default=None,)
	device: Optional[Device] = Field(alias="device",default=None,)
	user: Optional[User] = Field(alias="user",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .networkaccess_filtering_policy_action import NetworkaccessFilteringPolicyAction
from .networkaccess_application_snapshot import NetworkaccessApplicationSnapshot
from .networkaccess_web_category import NetworkaccessWebCategory
from .networkaccess_device_category import NetworkaccessDeviceCategory
from .networkaccess_headers import NetworkaccessHeaders
from .networkaccess_http_method import NetworkaccessHttpMethod
from .networkaccess_networking_protocol import NetworkaccessNetworkingProtocol
from .networkaccess_network_traffic_operation_status import NetworkaccessNetworkTrafficOperationStatus
from .networkaccess_private_access_details import NetworkaccessPrivateAccessDetails
from .networkaccess_traffic_type import NetworkaccessTrafficType
from .networkaccess_networking_protocol import NetworkaccessNetworkingProtocol
from .device import Device
from .user import User

