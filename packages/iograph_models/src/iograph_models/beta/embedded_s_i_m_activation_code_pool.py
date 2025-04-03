from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EmbeddedSIMActivationCodePool(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.embeddedSIMActivationCodePool"] = Field(alias="@odata.type", default="#microsoft.graph.embeddedSIMActivationCodePool")
	activationCodeCount: Optional[int] = Field(alias="activationCodeCount", default=None,)
	activationCodes: Optional[list[EmbeddedSIMActivationCode]] = Field(alias="activationCodes", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	assignments: Optional[list[EmbeddedSIMActivationCodePoolAssignment]] = Field(alias="assignments", default=None,)
	deviceStates: Optional[list[EmbeddedSIMDeviceState]] = Field(alias="deviceStates", default=None,)

from .embedded_s_i_m_activation_code import EmbeddedSIMActivationCode
from .embedded_s_i_m_activation_code_pool_assignment import EmbeddedSIMActivationCodePoolAssignment
from .embedded_s_i_m_device_state import EmbeddedSIMDeviceState
