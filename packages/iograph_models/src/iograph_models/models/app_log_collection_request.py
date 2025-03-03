from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AppLogCollectionRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	customLogFolders: Optional[list[str]] = Field(default=None,alias="customLogFolders",)
	errorMessage: Optional[str] = Field(default=None,alias="errorMessage",)
	status: Optional[AppLogUploadState] = Field(default=None,alias="status",)

from .app_log_upload_state import AppLogUploadState

