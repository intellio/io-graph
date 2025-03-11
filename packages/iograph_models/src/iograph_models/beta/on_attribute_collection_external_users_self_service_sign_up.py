from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnAttributeCollectionExternalUsersSelfServiceSignUp(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	attributeCollectionPage: Optional[AuthenticationAttributeCollectionPage] = Field(alias="attributeCollectionPage",default=None,)
	attributes: SerializeAsAny[Optional[list[IdentityUserFlowAttribute]]] = Field(alias="attributes",default=None,)

from .authentication_attribute_collection_page import AuthenticationAttributeCollectionPage
from .identity_user_flow_attribute import IdentityUserFlowAttribute

