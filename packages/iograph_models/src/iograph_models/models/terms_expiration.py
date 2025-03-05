from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TermsExpiration(BaseModel):
	frequency: Optional[str] = Field(default=None,alias="frequency",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


