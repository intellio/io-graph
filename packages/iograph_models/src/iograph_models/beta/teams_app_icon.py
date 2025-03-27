from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAppIcon(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	hostedContent: Optional[Union[ChatMessageHostedContent]] = Field(alias="hostedContent", default=None,discriminator="odata_type", )

from .chat_message_hosted_content import ChatMessageHostedContent

