from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class PrinterBase(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	capabilities: Optional[PrinterCapabilities] = Field(alias="capabilities", default=None,)
	defaults: Optional[PrinterDefaults] = Field(alias="defaults", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isAcceptingJobs: Optional[bool] = Field(alias="isAcceptingJobs", default=None,)
	location: Optional[PrinterLocation] = Field(alias="location", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	status: Optional[PrinterStatus] = Field(alias="status", default=None,)
	jobs: Optional[list[PrintJob]] = Field(alias="jobs", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.printer":
				from .printer import Printer
				return Printer.model_validate(data)
			if mapping_key == "#microsoft.graph.printerShare":
				from .printer_share import PrinterShare
				return PrinterShare.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .printer_capabilities import PrinterCapabilities
from .printer_defaults import PrinterDefaults
from .printer_location import PrinterLocation
from .printer_status import PrinterStatus
from .print_job import PrintJob
