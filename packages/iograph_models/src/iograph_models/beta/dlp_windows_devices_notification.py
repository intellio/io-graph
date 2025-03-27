from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DlpWindowsDevicesNotification(BaseModel):
	author: Optional[str] = Field(alias="author", default=None,)
	odata_type: Literal["#microsoft.graph.dlpWindowsDevicesNotification"] = Field(alias="@odata.type", default="#microsoft.graph.dlpWindowsDevicesNotification")
	contentName: Optional[str] = Field(alias="contentName", default=None,)
	lastModfiedBy: Optional[str] = Field(alias="lastModfiedBy", default=None,)


