from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AadUserNotificationRecipient(BaseModel):
	odata_type: Literal["#microsoft.graph.aadUserNotificationRecipient"] = Field(alias="@odata.type", default="#microsoft.graph.aadUserNotificationRecipient")
	userId: Optional[str] = Field(alias="userId", default=None,)


