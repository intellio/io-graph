from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookChartFont(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	bold: Optional[bool] = Field(alias="bold", default=None,)
	color: Optional[str] = Field(alias="color", default=None,)
	italic: Optional[bool] = Field(alias="italic", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	size: float | str | ReferenceNumeric
	underline: Optional[str] = Field(alias="underline", default=None,)

from .reference_numeric import ReferenceNumeric

