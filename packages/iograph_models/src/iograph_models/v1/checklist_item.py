from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ChecklistItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.checklistItem"] = Field(alias="@odata.type",)
	checkedDateTime: Optional[datetime] = Field(alias="checkedDateTime", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isChecked: Optional[bool] = Field(alias="isChecked", default=None,)

