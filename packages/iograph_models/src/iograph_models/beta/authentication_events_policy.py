from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationEventsPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	onSignupStart: Optional[list[Annotated[Union[InvokeUserFlowListener]],Field(discriminator="odata_type")]]] = Field(alias="onSignupStart", default=None,)

from .invoke_user_flow_listener import InvokeUserFlowListener

