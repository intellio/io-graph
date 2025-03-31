from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookFunctionResult(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookFunctionResult"] = Field(alias="@odata.type",)
	error: Optional[str] = Field(alias="error", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)

