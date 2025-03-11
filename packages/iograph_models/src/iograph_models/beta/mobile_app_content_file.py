from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppContentFile(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	azureStorageUri: Optional[str] = Field(alias="azureStorageUri",default=None,)
	azureStorageUriExpirationDateTime: Optional[datetime] = Field(alias="azureStorageUriExpirationDateTime",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	isCommitted: Optional[bool] = Field(alias="isCommitted",default=None,)
	isDependency: Optional[bool] = Field(alias="isDependency",default=None,)
	isFrameworkFile: Optional[bool] = Field(alias="isFrameworkFile",default=None,)
	manifest: Optional[str] = Field(alias="manifest",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	size: Optional[int] = Field(alias="size",default=None,)
	sizeEncrypted: Optional[int] = Field(alias="sizeEncrypted",default=None,)
	sizeEncryptedInBytes: Optional[int] = Field(alias="sizeEncryptedInBytes",default=None,)
	sizeInBytes: Optional[int] = Field(alias="sizeInBytes",default=None,)
	uploadState: Optional[MobileAppContentFileUploadState | str] = Field(alias="uploadState",default=None,)

from .mobile_app_content_file_upload_state import MobileAppContentFileUploadState

