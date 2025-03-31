from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Sharepoint(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.sharepoint"] = Field(alias="@odata.type",)
	settings: Optional[SharepointSettings] = Field(alias="settings", default=None,)

from .sharepoint_settings import SharepointSettings
