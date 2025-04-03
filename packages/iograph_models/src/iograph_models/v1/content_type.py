from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ContentType(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.contentType"] = Field(alias="@odata.type", default="#microsoft.graph.contentType")
	associatedHubsUrls: Optional[list[str]] = Field(alias="associatedHubsUrls", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	documentSet: Optional[DocumentSet] = Field(alias="documentSet", default=None,)
	documentTemplate: Optional[DocumentSetContent] = Field(alias="documentTemplate", default=None,)
	group: Optional[str] = Field(alias="group", default=None,)
	hidden: Optional[bool] = Field(alias="hidden", default=None,)
	inheritedFrom: Optional[ItemReference] = Field(alias="inheritedFrom", default=None,)
	isBuiltIn: Optional[bool] = Field(alias="isBuiltIn", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	order: Optional[ContentTypeOrder] = Field(alias="order", default=None,)
	parentId: Optional[str] = Field(alias="parentId", default=None,)
	propagateChanges: Optional[bool] = Field(alias="propagateChanges", default=None,)
	readOnly: Optional[bool] = Field(alias="readOnly", default=None,)
	sealed: Optional[bool] = Field(alias="sealed", default=None,)
	base: Optional[ContentType] = Field(alias="base", default=None,)
	baseTypes: Optional[list[ContentType]] = Field(alias="baseTypes", default=None,)
	columnLinks: Optional[list[ColumnLink]] = Field(alias="columnLinks", default=None,)
	columnPositions: Optional[list[ColumnDefinition]] = Field(alias="columnPositions", default=None,)
	columns: Optional[list[ColumnDefinition]] = Field(alias="columns", default=None,)

from .document_set import DocumentSet
from .document_set_content import DocumentSetContent
from .item_reference import ItemReference
from .content_type_order import ContentTypeOrder
from .column_link import ColumnLink
from .column_definition import ColumnDefinition
