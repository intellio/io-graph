from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityUserFlowCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[B2cIdentityUserFlow, B2xIdentityUserFlow]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .b2c_identity_user_flow import B2cIdentityUserFlow
from .b2x_identity_user_flow import B2xIdentityUserFlow

