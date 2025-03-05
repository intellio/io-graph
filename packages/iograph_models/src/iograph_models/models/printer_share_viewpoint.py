from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrinterShareViewpoint(BaseModel):
	lastUsedDateTime: Optional[datetime] = Field(default=None,alias="lastUsedDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


