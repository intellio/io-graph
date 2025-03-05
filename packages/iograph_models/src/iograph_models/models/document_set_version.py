from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DocumentSetVersion(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	publication: Optional[PublicationFacet] = Field(default=None,alias="publication",)
	fields: Optional[FieldValueSet] = Field(default=None,alias="fields",)
	comment: Optional[str] = Field(default=None,alias="comment",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	items: Optional[list[DocumentSetVersionItem]] = Field(default=None,alias="items",)
	shouldCaptureMinorVersion: Optional[bool] = Field(default=None,alias="shouldCaptureMinorVersion",)

from .identity_set import IdentitySet
from .publication_facet import PublicationFacet
from .field_value_set import FieldValueSet
from .identity_set import IdentitySet
from .document_set_version_item import DocumentSetVersionItem

