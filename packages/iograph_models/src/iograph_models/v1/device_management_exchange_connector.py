from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementExchangeConnector(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementExchangeConnector"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementExchangeConnector")
	connectorServerName: Optional[str] = Field(alias="connectorServerName", default=None,)
	exchangeAlias: Optional[str] = Field(alias="exchangeAlias", default=None,)
	exchangeConnectorType: Optional[DeviceManagementExchangeConnectorType | str] = Field(alias="exchangeConnectorType", default=None,)
	exchangeOrganization: Optional[str] = Field(alias="exchangeOrganization", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	primarySmtpAddress: Optional[str] = Field(alias="primarySmtpAddress", default=None,)
	serverName: Optional[str] = Field(alias="serverName", default=None,)
	status: Optional[DeviceManagementExchangeConnectorStatus | str] = Field(alias="status", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)

from .device_management_exchange_connector_type import DeviceManagementExchangeConnectorType
from .device_management_exchange_connector_status import DeviceManagementExchangeConnectorStatus
