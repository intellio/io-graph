from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ColumnDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.columnDefinition"] = Field(alias="@odata.type",)
	boolean: Optional[BooleanColumn] = Field(alias="boolean", default=None,)
	calculated: Optional[CalculatedColumn] = Field(alias="calculated", default=None,)
	choice: Optional[ChoiceColumn] = Field(alias="choice", default=None,)
	columnGroup: Optional[str] = Field(alias="columnGroup", default=None,)
	contentApprovalStatus: Optional[ContentApprovalStatusColumn] = Field(alias="contentApprovalStatus", default=None,)
	currency: Optional[CurrencyColumn] = Field(alias="currency", default=None,)
	dateTime: Optional[DateTimeColumn] = Field(alias="dateTime", default=None,)
	defaultValue: Optional[DefaultColumnValue] = Field(alias="defaultValue", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enforceUniqueValues: Optional[bool] = Field(alias="enforceUniqueValues", default=None,)
	geolocation: Optional[GeolocationColumn] = Field(alias="geolocation", default=None,)
	hidden: Optional[bool] = Field(alias="hidden", default=None,)
	hyperlinkOrPicture: Optional[HyperlinkOrPictureColumn] = Field(alias="hyperlinkOrPicture", default=None,)
	indexed: Optional[bool] = Field(alias="indexed", default=None,)
	isDeletable: Optional[bool] = Field(alias="isDeletable", default=None,)
	isReorderable: Optional[bool] = Field(alias="isReorderable", default=None,)
	isSealed: Optional[bool] = Field(alias="isSealed", default=None,)
	lookup: Optional[LookupColumn] = Field(alias="lookup", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	number: Optional[NumberColumn] = Field(alias="number", default=None,)
	personOrGroup: Optional[PersonOrGroupColumn] = Field(alias="personOrGroup", default=None,)
	propagateChanges: Optional[bool] = Field(alias="propagateChanges", default=None,)
	readOnly: Optional[bool] = Field(alias="readOnly", default=None,)
	required: Optional[bool] = Field(alias="required", default=None,)
	sourceContentType: Optional[ContentTypeInfo] = Field(alias="sourceContentType", default=None,)
	term: Optional[TermColumn] = Field(alias="term", default=None,)
	text: Optional[TextColumn] = Field(alias="text", default=None,)
	thumbnail: Optional[ThumbnailColumn] = Field(alias="thumbnail", default=None,)
	type: Optional[ColumnTypes | str] = Field(alias="type", default=None,)
	validation: Optional[ColumnValidation] = Field(alias="validation", default=None,)
	sourceColumn: Optional[ColumnDefinition] = Field(alias="sourceColumn", default=None,)

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
