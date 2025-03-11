from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MoveAction(BaseModel):
	from_: Optional[str] = Field(alias="from",default=None,)
	to: Optional[str] = Field(alias="to",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


