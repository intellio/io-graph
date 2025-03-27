from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskLocalUser(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsKioskLocalUser"] = Field(alias="@odata.type", default="#microsoft.graph.windowsKioskLocalUser")
	userName: Optional[str] = Field(alias="userName", default=None,)


