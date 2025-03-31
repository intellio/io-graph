from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class DepEnrollmentBaseProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DepIOSEnrollmentProfile, DepMacOSEnrollmentProfile],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
