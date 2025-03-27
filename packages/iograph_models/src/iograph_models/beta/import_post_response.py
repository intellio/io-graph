from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ImportPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ImportedWindowsAutopilotDeviceIdentity]] = Field(alias="value", default=None,)

from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity

