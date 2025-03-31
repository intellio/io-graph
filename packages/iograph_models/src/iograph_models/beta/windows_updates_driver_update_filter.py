from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class WindowsUpdatesDriverUpdateFilter(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsUpdates.driverUpdateFilter"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.driverUpdateFilter")

