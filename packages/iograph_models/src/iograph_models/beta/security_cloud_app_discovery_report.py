from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityCloudAppDiscoveryReport(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.cloudAppDiscoveryReport"] = Field(alias="@odata.type",)
	anonymizeMachineData: Optional[bool] = Field(alias="anonymizeMachineData", default=None,)
	anonymizeUserData: Optional[bool] = Field(alias="anonymizeUserData", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isSnapshotReport: Optional[bool] = Field(alias="isSnapshotReport", default=None,)
	lastDataReceivedDateTime: Optional[datetime] = Field(alias="lastDataReceivedDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	logDataProvider: Optional[SecurityLogDataProvider | str] = Field(alias="logDataProvider", default=None,)
	logFileCount: Optional[int] = Field(alias="logFileCount", default=None,)
	receiverProtocol: Optional[SecurityReceiverProtocol | str] = Field(alias="receiverProtocol", default=None,)
	supportedEntityTypes: Optional[list[SecurityEntityType | str]] = Field(alias="supportedEntityTypes", default=None,)
	supportedTrafficTypes: Optional[list[SecurityTrafficType | str]] = Field(alias="supportedTrafficTypes", default=None,)

from .security_log_data_provider import SecurityLogDataProvider
from .security_receiver_protocol import SecurityReceiverProtocol
from .security_entity_type import SecurityEntityType
from .security_traffic_type import SecurityTrafficType
