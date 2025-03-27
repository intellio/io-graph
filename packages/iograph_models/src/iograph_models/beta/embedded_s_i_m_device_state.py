from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EmbeddedSIMDeviceState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	state: Optional[EmbeddedSIMDeviceStateValue | str] = Field(alias="state", default=None,)
	stateDetails: Optional[str] = Field(alias="stateDetails", default=None,)
	universalIntegratedCircuitCardIdentifier: Optional[str] = Field(alias="universalIntegratedCircuitCardIdentifier", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)

from .embedded_s_i_m_device_state_value import EmbeddedSIMDeviceStateValue

