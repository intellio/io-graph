from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class WindowsKioskVisitor(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsKioskVisitor"] = Field(alias="@odata.type", default="#microsoft.graph.windowsKioskVisitor")

