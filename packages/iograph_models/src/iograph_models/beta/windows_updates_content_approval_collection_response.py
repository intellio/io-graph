from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsUpdatesContentApprovalCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsUpdatesContentApproval]] = Field(alias="value", default=None,)

from .windows_updates_content_approval import WindowsUpdatesContentApproval
