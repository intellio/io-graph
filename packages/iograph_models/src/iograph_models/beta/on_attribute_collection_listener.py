from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class OnAttributeCollectionListener(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.onAttributeCollectionListener"] = Field(alias="@odata.type", default="#microsoft.graph.onAttributeCollectionListener")
	authenticationEventsFlowId: Optional[str] = Field(alias="authenticationEventsFlowId", default=None,)
	conditions: Optional[AuthenticationConditions] = Field(alias="conditions", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	handler: Optional[Union[OnAttributeCollectionExternalUsersSelfServiceSignUp]] = Field(alias="handler", default=None,discriminator="odata_type", )

from .authentication_conditions import AuthenticationConditions
from .on_attribute_collection_external_users_self_service_sign_up import OnAttributeCollectionExternalUsersSelfServiceSignUp
