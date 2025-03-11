from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedAppLogUpload(BaseModel):
	managedAppComponent: Optional[str] = Field(alias="managedAppComponent",default=None,)
	managedAppComponentDescription: Optional[str] = Field(alias="managedAppComponentDescription",default=None,)
	referenceId: Optional[str] = Field(alias="referenceId",default=None,)
	status: Optional[ManagedAppLogUploadState | str] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .managed_app_log_upload_state import ManagedAppLogUploadState

