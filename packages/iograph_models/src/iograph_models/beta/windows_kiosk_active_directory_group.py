from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskActiveDirectoryGroup(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsKioskActiveDirectoryGroup"] = Field(alias="@odata.type", default="#microsoft.graph.windowsKioskActiveDirectoryGroup")
	groupName: Optional[str] = Field(alias="groupName", default=None,)


