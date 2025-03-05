from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AutomaticRepliesSetting(BaseModel):
	externalAudience: Optional[ExternalAudienceScope | str] = Field(alias="externalAudience",default=None,)
	externalReplyMessage: Optional[str] = Field(alias="externalReplyMessage",default=None,)
	internalReplyMessage: Optional[str] = Field(alias="internalReplyMessage",default=None,)
	scheduledEndDateTime: Optional[DateTimeTimeZone] = Field(alias="scheduledEndDateTime",default=None,)
	scheduledStartDateTime: Optional[DateTimeTimeZone] = Field(alias="scheduledStartDateTime",default=None,)
	status: Optional[AutomaticRepliesStatus | str] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .external_audience_scope import ExternalAudienceScope
from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone
from .automatic_replies_status import AutomaticRepliesStatus

