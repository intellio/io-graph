from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ImportedWindowsAutopilotDeviceIdentityCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[ImportedWindowsAutopilotDeviceIdentity]] = Field(default=None,alias="value",)

from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity

