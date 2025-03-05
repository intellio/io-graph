from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HyperlinkOrPictureColumn(BaseModel):
	isPicture: Optional[bool] = Field(default=None,alias="isPicture",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


