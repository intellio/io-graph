from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsUpdatesKnownIssueHistoryItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsUpdatesKnownIssueHistoryItem]] = Field(alias="value", default=None,)

from .windows_updates_known_issue_history_item import WindowsUpdatesKnownIssueHistoryItem
