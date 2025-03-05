from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnAttributeCollectionExternalUsersSelfServiceSignUp(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	attributeCollectionPage: Optional[AuthenticationAttributeCollectionPage] = Field(default=None,alias="attributeCollectionPage",)
	attributes: Optional[list[IdentityUserFlowAttribute]] = Field(default=None,alias="attributes",)

from .authentication_attribute_collection_page import AuthenticationAttributeCollectionPage
from .identity_user_flow_attribute import IdentityUserFlowAttribute

