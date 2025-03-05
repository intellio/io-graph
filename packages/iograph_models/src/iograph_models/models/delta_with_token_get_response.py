from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Delta_with_tokenGetResponse(BaseModel):
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	odata_deltaLink: Optional[str] = Field(default=None,alias="@odata.deltaLink",)
	value: Optional[list[ListItem]] = Field(default=None,alias="value",)

from .list_item import ListItem

