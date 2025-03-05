from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class OnenoteEntityBaseModel(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	self: Optional[str] = Field(alias="self",default=None,)

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
			if mapping_key == "#microsoft.graph.onenoteEntitySchemaObjectModel":
				from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
				return OnenoteEntitySchemaObjectModel.model_validate(data)
			if mapping_key == "#microsoft.graph.onenoteEntityHierarchyModel":
				from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
				return OnenoteEntityHierarchyModel.model_validate(data)
			if mapping_key == "#microsoft.graph.notebook":
				from .notebook import Notebook
				return Notebook.model_validate(data)
			if mapping_key == "#microsoft.graph.onenoteSection":
				from .onenote_section import OnenoteSection
				return OnenoteSection.model_validate(data)
			if mapping_key == "#microsoft.graph.sectionGroup":
				from .section_group import SectionGroup
				return SectionGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.onenotePage":
				from .onenote_page import OnenotePage
				return OnenotePage.model_validate(data)
			if mapping_key == "#microsoft.graph.onenoteResource":
				from .onenote_resource import OnenoteResource
				return OnenoteResource.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


