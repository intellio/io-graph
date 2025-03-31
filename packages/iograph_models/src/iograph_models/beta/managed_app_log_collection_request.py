from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedAppLogCollectionRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedAppLogCollectionRequest"] = Field(alias="@odata.type",)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	managedAppRegistrationId: Optional[str] = Field(alias="managedAppRegistrationId", default=None,)
	requestedBy: Optional[str] = Field(alias="requestedBy", default=None,)
	requestedByUserPrincipalName: Optional[str] = Field(alias="requestedByUserPrincipalName", default=None,)
	requestedDateTime: Optional[datetime] = Field(alias="requestedDateTime", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	uploadedLogs: Optional[list[ManagedAppLogUpload]] = Field(alias="uploadedLogs", default=None,)
	userLogUploadConsent: Optional[ManagedAppLogUploadConsent | str] = Field(alias="userLogUploadConsent", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)

from .managed_app_log_upload import ManagedAppLogUpload
from .managed_app_log_upload_consent import ManagedAppLogUploadConsent
