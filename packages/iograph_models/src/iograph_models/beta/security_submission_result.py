from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecuritySubmissionResult(BaseModel):
	category: Optional[SecuritySubmissionResultCategory | str] = Field(alias="category", default=None,)
	detail: Optional[SecuritySubmissionResultDetail | str] = Field(alias="detail", default=None,)
	detectedFiles: Optional[list[SecuritySubmissionDetectedFile]] = Field(alias="detectedFiles", default=None,)
	detectedUrls: Optional[list[str]] = Field(alias="detectedUrls", default=None,)
	userMailboxSetting: Optional[SecurityUserMailboxSetting | str] = Field(alias="userMailboxSetting", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_submission_result_category import SecuritySubmissionResultCategory
from .security_submission_result_detail import SecuritySubmissionResultDetail
from .security_submission_detected_file import SecuritySubmissionDetectedFile
from .security_user_mailbox_setting import SecurityUserMailboxSetting
