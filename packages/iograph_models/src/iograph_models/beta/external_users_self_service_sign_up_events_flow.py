from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalUsersSelfServiceSignUpEventsFlow(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalUsersSelfServiceSignUpEventsFlow"] = Field(alias="@odata.type", default="#microsoft.graph.externalUsersSelfServiceSignUpEventsFlow")
	conditions: Optional[AuthenticationConditions] = Field(alias="conditions", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	onAttributeCollection: Optional[Union[OnAttributeCollectionExternalUsersSelfServiceSignUp]] = Field(alias="onAttributeCollection", default=None,discriminator="odata_type", )
	onAttributeCollectionStart: Optional[Union[OnAttributeCollectionStartCustomExtensionHandler]] = Field(alias="onAttributeCollectionStart", default=None,discriminator="odata_type", )
	onAttributeCollectionSubmit: Optional[Union[OnAttributeCollectionSubmitCustomExtensionHandler]] = Field(alias="onAttributeCollectionSubmit", default=None,discriminator="odata_type", )
	onAuthenticationMethodLoadStart: Optional[Union[OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp]] = Field(alias="onAuthenticationMethodLoadStart", default=None,discriminator="odata_type", )
	onInteractiveAuthFlowStart: Optional[Union[OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp]] = Field(alias="onInteractiveAuthFlowStart", default=None,discriminator="odata_type", )
	onUserCreateStart: Optional[Union[OnUserCreateStartExternalUsersSelfServiceSignUp]] = Field(alias="onUserCreateStart", default=None,discriminator="odata_type", )

from .authentication_conditions import AuthenticationConditions
from .on_attribute_collection_external_users_self_service_sign_up import OnAttributeCollectionExternalUsersSelfServiceSignUp
from .on_attribute_collection_start_custom_extension_handler import OnAttributeCollectionStartCustomExtensionHandler
from .on_attribute_collection_submit_custom_extension_handler import OnAttributeCollectionSubmitCustomExtensionHandler
from .on_authentication_method_load_start_external_users_self_service_sign_up import OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp
from .on_interactive_auth_flow_start_external_users_self_service_sign_up import OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp
from .on_user_create_start_external_users_self_service_sign_up import OnUserCreateStartExternalUsersSelfServiceSignUp

