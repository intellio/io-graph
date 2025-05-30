from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MicrosoftStoreForBusinessAppAssignmentSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.microsoftStoreForBusinessAppAssignmentSettings"] = Field(alias="@odata.type", default="#microsoft.graph.microsoftStoreForBusinessAppAssignmentSettings")
	useDeviceContext: Optional[bool] = Field(alias="useDeviceContext", default=None,)

