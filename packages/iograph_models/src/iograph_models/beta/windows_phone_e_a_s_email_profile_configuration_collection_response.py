from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsPhoneEASEmailProfileConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsPhoneEASEmailProfileConfiguration]] = Field(alias="value", default=None,)

from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration

