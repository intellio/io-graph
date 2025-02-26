from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementExchangeConnector(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	connectorServerName: Optional[str] = Field(default=None,alias="connectorServerName",)
	exchangeAlias: Optional[str] = Field(default=None,alias="exchangeAlias",)
	exchangeConnectorType: Optional[DeviceManagementExchangeConnectorType] = Field(default=None,alias="exchangeConnectorType",)
	exchangeOrganization: Optional[str] = Field(default=None,alias="exchangeOrganization",)
	lastSyncDateTime: Optional[datetime] = Field(default=None,alias="lastSyncDateTime",)
	primarySmtpAddress: Optional[str] = Field(default=None,alias="primarySmtpAddress",)
	serverName: Optional[str] = Field(default=None,alias="serverName",)
	status: Optional[DeviceManagementExchangeConnectorStatus] = Field(default=None,alias="status",)
	version: Optional[str] = Field(default=None,alias="version",)

from .device_management_exchange_connector_type import DeviceManagementExchangeConnectorType
from .device_management_exchange_connector_status import DeviceManagementExchangeConnectorStatus

