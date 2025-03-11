from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ReferenceAttachment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	contentType: Optional[str] = Field(alias="contentType",default=None,)
	isInline: Optional[bool] = Field(alias="isInline",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	size: Optional[int] = Field(alias="size",default=None,)
	isFolder: Optional[bool] = Field(alias="isFolder",default=None,)
	permission: Optional[ReferenceAttachmentPermission | str] = Field(alias="permission",default=None,)
	previewUrl: Optional[str] = Field(alias="previewUrl",default=None,)
	providerType: Optional[ReferenceAttachmentProvider | str] = Field(alias="providerType",default=None,)
	sourceUrl: Optional[str] = Field(alias="sourceUrl",default=None,)
	thumbnailUrl: Optional[str] = Field(alias="thumbnailUrl",default=None,)

from .reference_attachment_permission import ReferenceAttachmentPermission
from .reference_attachment_provider import ReferenceAttachmentProvider

