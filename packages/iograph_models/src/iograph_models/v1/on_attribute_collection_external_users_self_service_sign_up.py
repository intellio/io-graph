from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class OnAttributeCollectionExternalUsersSelfServiceSignUp(BaseModel):
	odata_type: Literal["#microsoft.graph.onAttributeCollectionExternalUsersSelfServiceSignUp"] = Field(alias="@odata.type", default="#microsoft.graph.onAttributeCollectionExternalUsersSelfServiceSignUp")
	attributeCollectionPage: Optional[AuthenticationAttributeCollectionPage] = Field(alias="attributeCollectionPage", default=None,)
	attributes: Optional[list[Annotated[Union[IdentityBuiltInUserFlowAttribute, IdentityCustomUserFlowAttribute],Field(discriminator="odata_type")]]] = Field(alias="attributes", default=None,)

from .authentication_attribute_collection_page import AuthenticationAttributeCollectionPage
from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute

