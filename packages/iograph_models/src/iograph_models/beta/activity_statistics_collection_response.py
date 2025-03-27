from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class ActivityStatisticsCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[CallActivityStatistics, ChatActivityStatistics, EmailActivityStatistics, FocusActivityStatistics, MeetingActivityStatistics]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .call_activity_statistics import CallActivityStatistics
from .chat_activity_statistics import ChatActivityStatistics
from .email_activity_statistics import EmailActivityStatistics
from .focus_activity_statistics import FocusActivityStatistics
from .meeting_activity_statistics import MeetingActivityStatistics

