from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class OnUserCreateStartListener(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.onUserCreateStartListener"] = Field(alias="@odata.type", default="#microsoft.graph.onUserCreateStartListener")
	authenticationEventsFlowId: Optional[str] = Field(alias="authenticationEventsFlowId", default=None,)
	conditions: Optional[AuthenticationConditions] = Field(alias="conditions", default=None,)
	handler: Optional[Union[OnUserCreateStartExternalUsersSelfServiceSignUp]] = Field(alias="handler", default=None,discriminator="odata_type", )

from .authentication_conditions import AuthenticationConditions
from .on_user_create_start_external_users_self_service_sign_up import OnUserCreateStartExternalUsersSelfServiceSignUp

