from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class ConversationMemberCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AadUserConversationMember, AnonymousGuestConversationMember, AzureCommunicationServicesUserConversationMember, MicrosoftAccountUserConversationMember, SkypeForBusinessUserConversationMember, SkypeUserConversationMember]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .aad_user_conversation_member import AadUserConversationMember
from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
from .skype_user_conversation_member import SkypeUserConversationMember

