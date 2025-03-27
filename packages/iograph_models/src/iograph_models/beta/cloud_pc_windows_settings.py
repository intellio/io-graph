from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcWindowsSettings(BaseModel):
	language: Optional[str] = Field(alias="language", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


