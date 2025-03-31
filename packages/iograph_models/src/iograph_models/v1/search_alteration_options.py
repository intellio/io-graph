from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchAlterationOptions(BaseModel):
	enableModification: Optional[bool] = Field(alias="enableModification", default=None,)
	enableSuggestion: Optional[bool] = Field(alias="enableSuggestion", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

