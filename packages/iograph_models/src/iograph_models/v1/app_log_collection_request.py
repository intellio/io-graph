from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AppLogCollectionRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.appLogCollectionRequest"] = Field(alias="@odata.type", default="#microsoft.graph.appLogCollectionRequest")
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	customLogFolders: Optional[list[str]] = Field(alias="customLogFolders", default=None,)
	errorMessage: Optional[str] = Field(alias="errorMessage", default=None,)
	status: Optional[AppLogUploadState | str] = Field(alias="status", default=None,)

from .app_log_upload_state import AppLogUploadState
