from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppListItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AppListItem]] = Field(alias="value", default=None,)

from .app_list_item import AppListItem
