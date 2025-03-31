from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class TeamsAppIcon(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamsAppIcon"] = Field(alias="@odata.type",)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	hostedContent: Optional[Union[ChatMessageHostedContent]] = Field(alias="hostedContent", default=None,discriminator="odata_type", )

from .chat_message_hosted_content import ChatMessageHostedContent
