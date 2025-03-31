from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class EnrollmentProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DepIOSEnrollmentProfile, DepMacOSEnrollmentProfile, DepEnrollmentProfile, DepTvOSEnrollmentProfile, DepVisionOSEnrollmentProfile],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
from .dep_enrollment_profile import DepEnrollmentProfile
from .dep_tv_o_s_enrollment_profile import DepTvOSEnrollmentProfile
from .dep_vision_o_s_enrollment_profile import DepVisionOSEnrollmentProfile
