from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class ExternalProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[ExternalUserProfile, PendingExternalUserProfile],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .external_user_profile import ExternalUserProfile
from .pending_external_user_profile import PendingExternalUserProfile
