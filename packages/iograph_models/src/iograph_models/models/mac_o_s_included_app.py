from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSIncludedApp(BaseModel):
	bundleId: Optional[str] = Field(default=None,alias="bundleId",)
	bundleVersion: Optional[str] = Field(default=None,alias="bundleVersion",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


