from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SyncPostRequest(BaseModel):
	syncType: Optional[DeviceManagementExchangeConnectorSyncType] = Field(default=None,alias="syncType",)

from .device_management_exchange_connector_sync_type import DeviceManagementExchangeConnectorSyncType

