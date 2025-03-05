from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalUsersSelfServiceSignUpEventsFlow(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	conditions: Optional[AuthenticationConditions] = Field(default=None,alias="conditions",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	onAttributeCollection: SerializeAsAny[Optional[OnAttributeCollectionHandler]] = Field(default=None,alias="onAttributeCollection",)
	onAuthenticationMethodLoadStart: SerializeAsAny[Optional[OnAuthenticationMethodLoadStartHandler]] = Field(default=None,alias="onAuthenticationMethodLoadStart",)
	onInteractiveAuthFlowStart: SerializeAsAny[Optional[OnInteractiveAuthFlowStartHandler]] = Field(default=None,alias="onInteractiveAuthFlowStart",)
	onUserCreateStart: SerializeAsAny[Optional[OnUserCreateStartHandler]] = Field(default=None,alias="onUserCreateStart",)

from .authentication_conditions import AuthenticationConditions
from .on_attribute_collection_handler import OnAttributeCollectionHandler
from .on_authentication_method_load_start_handler import OnAuthenticationMethodLoadStartHandler
from .on_interactive_auth_flow_start_handler import OnInteractiveAuthFlowStartHandler
from .on_user_create_start_handler import OnUserCreateStartHandler

