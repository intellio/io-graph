from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnlineMeetingRestricted(BaseModel):
	contentSharingDisabled: Optional[OnlineMeetingContentSharingDisabledReason | str] = Field(alias="contentSharingDisabled", default=None,)
	videoDisabled: Optional[OnlineMeetingVideoDisabledReason | str] = Field(alias="videoDisabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .online_meeting_content_sharing_disabled_reason import OnlineMeetingContentSharingDisabledReason
from .online_meeting_video_disabled_reason import OnlineMeetingVideoDisabledReason

