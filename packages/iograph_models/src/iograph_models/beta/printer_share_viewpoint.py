from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrinterShareViewpoint(BaseModel):
	lastUsedDateTime: Optional[datetime] = Field(alias="lastUsedDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


