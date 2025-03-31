from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SpecifiedCaptiveNetworkPlugins(BaseModel):
	allowedBundleIdentifiers: Optional[list[str]] = Field(alias="allowedBundleIdentifiers", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

