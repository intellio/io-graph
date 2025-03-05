from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnlineMeetingRestricted(BaseModel):
	contentSharingDisabled: Optional[OnlineMeetingContentSharingDisabledReason] = Field(default=None,alias="contentSharingDisabled",)
	videoDisabled: Optional[OnlineMeetingVideoDisabledReason] = Field(default=None,alias="videoDisabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .online_meeting_content_sharing_disabled_reason import OnlineMeetingContentSharingDisabledReason
from .online_meeting_video_disabled_reason import OnlineMeetingVideoDisabledReason

