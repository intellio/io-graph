from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesUpdateManagementEnrollment(BaseModel):
	driver: Optional[WindowsUpdatesUpdateCategoryEnrollmentInformation] = Field(alias="driver", default=None,)
	feature: Optional[WindowsUpdatesUpdateCategoryEnrollmentInformation] = Field(alias="feature", default=None,)
	quality: Optional[WindowsUpdatesUpdateCategoryEnrollmentInformation] = Field(alias="quality", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_updates_update_category_enrollment_information import WindowsUpdatesUpdateCategoryEnrollmentInformation
from .windows_updates_update_category_enrollment_information import WindowsUpdatesUpdateCategoryEnrollmentInformation
from .windows_updates_update_category_enrollment_information import WindowsUpdatesUpdateCategoryEnrollmentInformation

