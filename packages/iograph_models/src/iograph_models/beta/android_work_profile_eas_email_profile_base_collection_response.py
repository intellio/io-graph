from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AndroidWorkProfileEasEmailProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AndroidWorkProfileGmailEasConfiguration, AndroidWorkProfileNineWorkEasConfiguration],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
