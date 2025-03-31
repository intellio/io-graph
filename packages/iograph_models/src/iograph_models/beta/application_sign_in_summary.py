from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ApplicationSignInSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.applicationSignInSummary"] = Field(alias="@odata.type",)
	appDisplayName: Optional[str] = Field(alias="appDisplayName", default=None,)
	failedSignInCount: Optional[int] = Field(alias="failedSignInCount", default=None,)
	successfulSignInCount: Optional[int] = Field(alias="successfulSignInCount", default=None,)
	successPercentage: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
