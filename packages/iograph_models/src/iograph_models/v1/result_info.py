from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ResultInfo(BaseModel):
	code: Optional[int] = Field(alias="code",default=None,)
	message: Optional[str] = Field(alias="message",default=None,)
	subcode: Optional[int] = Field(alias="subcode",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


