from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUniversalAppXContainedApp(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUniversalAppXContainedApp"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUniversalAppXContainedApp")
	appUserModelId: Optional[str] = Field(alias="appUserModelId", default=None,)


