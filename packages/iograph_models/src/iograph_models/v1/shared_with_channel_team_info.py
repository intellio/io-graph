from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class SharedWithChannelTeamInfo(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.sharedWithChannelTeamInfo"] = Field(alias="@odata.type", default="#microsoft.graph.sharedWithChannelTeamInfo")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	team: Optional[Team] = Field(alias="team", default=None,)
	isHostTeam: Optional[bool] = Field(alias="isHostTeam", default=None,)
	allowedMembers: Optional[list[Annotated[Union[AadUserConversationMember, AnonymousGuestConversationMember, AzureCommunicationServicesUserConversationMember, MicrosoftAccountUserConversationMember, SkypeForBusinessUserConversationMember, SkypeUserConversationMember],Field(discriminator="odata_type")]]] = Field(alias="allowedMembers", default=None,)

from .team import Team
from .aad_user_conversation_member import AadUserConversationMember
from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
from .skype_user_conversation_member import SkypeUserConversationMember
