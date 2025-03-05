from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AppLogCollectionRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	customLogFolders: Optional[list[str]] = Field(alias="customLogFolders",default=None,)
	errorMessage: Optional[str] = Field(alias="errorMessage",default=None,)
	status: Optional[str | AppLogUploadState] = Field(alias="status",default=None,)

from .app_log_upload_state import AppLogUploadState

