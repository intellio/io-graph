from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class PrintUsage(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	blackAndWhitePageCount: Optional[int] = Field(alias="blackAndWhitePageCount",default=None,)
	colorPageCount: Optional[int] = Field(alias="colorPageCount",default=None,)
	completedBlackAndWhiteJobCount: Optional[int] = Field(alias="completedBlackAndWhiteJobCount",default=None,)
	completedColorJobCount: Optional[int] = Field(alias="completedColorJobCount",default=None,)
	completedJobCount: Optional[int] = Field(alias="completedJobCount",default=None,)
	doubleSidedSheetCount: Optional[int] = Field(alias="doubleSidedSheetCount",default=None,)
	incompleteJobCount: Optional[int] = Field(alias="incompleteJobCount",default=None,)
	mediaSheetCount: Optional[int] = Field(alias="mediaSheetCount",default=None,)
	pageCount: Optional[int] = Field(alias="pageCount",default=None,)
	singleSidedSheetCount: Optional[int] = Field(alias="singleSidedSheetCount",default=None,)
	usageDate: Optional[str] = Field(alias="usageDate",default=None,)

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


