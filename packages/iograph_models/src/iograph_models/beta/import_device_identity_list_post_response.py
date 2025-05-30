from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Import_device_identity_listPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ImportedDeviceIdentityResult]] = Field(alias="value", default=None,)

from .imported_device_identity_result import ImportedDeviceIdentityResult
