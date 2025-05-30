from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSKernelExtension(BaseModel):
	bundleId: Optional[str] = Field(alias="bundleId", default=None,)
	teamIdentifier: Optional[str] = Field(alias="teamIdentifier", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

