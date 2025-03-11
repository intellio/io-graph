from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HyperlinkOrPictureColumn(BaseModel):
	isPicture: Optional[bool] = Field(alias="isPicture",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


