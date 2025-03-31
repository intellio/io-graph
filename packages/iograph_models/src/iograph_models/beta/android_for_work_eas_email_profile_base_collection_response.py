from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AndroidForWorkEasEmailProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AndroidForWorkGmailEasConfiguration, AndroidForWorkNineWorkEasConfiguration],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .android_for_work_gmail_eas_configuration import AndroidForWorkGmailEasConfiguration
from .android_for_work_nine_work_eas_configuration import AndroidForWorkNineWorkEasConfiguration
