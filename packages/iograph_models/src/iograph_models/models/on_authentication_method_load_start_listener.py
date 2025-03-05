from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnAuthenticationMethodLoadStartListener(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authenticationEventsFlowId: Optional[str] = Field(default=None,alias="authenticationEventsFlowId",)
	conditions: Optional[AuthenticationConditions] = Field(default=None,alias="conditions",)
	handler: SerializeAsAny[Optional[OnAuthenticationMethodLoadStartHandler]] = Field(default=None,alias="handler",)

from .authentication_conditions import AuthenticationConditions
from .on_authentication_method_load_start_handler import OnAuthenticationMethodLoadStartHandler

