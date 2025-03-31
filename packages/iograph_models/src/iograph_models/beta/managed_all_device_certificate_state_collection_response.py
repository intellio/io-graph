from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedAllDeviceCertificateStateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ManagedAllDeviceCertificateState]] = Field(alias="value", default=None,)

from .managed_all_device_certificate_state import ManagedAllDeviceCertificateState
