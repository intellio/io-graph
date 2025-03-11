from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Import_apple_device_identity_listPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ImportedAppleDeviceIdentityResult]] = Field(alias="value",default=None,)

from .imported_apple_device_identity_result import ImportedAppleDeviceIdentityResult

