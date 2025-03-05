from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Sharepoint(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	settings: Optional[SharepointSettings] = Field(default=None,alias="settings",)

from .sharepoint_settings import SharepointSettings

