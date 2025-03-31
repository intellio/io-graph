from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsKioskSingleUWPApp(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsKioskSingleUWPApp"] = Field(alias="@odata.type", default="#microsoft.graph.windowsKioskSingleUWPApp")
	uwpApp: Optional[WindowsKioskUWPApp] = Field(alias="uwpApp", default=None,)

from .windows_kiosk_u_w_p_app import WindowsKioskUWPApp
