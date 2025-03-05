from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalUsersSelfServiceSignUpEventsFlow(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	conditions: Optional[AuthenticationConditions] = Field(alias="conditions",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	onAttributeCollection: SerializeAsAny[Optional[OnAttributeCollectionHandler]] = Field(alias="onAttributeCollection",default=None,)
	onAuthenticationMethodLoadStart: SerializeAsAny[Optional[OnAuthenticationMethodLoadStartHandler]] = Field(alias="onAuthenticationMethodLoadStart",default=None,)
	onInteractiveAuthFlowStart: SerializeAsAny[Optional[OnInteractiveAuthFlowStartHandler]] = Field(alias="onInteractiveAuthFlowStart",default=None,)
	onUserCreateStart: SerializeAsAny[Optional[OnUserCreateStartHandler]] = Field(alias="onUserCreateStart",default=None,)

from .authentication_conditions import AuthenticationConditions
from .on_attribute_collection_handler import OnAttributeCollectionHandler
from .on_authentication_method_load_start_handler import OnAuthenticationMethodLoadStartHandler
from .on_interactive_auth_flow_start_handler import OnInteractiveAuthFlowStartHandler
from .on_user_create_start_handler import OnUserCreateStartHandler

