from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ConfigurationManagerClientHealthState(BaseModel):
	errorCode: Optional[int] = Field(alias="errorCode",default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime",default=None,)
	state: Optional[ConfigurationManagerClientState | str] = Field(alias="state",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .configuration_manager_client_state import ConfigurationManagerClientState

