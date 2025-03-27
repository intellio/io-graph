from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskAutologon(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsKioskAutologon"] = Field(alias="@odata.type", default="#microsoft.graph.windowsKioskAutologon")


