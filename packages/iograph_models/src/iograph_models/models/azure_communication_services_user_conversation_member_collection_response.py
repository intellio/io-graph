from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AzureCommunicationServicesUserConversationMemberCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AzureCommunicationServicesUserConversationMember] = Field(alias="value",)

from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember

