from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookRangeFont(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookRangeFont"] = Field(alias="@odata.type",)
	bold: Optional[bool] = Field(alias="bold", default=None,)
	color: Optional[str] = Field(alias="color", default=None,)
	italic: Optional[bool] = Field(alias="italic", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	size: float | str | ReferenceNumeric
	underline: Optional[str] = Field(alias="underline", default=None,)

from .reference_numeric import ReferenceNumeric
