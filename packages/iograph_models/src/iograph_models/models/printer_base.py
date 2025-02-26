from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class PrinterBase(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	capabilities: Optional[PrinterCapabilities] = Field(default=None,alias="capabilities",)
	defaults: Optional[PrinterDefaults] = Field(default=None,alias="defaults",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isAcceptingJobs: Optional[bool] = Field(default=None,alias="isAcceptingJobs",)
	location: Optional[PrinterLocation] = Field(default=None,alias="location",)
	manufacturer: Optional[str] = Field(default=None,alias="manufacturer",)
	model: Optional[str] = Field(default=None,alias="model",)
	status: Optional[PrinterStatus] = Field(default=None,alias="status",)
	jobs: list[PrintJob] = Field(alias="jobs",)

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

