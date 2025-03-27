from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class EasEmailProfileConfigurationBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[IosEasEmailProfileConfiguration, Windows10EasEmailProfileConfiguration, WindowsPhoneEASEmailProfileConfiguration],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration

