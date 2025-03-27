from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EmbeddedSIMDeviceStateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EmbeddedSIMDeviceState]] = Field(alias="value", default=None,)

from .embedded_s_i_m_device_state import EmbeddedSIMDeviceState

