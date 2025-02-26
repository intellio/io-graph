from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TextColumn(BaseModel):
	allowMultipleLines: Optional[bool] = Field(default=None,alias="allowMultipleLines",)
	appendChangesToExistingText: Optional[bool] = Field(default=None,alias="appendChangesToExistingText",)
	linesForEditing: Optional[int] = Field(default=None,alias="linesForEditing",)
	maxLength: Optional[int] = Field(default=None,alias="maxLength",)
	textType: Optional[str] = Field(default=None,alias="textType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


