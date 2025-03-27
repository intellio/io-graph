from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DocumentSet(BaseModel):
	allowedContentTypes: Optional[list[ContentTypeInfo]] = Field(alias="allowedContentTypes", default=None,)
	defaultContents: Optional[list[DocumentSetContent]] = Field(alias="defaultContents", default=None,)
	propagateWelcomePageChanges: Optional[bool] = Field(alias="propagateWelcomePageChanges", default=None,)
	shouldPrefixNameToFile: Optional[bool] = Field(alias="shouldPrefixNameToFile", default=None,)
	welcomePageUrl: Optional[str] = Field(alias="welcomePageUrl", default=None,)
	sharedColumns: Optional[list[ColumnDefinition]] = Field(alias="sharedColumns", default=None,)
	welcomePageColumns: Optional[list[ColumnDefinition]] = Field(alias="welcomePageColumns", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .content_type_info import ContentTypeInfo
from .document_set_content import DocumentSetContent
from .column_definition import ColumnDefinition
from .column_definition import ColumnDefinition

