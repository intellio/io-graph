from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class InviteNewBotResponse(BaseModel):
	odata_type: Literal["#microsoft.graph.inviteNewBotResponse"] = Field(alias="@odata.type", default="#microsoft.graph.inviteNewBotResponse")
	inviteUri: Optional[str] = Field(alias="inviteUri", default=None,)


