from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsUpdatesUpdateCategoryEnrollmentInformation(BaseModel):
	enrollmentState: Optional[WindowsUpdatesEnrollmentState | str] = Field(alias="enrollmentState", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_updates_enrollment_state import WindowsUpdatesEnrollmentState
