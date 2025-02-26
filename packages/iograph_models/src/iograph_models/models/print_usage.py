from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class PrintUsage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	blackAndWhitePageCount: Optional[int] = Field(default=None,alias="blackAndWhitePageCount",)
	colorPageCount: Optional[int] = Field(default=None,alias="colorPageCount",)
	completedBlackAndWhiteJobCount: Optional[int] = Field(default=None,alias="completedBlackAndWhiteJobCount",)
	completedColorJobCount: Optional[int] = Field(default=None,alias="completedColorJobCount",)
	completedJobCount: Optional[int] = Field(default=None,alias="completedJobCount",)
	doubleSidedSheetCount: Optional[int] = Field(default=None,alias="doubleSidedSheetCount",)
	incompleteJobCount: Optional[int] = Field(default=None,alias="incompleteJobCount",)
	mediaSheetCount: Optional[int] = Field(default=None,alias="mediaSheetCount",)
	pageCount: Optional[int] = Field(default=None,alias="pageCount",)
	singleSidedSheetCount: Optional[int] = Field(default=None,alias="singleSidedSheetCount",)
	usageDate: Optional[str] = Field(default=None,alias="usageDate",)

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
			if mapping_key == "#microsoft.graph.printUsageByPrinter":
				from .print_usage_by_printer import PrintUsageByPrinter
				return PrintUsageByPrinter.model_validate(data)
			if mapping_key == "#microsoft.graph.printUsageByUser":
				from .print_usage_by_user import PrintUsageByUser
				return PrintUsageByUser.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


