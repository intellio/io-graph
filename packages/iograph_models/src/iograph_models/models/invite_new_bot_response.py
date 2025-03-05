from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InviteNewBotResponse(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	inviteUri: Optional[str] = Field(alias="inviteUri",default=None,)


