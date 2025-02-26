from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DocumentSet(BaseModel):
	allowedContentTypes: list[ContentTypeInfo] = Field(alias="allowedContentTypes",)
	defaultContents: list[DocumentSetContent] = Field(alias="defaultContents",)
	propagateWelcomePageChanges: Optional[bool] = Field(default=None,alias="propagateWelcomePageChanges",)
	shouldPrefixNameToFile: Optional[bool] = Field(default=None,alias="shouldPrefixNameToFile",)
	welcomePageUrl: Optional[str] = Field(default=None,alias="welcomePageUrl",)
	sharedColumns: list[ColumnDefinition] = Field(alias="sharedColumns",)
	welcomePageColumns: list[ColumnDefinition] = Field(alias="welcomePageColumns",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .content_type_info import ContentTypeInfo
from .document_set_content import DocumentSetContent
from .column_definition import ColumnDefinition
from .column_definition import ColumnDefinition

