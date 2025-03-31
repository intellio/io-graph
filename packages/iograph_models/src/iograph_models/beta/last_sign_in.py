from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class LastSignIn(BaseModel):
	interactiveDateTime: Optional[datetime] = Field(alias="interactiveDateTime", default=None,)
	nonInteractiveDateTime: Optional[datetime] = Field(alias="nonInteractiveDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

