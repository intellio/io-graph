from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppContentFile(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	azureStorageUri: Optional[str] = Field(default=None,alias="azureStorageUri",)
	azureStorageUriExpirationDateTime: Optional[datetime] = Field(default=None,alias="azureStorageUriExpirationDateTime",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	isCommitted: Optional[bool] = Field(default=None,alias="isCommitted",)
	isDependency: Optional[bool] = Field(default=None,alias="isDependency",)
	manifest: Optional[str] = Field(default=None,alias="manifest",)
	name: Optional[str] = Field(default=None,alias="name",)
	size: Optional[int] = Field(default=None,alias="size",)
	sizeEncrypted: Optional[int] = Field(default=None,alias="sizeEncrypted",)
	uploadState: Optional[MobileAppContentFileUploadState] = Field(default=None,alias="uploadState",)

from .mobile_app_content_file_upload_state import MobileAppContentFileUploadState

