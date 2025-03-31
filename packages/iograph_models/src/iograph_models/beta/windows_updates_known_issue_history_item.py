from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsUpdatesKnownIssueHistoryItem(BaseModel):
	body: Optional[WindowsUpdatesItemBody] = Field(alias="body", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_updates_item_body import WindowsUpdatesItemBody
