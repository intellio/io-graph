from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TextColumn(BaseModel):
	allowMultipleLines: Optional[bool] = Field(alias="allowMultipleLines", default=None,)
	appendChangesToExistingText: Optional[bool] = Field(alias="appendChangesToExistingText", default=None,)
	linesForEditing: Optional[int] = Field(alias="linesForEditing", default=None,)
	maxLength: Optional[int] = Field(alias="maxLength", default=None,)
	textType: Optional[str] = Field(alias="textType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

