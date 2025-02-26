from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AutomaticRepliesSetting(BaseModel):
	externalAudience: Optional[ExternalAudienceScope] = Field(default=None,alias="externalAudience",)
	externalReplyMessage: Optional[str] = Field(default=None,alias="externalReplyMessage",)
	internalReplyMessage: Optional[str] = Field(default=None,alias="internalReplyMessage",)
	scheduledEndDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="scheduledEndDateTime",)
	scheduledStartDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="scheduledStartDateTime",)
	status: Optional[AutomaticRepliesStatus] = Field(default=None,alias="status",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .external_audience_scope import ExternalAudienceScope
from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone
from .automatic_replies_status import AutomaticRepliesStatus

