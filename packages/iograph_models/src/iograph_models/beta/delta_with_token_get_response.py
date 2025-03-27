from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Delta_with_tokenGetResponse(BaseModel):
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	odata_deltaLink: Optional[str] = Field(alias="@odata.deltaLink", default=None,)
	value: Optional[list[ListItem]] = Field(alias="value", default=None,)

from .list_item import ListItem

