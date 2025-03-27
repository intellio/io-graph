from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SyncPostRequest(BaseModel):
	syncType: Optional[DeviceManagementExchangeConnectorSyncType | str] = Field(alias="syncType", default=None,)

from .device_management_exchange_connector_sync_type import DeviceManagementExchangeConnectorSyncType

