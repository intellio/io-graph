from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DocumentSetVersion(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	publication: Optional[PublicationFacet] = Field(alias="publication",default=None,)
	fields: Optional[FieldValueSet] = Field(alias="fields",default=None,)
	comment: Optional[str] = Field(alias="comment",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	items: Optional[list[DocumentSetVersionItem]] = Field(alias="items",default=None,)
	shouldCaptureMinorVersion: Optional[bool] = Field(alias="shouldCaptureMinorVersion",default=None,)

from .identity_set import IdentitySet
from .publication_facet import PublicationFacet
from .field_value_set import FieldValueSet
from .identity_set import IdentitySet
from .document_set_version_item import DocumentSetVersionItem

