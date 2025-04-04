from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccountAlias(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	idType: Optional[str] = Field(alias="idType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

