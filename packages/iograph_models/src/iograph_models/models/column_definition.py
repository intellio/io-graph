from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ColumnDefinition(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	boolean: Optional[BooleanColumn] = Field(default=None,alias="boolean",)
	calculated: Optional[CalculatedColumn] = Field(default=None,alias="calculated",)
	choice: Optional[ChoiceColumn] = Field(default=None,alias="choice",)
	columnGroup: Optional[str] = Field(default=None,alias="columnGroup",)
	contentApprovalStatus: Optional[ContentApprovalStatusColumn] = Field(default=None,alias="contentApprovalStatus",)
	currency: Optional[CurrencyColumn] = Field(default=None,alias="currency",)
	dateTime: Optional[DateTimeColumn] = Field(default=None,alias="dateTime",)
	defaultValue: Optional[DefaultColumnValue] = Field(default=None,alias="defaultValue",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	enforceUniqueValues: Optional[bool] = Field(default=None,alias="enforceUniqueValues",)
	geolocation: Optional[GeolocationColumn] = Field(default=None,alias="geolocation",)
	hidden: Optional[bool] = Field(default=None,alias="hidden",)
	hyperlinkOrPicture: Optional[HyperlinkOrPictureColumn] = Field(default=None,alias="hyperlinkOrPicture",)
	indexed: Optional[bool] = Field(default=None,alias="indexed",)
	isDeletable: Optional[bool] = Field(default=None,alias="isDeletable",)
	isReorderable: Optional[bool] = Field(default=None,alias="isReorderable",)
	isSealed: Optional[bool] = Field(default=None,alias="isSealed",)
	lookup: Optional[LookupColumn] = Field(default=None,alias="lookup",)
	name: Optional[str] = Field(default=None,alias="name",)
	number: Optional[NumberColumn] = Field(default=None,alias="number",)
	personOrGroup: Optional[PersonOrGroupColumn] = Field(default=None,alias="personOrGroup",)
	propagateChanges: Optional[bool] = Field(default=None,alias="propagateChanges",)
	readOnly: Optional[bool] = Field(default=None,alias="readOnly",)
	required: Optional[bool] = Field(default=None,alias="required",)
	sourceContentType: Optional[ContentTypeInfo] = Field(default=None,alias="sourceContentType",)
	term: Optional[TermColumn] = Field(default=None,alias="term",)
	text: Optional[TextColumn] = Field(default=None,alias="text",)
	thumbnail: Optional[ThumbnailColumn] = Field(default=None,alias="thumbnail",)
	type: Optional[ColumnTypes] = Field(default=None,alias="type",)
	validation: Optional[ColumnValidation] = Field(default=None,alias="validation",)
	sourceColumn: Optional[ColumnDefinition] = Field(default=None,alias="sourceColumn",)

from .boolean_column import BooleanColumn
from .calculated_column import CalculatedColumn
from .choice_column import ChoiceColumn
from .content_approval_status_column import ContentApprovalStatusColumn
from .currency_column import CurrencyColumn
from .date_time_column import DateTimeColumn
from .default_column_value import DefaultColumnValue
from .geolocation_column import GeolocationColumn
from .hyperlink_or_picture_column import HyperlinkOrPictureColumn
from .lookup_column import LookupColumn
from .number_column import NumberColumn
from .person_or_group_column import PersonOrGroupColumn
from .content_type_info import ContentTypeInfo
from .term_column import TermColumn
from .text_column import TextColumn
from .thumbnail_column import ThumbnailColumn
from .column_types import ColumnTypes
from .column_validation import ColumnValidation

