from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class RemovePostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AadUserConversationMemberResult],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .aad_user_conversation_member_result import AadUserConversationMemberResult
