from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MailSearchFolderCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[MailSearchFolder]] = Field(default=None,alias="value",)

from .mail_search_folder import MailSearchFolder

