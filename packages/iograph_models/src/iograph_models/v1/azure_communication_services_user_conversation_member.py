from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AzureCommunicationServicesUserConversationMember(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.azureCommunicationServicesUserConversationMember"] = Field(alias="@odata.type", default="#microsoft.graph.azureCommunicationServicesUserConversationMember")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	roles: Optional[list[str]] = Field(alias="roles", default=None,)
	visibleHistoryStartDateTime: Optional[datetime] = Field(alias="visibleHistoryStartDateTime", default=None,)
	azureCommunicationServicesId: Optional[str] = Field(alias="azureCommunicationServicesId", default=None,)


