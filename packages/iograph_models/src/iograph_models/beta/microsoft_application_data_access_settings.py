from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MicrosoftApplicationDataAccessSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.microsoftApplicationDataAccessSettings"] = Field(alias="@odata.type", default="#microsoft.graph.microsoftApplicationDataAccessSettings")
	disabledForGroup: Optional[str] = Field(alias="disabledForGroup", default=None,)
	isEnabledForAllMicrosoftApplications: Optional[bool] = Field(alias="isEnabledForAllMicrosoftApplications", default=None,)

