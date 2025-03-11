from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Office365GroupsActivityCounts(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	exchangeEmailsReceived: Optional[int] = Field(alias="exchangeEmailsReceived",default=None,)
	reportDate: Optional[str] = Field(alias="reportDate",default=None,)
	reportPeriod: Optional[str] = Field(alias="reportPeriod",default=None,)
	reportRefreshDate: Optional[str] = Field(alias="reportRefreshDate",default=None,)
	teamsChannelMessages: Optional[int] = Field(alias="teamsChannelMessages",default=None,)
	teamsMeetingsOrganized: Optional[int] = Field(alias="teamsMeetingsOrganized",default=None,)
	yammerMessagesLiked: Optional[int] = Field(alias="yammerMessagesLiked",default=None,)
	yammerMessagesPosted: Optional[int] = Field(alias="yammerMessagesPosted",default=None,)
	yammerMessagesRead: Optional[int] = Field(alias="yammerMessagesRead",default=None,)


