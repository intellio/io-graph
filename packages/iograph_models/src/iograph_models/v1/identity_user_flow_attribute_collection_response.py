from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityUserFlowAttributeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[IdentityBuiltInUserFlowAttribute, IdentityCustomUserFlowAttribute]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute

