from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PersonOrGroupColumn(BaseModel):
	allowMultipleSelection: Optional[bool] = Field(default=None,alias="allowMultipleSelection",)
	chooseFromType: Optional[str] = Field(default=None,alias="chooseFromType",)
	displayAs: Optional[str] = Field(default=None,alias="displayAs",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


