from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class OnInteractiveAuthFlowStartListener(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.onInteractiveAuthFlowStartListener"] = Field(alias="@odata.type", default="#microsoft.graph.onInteractiveAuthFlowStartListener")
	authenticationEventsFlowId: Optional[str] = Field(alias="authenticationEventsFlowId", default=None,)
	conditions: Optional[AuthenticationConditions] = Field(alias="conditions", default=None,)
	handler: Optional[Union[OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp]] = Field(alias="handler", default=None,discriminator="odata_type", )

from .authentication_conditions import AuthenticationConditions
from .on_interactive_auth_flow_start_external_users_self_service_sign_up import OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp

