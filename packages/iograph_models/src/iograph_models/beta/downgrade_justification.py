from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DowngradeJustification(BaseModel):
	isDowngradeJustified: Optional[bool] = Field(alias="isDowngradeJustified",default=None,)
	justificationMessage: Optional[str] = Field(alias="justificationMessage",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


