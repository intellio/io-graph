from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class OnUserCreateStartExternalUsersSelfServiceSignUp(BaseModel):
	odata_type: Literal["#microsoft.graph.onUserCreateStartExternalUsersSelfServiceSignUp"] = Field(alias="@odata.type", default="#microsoft.graph.onUserCreateStartExternalUsersSelfServiceSignUp")
	userTypeToCreate: Optional[UserType | str] = Field(alias="userTypeToCreate", default=None,)

from .user_type import UserType

