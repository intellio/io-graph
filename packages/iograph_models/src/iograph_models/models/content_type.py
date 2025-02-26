from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ContentType(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	associatedHubsUrls: list[Optional[str]] = Field(alias="associatedHubsUrls",)
	description: Optional[str] = Field(default=None,alias="description",)
	documentSet: Optional[DocumentSet] = Field(default=None,alias="documentSet",)
	documentTemplate: Optional[DocumentSetContent] = Field(default=None,alias="documentTemplate",)
	group: Optional[str] = Field(default=None,alias="group",)
	hidden: Optional[bool] = Field(default=None,alias="hidden",)
	inheritedFrom: Optional[ItemReference] = Field(default=None,alias="inheritedFrom",)
	isBuiltIn: Optional[bool] = Field(default=None,alias="isBuiltIn",)
	name: Optional[str] = Field(default=None,alias="name",)
	order: Optional[ContentTypeOrder] = Field(default=None,alias="order",)
	parentId: Optional[str] = Field(default=None,alias="parentId",)
	propagateChanges: Optional[bool] = Field(default=None,alias="propagateChanges",)
	readOnly: Optional[bool] = Field(default=None,alias="readOnly",)
	sealed: Optional[bool] = Field(default=None,alias="sealed",)
	base: Optional[ContentType] = Field(default=None,alias="base",)
	baseTypes: list[ContentType] = Field(alias="baseTypes",)
	columnLinks: list[ColumnLink] = Field(alias="columnLinks",)
	columnPositions: list[ColumnDefinition] = Field(alias="columnPositions",)
	columns: list[ColumnDefinition] = Field(alias="columns",)

from .document_set import DocumentSet
from .document_set_content import DocumentSetContent
from .item_reference import ItemReference
from .content_type_order import ContentTypeOrder
from .column_link import ColumnLink
from .column_definition import ColumnDefinition
from .column_definition import ColumnDefinition

