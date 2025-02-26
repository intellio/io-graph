from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChartFont(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	bold: Optional[bool] = Field(default=None,alias="bold",)
	color: Optional[str] = Field(default=None,alias="color",)
	italic: Optional[bool] = Field(default=None,alias="italic",)
	name: Optional[str] = Field(default=None,alias="name",)
	size: Optional[float] | Optional[str] | ReferenceNumeric
	underline: Optional[str] = Field(default=None,alias="underline",)

from .reference_numeric import ReferenceNumeric

