from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CampaignSchedule(BaseModel):
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime",default=None,)
	launchDateTime: Optional[datetime] = Field(alias="launchDateTime",default=None,)
	status: Optional[CampaignStatus | str] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .campaign_status import CampaignStatus

