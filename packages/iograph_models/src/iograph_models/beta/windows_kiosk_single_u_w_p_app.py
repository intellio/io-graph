from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskSingleUWPApp(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	uwpApp: Optional[WindowsKioskUWPApp] = Field(alias="uwpApp",default=None,)

from .windows_kiosk_u_w_p_app import WindowsKioskUWPApp

