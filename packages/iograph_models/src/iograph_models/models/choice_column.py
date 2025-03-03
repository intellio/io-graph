from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChoiceColumn(BaseModel):
	allowTextEntry: Optional[bool] = Field(default=None,alias="allowTextEntry",)
	choices: Optional[list[str]] = Field(default=None,alias="choices",)
	displayAs: Optional[str] = Field(default=None,alias="displayAs",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


