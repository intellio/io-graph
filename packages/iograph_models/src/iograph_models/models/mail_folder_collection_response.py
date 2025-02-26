from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MailFolderCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MailFolder] = Field(alias="value",)

from .mail_folder import MailFolder

