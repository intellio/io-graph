from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeltaGetResponse(BaseModel):
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	odata_deltaLink: Optional[str] = Field(alias="@odata.deltaLink", default=None,)
	value: Optional[list[User]] = Field(alias="value", default=None,)

from .user import User

