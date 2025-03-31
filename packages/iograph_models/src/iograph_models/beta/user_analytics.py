from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class UserAnalytics(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userAnalytics"] = Field(alias="@odata.type",)
	settings: Optional[Settings] = Field(alias="settings", default=None,)
	activityStatistics: Optional[list[Annotated[Union[CallActivityStatistics, ChatActivityStatistics, EmailActivityStatistics, FocusActivityStatistics, MeetingActivityStatistics],Field(discriminator="odata_type")]]] = Field(alias="activityStatistics", default=None,)

from .settings import Settings
from .call_activity_statistics import CallActivityStatistics
from .chat_activity_statistics import ChatActivityStatistics
from .email_activity_statistics import EmailActivityStatistics
from .focus_activity_statistics import FocusActivityStatistics
from .meeting_activity_statistics import MeetingActivityStatistics
