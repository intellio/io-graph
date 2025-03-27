from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class OutgoingCallOptions(BaseModel):
	hideBotAfterEscalation: Optional[bool] = Field(alias="hideBotAfterEscalation", default=None,)
	isContentSharingNotificationEnabled: Optional[bool] = Field(alias="isContentSharingNotificationEnabled", default=None,)
	isDeltaRosterEnabled: Optional[bool] = Field(alias="isDeltaRosterEnabled", default=None,)
	odata_type: Literal["#microsoft.graph.outgoingCallOptions"] = Field(alias="@odata.type", default="#microsoft.graph.outgoingCallOptions")


