from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesContentApprovalRule(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastEvaluatedDateTime: Optional[datetime] = Field(alias="lastEvaluatedDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	contentFilter: SerializeAsAny[Optional[WindowsUpdatesContentFilter]] = Field(alias="contentFilter",default=None,)
	durationBeforeDeploymentStart: Optional[str] = Field(alias="durationBeforeDeploymentStart",default=None,)

from .windows_updates_content_filter import WindowsUpdatesContentFilter

