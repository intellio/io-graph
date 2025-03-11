from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExchangeSettings(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	inPlaceArchiveMailboxId: Optional[str] = Field(alias="inPlaceArchiveMailboxId",default=None,)
	primaryMailboxId: Optional[str] = Field(alias="primaryMailboxId",default=None,)


